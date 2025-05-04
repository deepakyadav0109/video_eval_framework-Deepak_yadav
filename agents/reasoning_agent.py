import os
import torch
import clip
from PIL import Image
import numpy as np
import cv2
from tqdm import tqdm

class ReasoningAgent:
    def __init__(self, frames_dir: str, prompt: str):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.prompt = prompt
        self.frames = sorted([os.path.join(frames_dir, f) for f in os.listdir(frames_dir) if f.endswith(".jpg")])
        self.model, self.preprocess = clip.load("ViT-B/32", device=self.device)

    def clip_similarity(self):
        text = clip.tokenize([self.prompt]).to(self.device)
        text_feat = self.model.encode_text(text).float()
        scores = []
        for path in tqdm(self.frames):
            image = self.preprocess(Image.open(path)).unsqueeze(0).to(self.device)
            with torch.no_grad():
                image_feat = self.model.encode_image(image).float()
                score = torch.nn.functional.cosine_similarity(image_feat, text_feat).item()
                scores.append(score)
        return scores

    def scene_changes(self, threshold=0.2):
        prev = None
        transitions = []
        for i, file in enumerate(self.frames):
            curr = cv2.imread(file, 0)
            if prev is not None:
                diff = np.mean(cv2.absdiff(prev, curr)) / 255.0
                if diff > threshold:
                    transitions.append(i)
            prev = curr
        return transitions

    def run(self):
        scores = self.clip_similarity()
        transitions = self.scene_changes()

        return {
            "mean_clip_score": float(np.mean(scores)),
            "clip_scores": scores,
            "scene_transitions": transitions
        }