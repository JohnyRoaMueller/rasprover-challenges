# module to get onboard videos

import cv2
import threading
import queue

class FrameRecorder:
    def __init__(self, filename, frame_rate, resolution):
        self.filename = filename
        self.frame_rate = frame_rate
        self.frame_interval = 1 / frame_rate
        self.resolution = resolution
        self.queue = queue.Queue(maxsize=100)
        self.running = False
        self.writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'mp4v'),
                                      frame_rate, resolution)
        self.thread = threading.Thread(target=self._write_frames)

    def start(self):
        self.running = True
        self.thread.start()

    def push_frame(self, frame):
        """Hier werden die Frames vom Hauptthread oder einer anderen Quelle reingeschoben"""
        if not self.queue.full():
            self.queue.put(frame)

    def _write_frames(self):
        import time
        while self.running or not self.queue.empty():
            if not self.queue.empty():
                frame = self.queue.get()
                self.writer.write(frame)
            else:
                time.sleep(self.frame_interval)  # warten, wenn kein Frame da

    def stop(self):
        self.running = False
        self.thread.join()
        self.writer.release()