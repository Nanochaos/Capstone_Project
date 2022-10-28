from pathlib import Path
import os
import sys

import torch
import torch.backends.cudnn as cudnn

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from models.common import DetectMultiBackend
from utils.datasets import IMG_FORMATS, VID_FORMATS, LoadImages, LoadStreams
from utils.general import (LOGGER, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, scale_coords, strip_optimizer, xyxy2xywh)
from utils.plots import Annotator, colors, save_one_box
from utils.torch_utils import select_device, time_sync

from PySide2.QtCore import Signal, QObject, Qt
from PySide2.QtGui import QImage, QPixmap, QIcon


@torch.no_grad()  # Reduce memory usage and speeds up computation by disabling gradient calculation
class Detection(QObject):
    # Used for sending and receiving data while multithreading
    progress = Signal()
    finished = Signal()

    def __init__(self, object_main, weights, source, data, imgsz, conf_thres, iou_thres, max_det, device, view_img,
                 save_txt, save_conf, save_crop, nosave, classes, agnostic_nms, augment, visualize, update, project,
                 name, exist_ok, line_thickness, hide_labels, hide_conf, half, dnn):
        super().__init__()
        check_requirements(exclude=('tensorboard', 'thop'))
        self.weights = weights                                  # model.pt path(s)
        self.source = source                                    # file/dir/URL/glob, 0 for webcam
        self.data = data                                        # dataset.yaml path
        self.imgsz = imgsz                                      # inference size (height, width)
        # Classifies an object depending on the confidence threshold
        self.conf_thres = conf_thres                            # confidence threshold
        # Threshold for removing overlapping bounding boxes
        self.iou_thres = iou_thres                              # NMS IOU threshold
        self.max_det = max_det                                  # maximum detections per image
        self.device = device                                    # cuda device, i.e. 0 or 0,1,2,3 or cpu
        self.view_img = view_img                                # show results
        self.save_txt = save_txt                                # save results to *.txt
        self.save_conf = save_conf                              # save confidences in --save-txt labels
        self.save_crop = save_crop                              # save cropped prediction boxes
        self.nosave = nosave                                    # do not save images/videos
        # Class 0 is head detections; Class 1 is visible body detections
        self.classes = classes                                  # filter by class: --class 0, or --class 0 2 3
        self.agnostic_nms = agnostic_nms                        # class-agnostic NMS
        self.augment = augment                                  # augmented inference
        self.visualize = visualize                              # visualize features
        self.update = update                                    # update all models
        self.project = project                                  # save results to project/name
        self.name = name                                        # save results to project/name
        self.exist_ok = exist_ok                                # existing project/name ok, do not increment
        self.line_thickness = line_thickness                    # bounding box thickness (pixels)
        self.hide_labels = hide_labels                          # hide labels
        self.hide_conf = hide_conf                              # hide confidences
        self.half = half                                        # use FP16 half-precision inference
        self.dnn = dnn                                          # use OpenCV DNN for ONNX inference

        # For displaying images
        self.im0 = ''
        self.Display = Output(object_main, self)
        self.camera_close = False

    def run(self, object_main, video_state):
        # For some reason break_value always becomes true after being clicked once so this is to break that bug
        object_main.break_value = False
        self.camera_close = False

        save_img = not self.nosave and not self.source.endswith('.txt')                                         # save inference LoadImages
        is_file = Path(self.source).suffix[1:] in (IMG_FORMATS + VID_FORMATS)
        is_url = self.source.lower().startswith(('rtsp://', 'rtmp://', 'http://', 'https://'))
        webcam = self.source.isnumeric() or self.source.endswith('.txt') or (is_url and not is_file)
        if is_url and is_file:
            self.source = check_file(self.source)                                                               # download

        # Directories
        save_dir = increment_path(Path(self.project) / self.name, exist_ok=self.exist_ok)                       # increment run
        if not self.nosave:
            (save_dir / 'labels' if self.save_txt else save_dir).mkdir(parents=True, exist_ok=True)             # make directory

        # Load model
        bad_GPU = ['NVIDIA GeForce GTX 1050 Ti', 'NVIDIA GeForce GTX 1050', 'GeForce GTX 1050 Ti', 'GeForce GTX 1050']
        try:
            try:
                if torch.cuda.is_available() and torch.cuda.get_device_name(0) not in bad_GPU:
                    print('CUDA 0')
                    self.device = '0'
                    self.device = select_device(self.device)
            except AssertionError:
                if torch.cuda.is_available() and torch.cuda.get_device_name(1) not in bad_GPU:
                    print('CUDA 1')
                    self.device = '1'
                    self.device = select_device(self.device)
        except AssertionError:
            print('CPU')
            self.device = 'cpu'

        self.device = select_device(self.device)

        model = DetectMultiBackend(self.weights, device=self.device, dnn=self.dnn, data=self.data, fp16=self.half)
        stride, names, pt = model.stride, model.names, model.pt
        self.imgsz = check_img_size(self.imgsz, s=stride)                                                       # check image size

        # Dataloader
        if webcam:
            self.view_img = check_imshow()
            cudnn.benchmark = True                                                                              # set True to speed up constant image size inference
            dataset = LoadStreams(self.source, img_size=self.imgsz, stride=stride, auto=pt, object_det=self,
                                  object_main=object_main)
            bs = len(dataset)                                                                                   # batch_size
        else:
            dataset = LoadImages(self.source, img_size=self.imgsz, stride=stride, auto=pt, object_main=object_main)
            bs = 1                                                                                              # batch_size

        # Run inference
        model.warmup(imgsz=(1 if pt else bs, 3, *self.imgsz))                                                   # warmup
        dt, seen = [0.0, 0.0, 0.0], 0

        for path, im, im0s, vid_cap, s in dataset:
            process_time = time_sync()
            t1 = time_sync()
            im = torch.from_numpy(im).to(self.device)
            im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
            im /= 255  # 0 - 255 to 0.0 - 1.0
            if len(im.shape) == 3:
                im = im[None]  # expand for batch dim
            t2 = time_sync()
            dt[0] += t2 - t1

            # Inference
            self.visualize = increment_path(save_dir / Path(path).stem, mkdir=True) if self.visualize else False
            pred = model(im, augment=self.augment, visualize=self.visualize)
            t3 = time_sync()
            dt[1] += t3 - t2

            # NMS
            pred = non_max_suppression(pred, self.conf_thres, self.iou_thres, self.classes, self.agnostic_nms,
                                       max_det=self.max_det)
            dt[2] += time_sync() - t3

            # Second-stage classifier (optional)
            # pred = utils.general.apply_classifier(pred, classifier_model, im, im0s)

            # Process predictions
            for i, det in enumerate(pred):                                                                      # per image
                seen += 1
                if webcam:                                                                                      # batch_size >= 1
                    p, im0, frame = path[i], im0s[i].copy(), dataset.count
                    s += f'{i}: '
                else:
                    p, im0, frame = path, im0s.copy(), getattr(dataset, 'frame', 0)

                p = Path(p)                                                                                     # to Path
                save_path = str(save_dir / ("dummy" + ".jpeg"))                                                 # im.jpg
                txt_path = str(save_dir / 'labels' / p.stem) + ('' if dataset.mode == 'image' else f'_{frame}') # im.txt
                s += '%gx%g ' % im.shape[2:]                                                                    # print string
                gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]                                                      # normalization gain whwh
                imc = im0.copy() if self.save_crop else im0                                                     # for save_crop
                annotator = Annotator(im0, line_width=self.line_thickness, example=str(names))

                if len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_coords(im.shape[2:], det[:, :4], im0.shape).round()

                    # Print results
                    for c in det[:, -1].unique():
                        n = (det[:, -1] == c).sum()                                                             # detections per class
                        s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "                                            # add to string

                    # Write results
                    for *xyxy, conf, cls in reversed(det):
                        if self.save_txt:                                                                       # Write to file
                            xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()            # normalized xywh
                            line = (cls, *xywh, conf) if self.save_conf else (cls, *xywh)                       # label format
                            with open(txt_path + '.txt', 'a') as f:
                                f.write(('%g ' * len(line)).rstrip() % line + '\n')

                        if save_img or self.save_crop or self.view_img:                                         # Add bbox to image
                            c = int(cls)                                                                        # integer class
                            label = None if self.hide_labels else (names[c] if self.hide_conf else f'{names[c]} {conf:.2f}')
                            annotator.box_label(xyxy, label, color=colors(c, True))
                            if self.save_crop:
                                save_one_box(xyxy, imc, file=save_dir / 'crops' / names[c] / f'{p.stem}.jpg', BGR=True)

            # Save results (image with detections)
            if save_img:
                cv2.imwrite(save_path, im0)

            # Stream results
            im0 = annotator.result()

            # For converting AI detection results and converting to AI heatmap
            if not video_state and not webcam:
                object_main.DataTransfer.detection_data(im0s, det, save_dir, p, video_state, webcam, int(frame + 1))
            else:
                if webcam:
                    object_main.DataTransfer.detection_data(im0s[0], det, save_dir, p, video_state, webcam,
                                                            int(frame + 1))
                    object_main.ui.heatmapStartSlider.setMaximum(int(frame + 1))
                    object_main.ui.heatmapEndSlider.setMaximum(int(frame + 1))
                else:
                    object_main.DataTransfer.detection_data(im0s, det, save_dir, p, video_state, webcam, int(frame))

            self.progress.emit()

            # For displaying the bbox AI detection
            self.im0 = im0
            self.Display.change_output_image(object_main, im0, len(pred[0]), frame + 1, video_state, process_time)

            # Pause, play and stop functionality
            self.Display.update_player_value(object_main)
            while self.Display.pause_loop:
                self.Display.update_player_value(object_main)
                cv2.waitKey(2)
                if self.Display.break_value:
                    object_main.pause_loop = False
                    self.camera_close = True
                    self.results(seen, dt, save_img, save_dir)
                    self.finished.emit()
                    return

            if self.Display.break_value:
                if object_main.fname[0] != self.source:
                    object_main.ui.outputImage.setPixmap(QPixmap(""))
                self.camera_close = True
                break

        self.results(seen, dt, save_img, save_dir)
        self.finished.emit()

    def results(self, seen, dt, save_img, save_dir):
        # Print results
        t = tuple(x / seen * 1E3 for x in dt)                                                                   # speeds per image
        LOGGER.info(f'Speed: %.1fms pre-process, %.1fms inference, %.1fms NMS per image at shape {(1, 3, *self.imgsz)}' % t)
        if self.save_txt or save_img:
            s = f"\n{len(list(save_dir.glob('labels/*.txt')))} labels saved to {save_dir / 'labels'}" if self.save_txt else ''
            LOGGER.info(f"Results saved to {colorstr('bold', save_dir)}{s}")
        if self.update:
            strip_optimizer(self.weights)                                                                       # update model (to fix SourceChangeWarning


class Output:
    def __init__(self, object_main, object_det):
        super().__init__()
        self.break_value = object_main.break_value
        self.pause_loop = object_main.pause_loop
        self.object_det = object_det
        self.local_image = ('', '')
        object_main.ui.reloadBtn.clicked.connect(lambda: self.reload_display_image_event(object_main, self.object_det))
        self.once = False

    def video_delay(self, process_time):
        if not self.once:
            video_fps = cv2.VideoCapture(self.object_det.source).get(cv2.CAP_PROP_FPS)
        fps_time = (1000 / video_fps) / 100
        t1 = time_sync()
        t_process = t1 - process_time

        # print("total: %f" % t_process)
        # print("fps_time: %f" % fps_time)
        # print("fps-total: %f" % (fps_time - t_process))
        if t_process < fps_time:
            cv2.waitKey((fps_time-t_process)*100)
            """
            while True:
                t2 = time_sync()
                if((t2 - t1) + t_process) >= fps_time:
                    break
            # print("time_sync: %f" % (t2 - t1))
            """

    def change_output_image(self, object_main, im0, human_count, frame, video_state, process_time):
        cv2.cvtColor(im0, cv2.COLOR_BGR2RGB, im0)
        self.local_image = QImage(im0.data, im0.shape[1], im0.shape[0], im0.shape[1] * im0.shape[2],
                                  QImage.Format_RGB888)

        if video_state and not object_main.ui.cudaCheckBox.isChecked():
            self.video_delay(process_time)

        # Displays the cv2 image to the GUI
        self.display_image_event(object_main)

        # Displays the amount of humans counted
        if object_main.ui.mainContentsWidget.currentIndex() == 1 or object_main.ui.heatmapWidget.currentIndex() == 0:
            object_main.ui.humanCounter.setText(str(human_count))

        # re-enabling the buttons
        object_main.ui.stopBtn.setDisabled(False)
        object_main.ui.pauseBtn.setDisabled(False)
        object_main.ui.playBtn.setDisabled(False)
        object_main.ui.openBtn.setDisabled(False)
        object_main.ui.runBtn.setDisabled(False)
        object_main.ui.cameraBtn.setDisabled(False)

        if object_main.ui.maxDetectionsCheckBox.isChecked():
            try:
                if human_count > int(object_main.ui.maxDetectionsInput.text()):
                    object_main.ui.humanIcon.setIcon(QIcon("icons/human - red.svg"))
                    object_main.ui.warningIcon.setIcon(QIcon("icons/warning - red.svg"))
                elif human_count == int(object_main.ui.maxDetectionsInput.text()):
                    object_main.ui.humanIcon.setIcon(QIcon("icons/human - white.svg"))
                    object_main.ui.warningIcon.setIcon(QIcon("icons/warning - orange.svg"))
                else:
                    object_main.ui.humanIcon.setIcon(QIcon("icons/human - white.svg"))
                    object_main.ui.warningIcon.setIcon(QIcon(""))
            except:
                if human_count > 20:
                    object_main.ui.humanIcon.setIcon(QIcon("icons/human - red.svg"))
                    object_main.ui.warningIcon.setIcon(QIcon("icons/warning - red.svg"))
                elif human_count == 20:
                    object_main.ui.humanIcon.setIcon(QIcon("icons/human - white.svg"))
                    object_main.ui.warningIcon.setIcon(QIcon("icons/warning - orange.svg"))
                else:
                    object_main.ui.humanIcon.setIcon(QIcon("icons/human - white.svg"))
                    object_main.ui.warningIcon.setIcon(QIcon(""))

        # Current time of video slider code
        if video_state and not object_main.ui.videoSlider.change_event_return():
            object_main.ui.videoSlider.setValue(frame)

    def display_image_event(self, object_main):
        if self.local_image == '':
            return
        object_main.ui.outputImage.setPixmap(QPixmap.fromImage(self.local_image.scaled(
            object_main.ui.outputImage.size(), Qt.KeepAspectRatio)))

    def reload_display_image_event(self, object_main, object_det):
        cv2.waitKey(1)
        self.local_image = QImage(object_det.im0.data, object_det.im0.shape[1], object_det.im0.shape[0],
                                  object_det.im0.shape[1] * object_det.im0.shape[2], QImage.Format_RGB888)
        self.display_image_event(object_main)

    def update_player_value(self, object_main):
        self.break_value = object_main.break_value
        self.pause_loop = object_main.pause_loop
