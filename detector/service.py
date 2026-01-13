import random
import time

class DetectorService:
    def run(self, frame):
        # For testing: low confidence every 3 frames
        if "3" in frame or "6" in frame or "9" in frame:
            confidence = random.uniform(0.0, 0.25)  # very low
        else:
            confidence = random.uniform(0.4, 0.8)
        return {
            "label": "object",
            "confidence": confidence,
            "timestamp": time.time()
        }
