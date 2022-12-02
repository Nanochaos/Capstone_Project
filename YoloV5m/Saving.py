from numpy import zeros
from json import dumps
from base64 import b64encode
from zlib import compress
from YoloV5m import Heatmap

from os import mkdir, path
from astropy.convolution import convolve, Ring2DKernel
import cv2
from astropy.convolution.kernels import Gaussian2DKernel


class Saving:
    def __init__(self, object_main):
        self.once_event = False
        self.HP = Heatmap.Heatmap(multithreading=False, object_main=object_main)

    def json_results(self, im0s, det, save_dir, p, object_main, video_state, webcam, frame):
        matrix_data = {}
        # Save detections in matrix format
        m = zeros(im0s.shape[:2])

        for e in det[:, :4]:
            x1, y1, x2, y2 = e
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            mid_x, mid_y = int(x1+((x2-x1)/2)), int(y1+((y2-y1)/2))
            # print("x1: %s, x2: %s, y1: %s, y2: %s, mid_x: %s, mid_y: %s" % (x1, x2, y1, y2, mid_x, mid_y))
            if (x2-x1) < (y2-y1):
                y1 = mid_y - int((x2-x1)/2)
                y2 = mid_y + int((x2-x1)/2)
                ring_m = Ring2DKernel(0, x2 - x1)
            else:
                x1 = mid_x - int((y2 - y1)/2)
                x2 = mid_x + int((y2 - y1)/2)
                ring_m = Ring2DKernel(0, y2 - y1)
            # print("new x1: %s, new x2: %s, new y1: %s, new y2: %s" % (x1, x2, y1, y2))

            ring_m = ring_m.array
            i = 0
            while i < len(ring_m):
                j = 0
                while j < len(ring_m[0]):
                    if ring_m[i][j] != 0:
                        ring_m[i][j] = 1
                    j += 1
                i += 1

            m[y1:y2, x1:x2] = cv2.resize(ring_m, (x2-x1, y2-y1))


        std = 3

        m = convolve(m, Gaussian2DKernel(x_stddev=std, y_stddev=std, mode='center'))

        mkdir(save_dir / 'results') if not path.exists(save_dir / 'results') else None
        if not self.once_event:
            with open(save_dir / 'results' / f'{p.stem}.compressed', 'w') as f:
                f.write('')
            self.once_event = True

        matrix_data = dumps({'frame': frame, 'data': {'detections': len(det),
                                                      'matrix': b64encode(
                                                          compress(
                                                              dumps(m.tolist()).encode('utf-8')
                                                          )
                                                      ).decode('ascii')}})

        # save to compressed numpy file
        with open(save_dir / 'results' / f'{p.stem}.compressed', 'a') as f:
            f.write(f'{str(matrix_data)}\n')

        self.HP.source = "YoloV5m/runs/detect/exp/results/%s.compressed" % p.stem
        self.HP.webcam = webcam
        self.HP.matrix_to_image(start=frame, end=frame)

        if not object_main.thread_1.isRunning() and (webcam or video_state):
            object_main.Heatmap.source = "YoloV5m/runs/detect/exp/results/%s.compressed" % p.stem
            object_main.Heatmap.webcam = webcam

            if webcam:
                object_main.ui.heatmapStartSlider.setMinimum(1)
                object_main.ui.heatmapEndSlider.setMinimum(1)
                object_main.ui.heatmapStartSlider.setValue(1)
                object_main.ui.heatmapEndSlider.setValue(1)

            object_main.heatmap_function()

