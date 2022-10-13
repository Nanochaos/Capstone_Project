# This Python file uses the following encoding: utf-8
from pathlib import Path
from PySide2.QtCore import (QThread)

import argparse
from YoloV5m import Detection
from YoloV5m import Heatmap
from YoloV5m import Saving
import math
import cv2

# Screen Resolution Checker
from screeninfo import get_monitors

from ui_interface import Ui_MainWindow
from Custom_Widgets.Widgets import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)

        # Variables for the image/video source
        self.fname = ('', '')

        # Default AI parameters
            #setting slider deafult values
        self.ui.confidenceSlider.setValue(opt.conf_thres*100)
        self.ui.confidenceText.setText(str(int(opt.conf_thres*100)))
        self.ui.overlapSlider.setValue(opt.iou_thres*100)
        self.ui.overlapText.setText(str(int(opt.iou_thres*100)))

            #setting check box default values
        self.ui.labelsCheckBox.setChecked(opt.hide_labels)
        self.ui.confidenceCheckBox.setChecked(opt.hide_conf)

        # EXPAND SIDE MENU
            #settings btn clicked
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.sideBarLabel.setText("        Settings"))
            #information btn clicked
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.sideBarLabel.setText("        Information"))

        # CLOSE SIDE MENU
        self.ui.sideBarCloseBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

        # CHANGES Settings and Info Button Color back to default when closed
        self.ui.sideBarCloseBtn.clicked.connect(lambda: self.ui.settingsBtn.setStyleSheet("background-color: #16191d;"))
        self.ui.sideBarCloseBtn.clicked.connect(lambda: self.ui.infoBtn.setStyleSheet("background-color: #16191d;"))

        # Open File
        self.ui.openBtn.clicked.connect(lambda: self.get_file())

        # Adding stuff to combo box
        self.ui.heatmapCombo.addItem("Current Heatmap")
        self.ui.heatmapCombo.addItem("Overall Heatmap")

        # Setting Slider Stuff
            #confidence slider
        self.ui.confidenceSlider.setRange(0, 100)
        self.ui.confidenceSlider.valueChanged.connect(
            lambda: self.ui.confidenceText.setText(str(self.ui.confidenceSlider.value())))

            #overlap threshold slider
        self.ui.overlapSlider.setRange(0, 100)
        self.ui.overlapSlider.valueChanged.connect(
            lambda: self.ui.overlapText.setText(str(self.ui.overlapSlider.value())))

        # Setting the max width and height of the software
        for m in get_monitors():
            self.setMaximumWidth(m.width)
            self.setMaximumHeight(m.height)

        # Variables for Playing, pausing and stopping
        self.break_value = False
        self.pause_loop = False

        # Run AI software
        self.ui.runBtn.clicked.connect(lambda: self.human_detection())

        # Checks what page of heatmap it is
        self.timer_heatmap = QTimer()
        self.timer_heatmap.timeout.connect(lambda: self.heatmap_page())
        self.timer_heatmap.setInterval(250)
        self.ui.dataBtn.clicked.connect(lambda: self.timer_heatmap_page())

        # Using camera as source
        self.ui.cameraBtn.clicked.connect(lambda: self.camera_source())

        # This avoids the bug where software is keep on running after exiting
        self.ui.closeBtn.clicked.connect(lambda: self.proper_exit())

        # Login page start
        self.ui.mainContentsWidget.setCurrentIndex(0)  # Set this to 0 for login page

        # Disables a lot of buttons for login page
        self.ui.menuBtn.setDisabled(True)
        self.ui.homeBtn.setDisabled(True)
        self.ui.dataBtn.setDisabled(True)
        self.ui.openBtn.setDisabled(True)
        self.ui.settingsBtn.setDisabled(True)
        self.ui.runBtn.setDisabled(True)
        self.ui.reloadBtn.setDisabled(True)
        self.ui.cameraBtn.setDisabled(True)
        self.ui.stopBtn.setDisabled(True)

        self.ui.invalidText.setVisible(False)
        self.ui.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.loginBtn.clicked.connect(lambda: self.login())

        self.DataTransfer = DataTransfer()
        self.Saving = Saving.Saving(self)

        # For AI Detection
        self.video_state = False
        self.thread_2 = QThread()
        self.AI = Detection.Detection(self, **vars(opt))
        self.AI.moveToThread(self.thread_2)
        self.thread_2.started.connect(lambda: self.AI.run(self, self.video_state))
        self.AI.finished.connect(lambda: self.thread_2.quit())
        self.AI.finished.connect(lambda: self.breaking_function())
        self.AI.progress.connect(lambda: self.data_transfer())

        # For heatmap
        self.thread_1 = QThread()
        self.Heatmap = Heatmap.Heatmap(object_main=self, multithreading=True)
        self.Heatmap.moveToThread(self.thread_1)
        self.thread_1.started.connect(lambda: self.Heatmap.matrix_to_image())

        self.fps = 0

    def data_transfer(self):
        self.Saving.json_results(self.DataTransfer.im0s, self.DataTransfer.det, self.DataTransfer.save_dir,
                                 self.DataTransfer.p, self, self.DataTransfer.video_state,
                                 self.DataTransfer.webcam, self.DataTransfer.frame)

    # This just for proof of concept for data privacy still looks cool though
    def login(self):
        if self.ui.usernameInput.text() == "Thermografi" and self.ui.passwordInput.text() == "123456":
            # Enables all the buttons
            self.ui.menuBtn.setDisabled(False)
            self.ui.homeBtn.setDisabled(False)
            self.ui.dataBtn.setDisabled(False)
            self.ui.openBtn.setDisabled(False)
            self.ui.settingsBtn.setDisabled(False)
            self.ui.runBtn.setDisabled(False)
            self.ui.reloadBtn.setDisabled(False)
            self.ui.cameraBtn.setDisabled(False)
            self.ui.stopBtn.setDisabled(False)

            # Goes to main page
            self.ui.mainContentsWidget.setCurrentIndex(1)
        else:
            self.ui.invalidText.setVisible(True)

    def human_detection(self):
        self.ui.humanIcon.setIcon((QIcon("icons/human - white.svg")))
        self.ui.warningIcon.setIcon(QIcon(""))
        self.Saving.__init__(self)

        if self.thread_1.isRunning():
            self.thread_1.quit()
            self.DataTransfer.__init__()
            self.Heatmap.reset_value()

        IMG_FORMAT = 'bmp', 'dng', 'jpeg', 'jpg', 'mpo', 'png', 'tif', 'tiff', 'webp'
        VID_FORMAT = 'asf', 'avi', 'gif', 'm4v', 'mkv', 'mov', 'mp4', 'mpeg', 'mpg', 'ts', 'wmv'

        if self.fname != ('', ''):
            self.DataTransfer.__init__()                                    # Resets values of Data Transfer
            self.AI.source = self.fname[0]
            self.AI.iou_thres = self.ui.overlapSlider.value() / 100
            self.AI.conf_thres = self.ui.confidenceSlider.value() / 100
            self.AI.hide_labels = self.ui.labelsCheckBox.isChecked()
            self.AI.hide_conf = self.ui.confidenceCheckBox.isChecked()
            self.AI.line_thickness = self.ui.lineSpinBox.value()
            self.AI.classes = 0

            is_file = Path(self.AI.source).suffix[1:] in (IMG_FORMAT + VID_FORMAT)
            is_url = self.AI.source.lower().startswith(('rtsp://', 'rtmp://', 'http://', 'https://'))
            webcam = self.AI.source.isnumeric() or self.AI.source.endswith('.txt') or (is_url and not is_file)

            self.video_state = False
            if self.AI.source.endswith(VID_FORMAT) or webcam:
                self.ui.cameraBtn.setDisabled(True)
                self.ui.cameraBtn.setIcon(QIcon("icons/camera - gray.svg"))
                self.ui.runBtn.setDisabled(True)
                self.ui.runBtn.setIcon(QIcon("icons/play-circle - gray.svg"))

                if self.AI.source.endswith(VID_FORMAT):
                    self.initializing_video_slider(self.AI.source)
                    self.video_state = True

            self.ui.humanCounter.setText(str(0))

            # Start AI Detection Multithreading
            self.thread_2.start()

            # Buttons that will pause and play the AI detection process
            self.ui.pauseBtn.clicked.connect(lambda: self.pause_function())
            self.ui.playBtn.clicked.connect(lambda: self.play_function())

            # Buttons that will stop the AI detection process
            self.ui.stopBtn.clicked.connect(lambda: self.breaking_function())
            self.ui.openBtn.clicked.connect(lambda: self.breaking_function())
            self.ui.closeBtn.clicked.connect(lambda: self.breaking_function())

    def breaking_function(self):
        self.break_value = True
        self.ui.runBtn.setDisabled(False)
        self.ui.cameraBtn.setIcon(QIcon("icons/camera - white.svg"))
        self.ui.cameraBtn.setDisabled(False)
        self.ui.runBtn.setIcon(QIcon("icons/play-circle - white.svg"))

    def pause_function(self):
        self.pause_loop = True

    def play_function(self):
        self.pause_loop = False

    def get_file(self):
        self.ui.outputImage.setPixmap(QPixmap(""))
        self.fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\')
        self.ui.openBtn.setStyleSheet("background-color: #16191d;")

    def timer_heatmap_page(self):
        if not self.timer_heatmap.isActive():
            self.timer_heatmap.start()

    def heatmap_page(self):
        self.ui.heatmapWidget.setCurrentIndex(self.ui.heatmapCombo.currentIndex())

        if self.ui.mainContentsWidget.currentIndex() == 0:
            self.timer_heatmap.stop()

    def camera_source(self):
        # This is to avoid any crashes
        self.ui.stopBtn.setDisabled(True)
        self.ui.pauseBtn.setDisabled(True)
        self.ui.playBtn.setDisabled(True)
        self.ui.openBtn.setDisabled(True)
        self.ui.runBtn.setDisabled(True)
        self.ui.cameraBtn.setDisabled(True)
        self.ui.videoSlider.setValue(0)

        if self.thread_1.isRunning():
            self.thread_1.quit()
            self.DataTransfer.__init__()
            self.Heatmap.reset_value()

        self.ui.totalTime.setText("0:00:00")

        # This is for the camera itself
        self.fname = ['0']
        self.human_detection()

    def proper_exit(self):
        QCoreApplication.exit(0)
        exit()

    def frame_to_seconds(self, duration):
        hrs = str(math.floor(duration / 3600))
        mins = ''
        if (math.floor(duration / 60)) > 9:
            mins = str(math.floor(duration / 60))
        else:
            mins = '0' + str(math.floor(duration / 60))

        secs = ''
        if (duration % 60) > 10:
            secs = str(int(duration % 60))
        else:
            secs = '0' + str(int(duration % 60))

        return secs, mins, hrs

    def change_time(self, value):
        secs, mins, hrs = self.frame_to_seconds(value/self.fps)
        current_text = hrs + ':' + mins + ':' + secs
        return current_text

    def change_text_time(self, value, object_text):
        if self.DataTransfer.webcam and (object_text == self.ui.endHeatmap or object_text == self.ui.currentHeatmap):
            object_text.setText(self.change_time(int(value * self.DataTransfer.average_ms)))
        else:
            object_text.setText(self.change_time(value))

    def initializing_video_slider(self, source):
        self.fps = cv2.VideoCapture(source).get(cv2.CAP_PROP_FPS)
        total_frame = cv2.VideoCapture(source).get(cv2.CAP_PROP_FRAME_COUNT)

        # set max value for videoSlider
        self.ui.videoSlider.setValue(0)
        self.ui.videoSlider.setMaximum(total_frame)
        self.ui.videoSlider.valueChanged.connect(lambda: self.change_text_time(self.ui.videoSlider.value(),
                                                                               self.ui.currentTime))

        duration = total_frame/self.fps
        secs, mins, hrs = self.frame_to_seconds(duration)

        total_text = hrs + ':' + mins + ':' + secs
        self.ui.totalTime.setText(total_text)

        # This is for the Heatmap Sliders for Video only not webcam or image
        self.ui.heatmapEndSlider.setValue(1)
        self.ui.heatmapEndSlider.setMaximum(total_frame)
        self.ui.heatmapEndSlider.setMinimum(1)
        self.ui.heatmapStartSlider.setValue(1)
        self.ui.heatmapStartSlider.setMaximum(total_frame)
        self.ui.heatmapStartSlider.setMinimum(1)

    def heatmap_function(self):
        self.thread_1.start()


class DataTransfer:
    def __init__(self):
        self.im0s = ''
        self.det = ''
        self.save_dir = ''
        self.p = ''
        self.video_state = ''
        self.webcam = ''
        self.frame = ''
        self.camera_fps = ''
        self.camera_frame = ''
        self.frame_data = []
        self.prev_frame = 0
        self.average_ms = 1
        self.display = ''
        self.output = ''
        self.once = False

    def detection_data(self, im0s, det, save_dir, p, video_state, webcam, frame):
        self.im0s = im0s
        self.det = det
        self.save_dir = save_dir
        self.p = p
        self.video_state = video_state
        self.webcam = webcam
        self.frame = frame

    def dataset_data(self, camera_fps=30, camera_frame=1):
        self.camera_fps = camera_fps
        self.camera_frame = camera_frame

    def camera_overall_heatmap(self, prev_frame, frame_data):
        self.prev_frame = prev_frame
        self.frame_data.append(frame_data)

    def camera_heatmap(self, average_ms):
        self.average_ms = average_ms

    def heatmap_dataset(self, display):
        self.display = display

    def heatmap_zeros(self, output, once):
        self.output = output
        self.once = once


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='YoloV5m/crowdhuman_vbody_yolov5m.pt',
                        help='model path(s)')
    parser.add_argument('--source', type=str, default='YoloV5m/data/images', help='file/dir/URL/glob, 0 for webcam')
    parser.add_argument('--data', type=str, default='YoloV5m/data/coco128.yaml', help='(optional) dataset.yaml path')
    parser.add_argument('--imgsz', '--img', '--img-size', nargs='+', type=int, default=(640, 640),
                        help='inference size h,w')
    parser.add_argument('--conf-thres', type=float, default=0.25, help='confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='NMS IoU threshold')
    parser.add_argument('--max-det', type=int, default=1000, help='maximum detections per image')
    parser.add_argument('--device', default='cpu', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', default=True, action='store_true', help='show results')
    parser.add_argument('--save-txt', default=False, action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', default=False, action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--save-crop', default=False, action='store_true', help='save cropped prediction boxes')
    parser.add_argument('--nosave', default=True, action='store_true', help='do not save images/videos')
    parser.add_argument('--classes', default=0, nargs='+', type=int,
                        help='filter by class: --classes 0, or --classes 0 2 3')
    parser.add_argument('--agnostic-nms', default=True, action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', default=False, action='store_true', help='augmented inference')
    parser.add_argument('--visualize', default=False, action='store_true', help='visualize features')
    parser.add_argument('--update', default=False, action='store_true', help='update all models')
    parser.add_argument('--project', default='YoloV5m/runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', default=True, action='store_true',
                        help='existing project/name ok, do not increment')
    parser.add_argument('--line-thickness', default=3, type=int, help='bounding box thickness (pixels)')
    parser.add_argument('--hide-labels', default=False, action='store_true', help='hide labels')
    parser.add_argument('--hide-conf', default=False, action='store_true', help='hide confidences')
    parser.add_argument('--half', default=False, action='store_true', help='use FP16 half-precision inference')
    parser.add_argument('--dnn', default=False, action='store_true', help='use OpenCV DNN for ONNX inference')
    opt = parser.parse_args()
    opt.imgsz *= 2 if len(opt.imgsz) == 1 else 1  # expand

    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())

# This is for ui_interface.py just put it at the end and replace QSlider with Slider for videoSlider
"""
class Slider(QSlider):
    change_event = False
    intersect_event = False

    def mousePressEvent(self, event):
        super(Slider, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            val = self.pixelPosToRangeValue(event.pos())
            self.setValue(val)
        self.change(True)

    def pixelPosToRangeValue(self, pos):
        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        gr = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderGroove, self)
        sr = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderHandle, self)

        if self.orientation() == Qt.Horizontal:
            sliderLength = sr.width()
            sliderMin = gr.x()
            sliderMax = gr.right() - sliderLength + 1
        else:
            sliderLength = sr.height()
            sliderMin = gr.y()
            sliderMax = gr.bottom() - sliderLength + 1;
        pr = pos - sr.center() + sr.topLeft()
        p = pr.x() if self.orientation() == Qt.Horizontal else pr.y()
        self.intersect_event = True
        return QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), p - sliderMin,
                                              sliderMax - sliderMin, opt.upsideDown)

    def change(self, state):
        self.change_event = state

    def change_event_return(self):
        return self.change_event
"""
