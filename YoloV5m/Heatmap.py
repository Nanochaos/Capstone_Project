import sys

from PySide2.QtCore import QObject, Qt, QTimer
from json import loads
from zlib import decompress
from base64 import b64decode
from numpy import zeros, array, uint8, asarray
import cv2
from numpy import sum
from PySide2.QtGui import QImage, QPixmap, QIcon


class Heatmap(QObject):
    def __init__(self, source='', object_main=None, webcam=False, multithreading=False):
        super().__init__()
        self.object_main = object_main
        self.source = source
        self.im0s = self.object_main.DataTransfer.im0s
        self.webcam = webcam
        self.object_main_display = None
        self.multithreading = multithreading
        self.timer = QTimer()
        self.data = {}

        self.object_main.ui.reloadBtn.clicked.connect(lambda: self.reload_display_heatmap(
            self.object_main.DataTransfer.display))

        color_map_raw = [[113, 0, 0], [114, 0, 0], [115, 0, 0], [116, 0, 0], [117, 0, 0], [118, 0, 0], [119, 0, 0],
                         [120, 0, 0], [121, 0, 0], [122, 0, 0], [123, 0, 0], [123, 0, 0], [124, 0, 0], [125, 0, 0],
                         [126, 0, 0], [127, 0, 0], [128, 0, 0], [129, 0, 0], [130, 0, 0], [131, 0, 0], [132, 0, 0],
                         [133, 0, 0], [134, 0, 0], [135, 0, 0], [136, 0, 0], [137, 0, 0], [138, 0, 0], [139, 0, 0],
                         [140, 0, 0], [141, 0, 0], [142, 0, 0], [143, 0, 0], [144, 0, 0], [145, 0, 0], [146, 0, 0],
                         [147, 0, 0], [148, 0, 0], [149, 0, 0], [150, 0, 0], [151, 0, 0], [152, 0, 0], [153, 0, 0],
                         [154, 0, 0], [155, 0, 0], [155, 0, 0], [156, 0, 0], [157, 0, 0], [158, 0, 0], [159, 0, 0],
                         [160, 0, 0], [161, 0, 0], [162, 0, 0], [163, 0, 0], [164, 0, 0], [165, 0, 0], [166, 0, 0],
                         [167, 0, 0], [168, 0, 0], [169, 0, 0], [170, 0, 0], [171, 0, 0], [172, 0, 0], [173, 0, 0],
                         [174, 0, 0], [175, 0, 0], [176, 2, 0], [177, 4, 0], [179, 6, 0], [180, 8, 0], [181, 10, 0],
                         [183, 12, 0], [184, 14, 0], [185, 16, 0], [186, 18, 0], [188, 20, 0], [189, 22, 0],
                         [190, 24, 0], [191, 26, 0], [193, 28, 0], [194, 30, 0], [195, 32, 0], [196, 33, 0],
                         [198, 35, 0], [199, 37, 0], [200, 39, 0], [201, 41, 0], [203, 43, 0], [204, 45, 0],
                         [205, 47, 0], [206, 49, 0], [208, 51, 0], [209, 53, 0], [210, 55, 0], [212, 57, 0],
                         [213, 59, 0], [214, 61, 0], [215, 63, 0], [217, 64, 0], [218, 66, 0], [219, 68, 0],
                         [220, 70, 0], [222, 72, 0], [223, 74, 0], [224, 76, 0], [225, 78, 0], [227, 80, 0],
                         [228, 82, 0], [229, 84, 0], [230, 86, 0], [232, 88, 0], [233, 90, 0], [234, 92, 0],
                         [235, 94, 0], [237, 96, 0], [238, 97, 0], [239, 99, 0], [241, 101, 0], [242, 103, 0],
                         [243, 105, 0], [244, 107, 0], [246, 109, 0], [247, 111, 0], [248, 113, 0], [249, 115, 0],
                         [251, 117, 0], [252, 119, 0], [253, 121, 0], [254, 123, 0], [255, 125, 1], [255, 127, 3],
                         [255, 129, 5], [255, 131, 7], [255, 133, 9], [255, 135, 11], [255, 137, 13], [255, 139, 15],
                         [255, 141, 16], [255, 143, 18], [255, 145, 20], [255, 147, 22], [255, 149, 24], [255, 151, 26],
                         [255, 154, 28], [255, 156, 30], [255, 158, 32], [255, 160, 34], [255, 162, 36], [255, 164, 38],
                         [255, 166, 40], [255, 168, 42], [255, 170, 44], [255, 172, 46], [255, 174, 48], [255, 176, 49],
                         [255, 178, 51], [255, 180, 53], [255, 182, 55], [255, 184, 57], [255, 186, 59], [255, 189, 61],
                         [255, 191, 63], [255, 193, 65], [255, 195, 67], [255, 197, 69], [255, 199, 71], [255, 201, 73],
                         [255, 203, 75], [255, 205, 77], [255, 207, 79], [255, 209, 80], [255, 211, 82], [255, 213, 84],
                         [255, 215, 86], [255, 217, 88], [255, 219, 90], [255, 222, 92], [255, 224, 94], [255, 226, 96],
                         [255, 228, 98], [255, 230, 100], [255, 232, 102], [255, 234, 104], [255, 236, 106],
                         [255, 238, 108], [255, 240, 110], [255, 242, 112], [255, 244, 113], [255, 246, 115],
                         [255, 248, 117], [255, 250, 119], [255, 252, 121], [255, 254, 123], [255, 255, 125],
                         [255, 255, 127], [255, 255, 129], [255, 255, 131], [255, 255, 133], [255, 255, 135],
                         [255, 255, 138], [255, 255, 140], [255, 255, 142], [255, 255, 144], [255, 255, 146],
                         [255, 255, 148], [255, 255, 150], [255, 255, 152], [255, 255, 154], [255, 255, 156],
                         [255, 255, 158], [255, 255, 160], [255, 255, 162], [255, 255, 164], [255, 255, 166],
                         [255, 255, 168], [255, 255, 171], [255, 255, 173], [255, 255, 175], [255, 255, 177],
                         [255, 255, 179], [255, 255, 181], [255, 255, 183], [255, 255, 185], [255, 255, 187],
                         [255, 255, 189], [255, 255, 191], [255, 255, 193], [255, 255, 195], [255, 255, 197],
                         [255, 255, 199], [255, 255, 201], [255, 255, 203], [255, 255, 206], [255, 255, 208],
                         [255, 255, 210], [255, 255, 212], [255, 255, 214], [255, 255, 216], [255, 255, 218],
                         [255, 255, 220], [255, 255, 222], [255, 255, 224], [255, 255, 226], [255, 255, 228],
                         [255, 255, 230], [255, 255, 232], [255, 255, 234], [255, 255, 236], [255, 255, 239],
                         [255, 255, 241], [255, 255, 243], [255, 255, 245], [255, 255, 247], [255, 255, 249],
                         [255, 255, 251], [255, 255, 253], [144, 152, 148]]
        self.color_map_cv2 = asarray(color_map_raw[::-1]).reshape((256, 1, 3))

    def reset_value(self):
        self.source = ''
        self.im0s = self.object_main.DataTransfer.im0s
        self.webcam = False
        self.object_main_display = None

        self.timer = QTimer()
        self.data = {}

    def heatmap_slider_mechanics(self, first):
        start_value = self.object_main.ui.heatmapStartSlider.value()
        end_value = self.object_main.ui.heatmapEndSlider.value()

        if start_value > end_value and (self.object_main.ui.heatmapEndSlider.intersect_event or
                                        self.object_main.ui.heatmapStartSlider.intersect_event):
            self.object_main.ui.heatmapEndSlider.intersect_event = False
            self.object_main.ui.heatmapStartSlider.intersect_event = False

            if first:
                end_value = start_value
                self.object_main.ui.heatmapEndSlider.setValue(end_value)
            else:
                start_value = end_value
                self.object_main.ui.heatmapStartSlider.setValue(start_value)

    def matrix_addition(self, start, end):
        if not self.multithreading:
            self.data = {}
            self.object_main.ui.overallHeatmapOutput.setPixmap(QPixmap(""))

        with open(self.source) as f:
            x = f.readlines()[(start - 1): end]
            for i, data_arr in enumerate(x):
                temp = loads(data_arr)
                try:
                    if self.data[start + i]['frame'] == temp['frame']:  # if self.data[start + i] == temp:
                        continue
                    else:
                        self.data[temp['frame']] = temp  # Applicable for both decoded and non-decoded self.data var
                        self.data[temp['frame']]['data']['matrix'] = \
                            loads(decompress(b64decode(self.data[temp['frame']]['data']['matrix'])))  # Applicable only for decoded self.data var

                except KeyError:
                    self.data[temp['frame']] = temp  # Applicable for both decoded and non-decoded self.data var
                    self.data[temp['frame']]['data']['matrix'] = \
                        loads(decompress(b64decode(self.data[temp['frame']]['data']['matrix'])))  # Applicable only for decoded self.data var
        if not self.object_main.DataTransfer.once:
            output = zeros(array(self.data[1]['data']['matrix']).shape)  # Applicable only for decoded self.data var
            self.object_main.DataTransfer.heatmap_zeros(output, True)
        else:
            output = zeros(array(self.object_main.DataTransfer.output).shape)

        # output = zeros(array(self.object_main.DataTransfer.output).shape)
        text_status = "Overall Heatmap"
        human_count = 0
        for i in range(start, end + 1):
            try:
                output += self.data[i]['data']['matrix']  # Applicable only for decoded self.data var
                # output += loads(decompress(b64decode(self.data[i]['data']['matrix'])))
                if self.data[i]['data']['detections'] > human_count:
                    human_count = self.data[i]['data']['detections']
            except KeyError:
                text_status = "Overall Heatmap - Incomplete Data"

        if self.object_main.ui.maxDetectionsCheckBox.isChecked():
            try:
                if human_count > int(self.object_main.ui.maxDetectionsInput.text()):
                    self.object_main.ui.humanIcon.setIcon(QIcon("icons/human - red.svg"))
                    self.object_main.ui.warningIcon.setIcon(QIcon("icons/warning - red.svg"))
                elif human_count == int(self.object_main.ui.maxDetectionsInput.text()):
                    self.object_main.ui.humanIcon.setIcon(QIcon("icons/human - white.svg"))
                    self.object_main.ui.warningIcon.setIcon(QIcon("icons/warning - orange.svg"))
                else:
                    self.object_main.ui.humanIcon.setIcon(QIcon("icons/human - white.svg"))
                    self.object_main.ui.warningIcon.setIcon(QIcon(""))
            except:
                if human_count > 20:
                    self.object_main.ui.humanIcon.setIcon(QIcon("icons/human - red.svg"))
                    self.object_main.ui.warningIcon.setIcon(QIcon("icons/warning - red.svg"))
                elif human_count == 20:
                    self.object_main.ui.humanIcon.setIcon(QIcon("icons/human - white.svg"))
                    self.object_main.ui.warningIcon.setIcon(QIcon("icons/warning - orange.svg"))
                else:
                    self.object_main.ui.humanIcon.setIcon(QIcon("icons/human - white.svg"))
                    self.object_main.ui.warningIcon.setIcon(QIcon(""))

        if self.multithreading:
            self.object_main.ui.heatmapDesc_2.setText(text_status)
            if self.object_main.ui.mainContentsWidget.currentIndex() == 2 and \
                    self.object_main.ui.heatmapWidget.currentIndex() == 1:
                self.object_main.ui.humanCounter.setText(str(human_count))

        return output

    def matrix_to_image(self, start=1, end=1):
        if not self.multithreading:
            output = self.matrix_addition(start, end)
            self.object_main_display = self.object_main.ui.currentHeatmapOutput
            self.matrix_to_image_display(output)
        else:
            self.timer.start()
            self.timer.timeout.connect(lambda: self.threaded_matrix_to_image())
            self.timer.setInterval(1000)
            self.object_main.ui.heatmapStartSlider.valueChanged.connect(lambda: self.heatmap_slider_mechanics(True))
            self.object_main.ui.heatmapEndSlider.valueChanged.connect(lambda: self.heatmap_slider_mechanics(False))

            self.object_main.ui.heatmapStartSlider.valueChanged.connect(
                lambda: self.object_main.change_text_time(self.object_main.ui.heatmapStartSlider.value(),
                                                          self.object_main.ui.currentHeatmap))
            self.object_main.ui.heatmapEndSlider.valueChanged.connect(
                lambda: self.object_main.change_text_time(self.object_main.ui.heatmapEndSlider.value(),
                                                          self.object_main.ui.endHeatmap))

        if self.webcam:
            self.distance_camera_frames()

    def threaded_matrix_to_image(self):
        if self.webcam:
            output = self.matrix_addition(start=self.object_main.ui.heatmapStartSlider.value(),
                                          end=self.object_main.ui.heatmapEndSlider.value())
        else:
            output = self.matrix_addition(start=self.object_main.ui.heatmapStartSlider.value(),
                                          end=self.object_main.ui.heatmapEndSlider.value())

        self.object_main_display = self.object_main.ui.overallHeatmapOutput

        self.matrix_to_image_display(output)

    def matrix_to_image_display(self, output):
        self.im0s = self.object_main.DataTransfer.im0s

        display_hp = None
        display_hp = cv2.normalize(output, display_hp, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        display_hp = cv2.LUT(cv2.cvtColor(display_hp, cv2.COLOR_BGR2RGB), self.color_map_cv2).astype(uint8)
        display_image = cv2.addWeighted(display_hp, 0.3, cv2.cvtColor(self.im0s, cv2.COLOR_BGR2RGB), 0.7, 0.0)
        display = display_image

        if self.object_main.ui.overlapCheckBox.isChecked():
            qim = QImage(display.data, display.shape[1], display.shape[0], display.shape[1] * display.shape[2],
                         QImage.Format_RGB888)
            self.object_main.DataTransfer.display = display
        else:
            qim = QImage(display_hp.data, display_hp.shape[1], display_hp.shape[0],
                         display_hp.shape[1] * display_hp.shape[2], QImage.Format_RGB888)
            self.object_main.DataTransfer.display = display_hp

        self.display_heatmap(qim)

    def distance_camera_frames(self):
        if len(self.object_main.DataTransfer.frame_data) <= 30:
            diff_ms = self.object_main.DataTransfer.camera_frame - self.object_main.DataTransfer.prev_frame
            self.object_main.DataTransfer.camera_overall_heatmap(self.object_main.DataTransfer.camera_frame, diff_ms)
            average_ms = sum(self.object_main.DataTransfer.frame_data) / len(self.object_main.DataTransfer.frame_data)
            self.object_main.DataTransfer.camera_heatmap(average_ms)
        self.camera_time_change()

    def camera_time_change(self):
        self.object_main.fps = self.object_main.DataTransfer.camera_fps
        self.object_main.change_text_time(self.object_main.DataTransfer.camera_frame, self.object_main.ui.totalTime)

    def reload_display_heatmap(self, display):
        qim = QImage(display.data, display.shape[1], display.shape[0], display.shape[1] * display.shape[2],
                     QImage.Format_RGB888)
        self.display_heatmap(qim)

    def display_heatmap(self, qim):
        if self.object_main_display is not None:
            cv2.waitKey(1)
            self.object_main_display.setPixmap(QPixmap(qim.scaled(self.object_main_display.size(), Qt.KeepAspectRatio)))
