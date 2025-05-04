import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

class PerceptionAgent:
    def __init__(self, video_path: str, frame_dir: str = "frames"):
        self.video_path = video_path
        self.frame_dir = frame_dir
        os.makedirs(frame_dir, exist_ok=True)

    def extract_frames(self, fps=1):
        cap = cv2.VideoCapture(self.video_path)
        orig_fps = cap.get(cv2.CAP_PROP_FPS)
        step = int(orig_fps / fps)
        count = 0
        frames = []

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if count % step == 0:
                path = f"{self.frame_dir}/frame_{len(frames)}.jpg"
                cv2.imwrite(path, cv2.resize(frame, (640, 360)))
                frames.append(frame)
            count += 1
        cap.release()
        return frames

    def compute_optical_flow(self, frames):
        flows = []
        prev = cv2.cvtColor(frames[0], cv2.COLOR_BGR2GRAY)
        for i in range(1, len(frames)):
            curr = cv2.cvtColor(frames[i], cv2.COLOR_BGR2GRAY)
            flow = cv2.calcOpticalFlowFarneback(prev, curr, None, 0.5, 3, 15, 3, 5, 1.2, 0)
            mag, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
            flows.append(np.mean(mag))
            prev = curr
        return flows

    def run(self):
        frames = self.extract_frames()
        flows = self.compute_optical_flow(frames)

        plt.plot(flows)
        plt.title("Optical Flow Magnitude")
        plt.savefig("report/optical_flow.png")

        return {
            "average_flow": float(np.mean(flows)),
            "flow_std_dev": float(np.std(flows)),
            "num_frames": len(frames)
        }