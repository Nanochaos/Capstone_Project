from numpy import zeros
from json import dumps
from base64 import b64encode
from zlib import compress
from YoloV5m import Heatmap

from os import mkdir, path, remove


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
            m[y1:y2, x1:x2] += 1

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

