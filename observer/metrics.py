from collections import deque

class Observer:
    def __init__(self, window=1):  # <--- set window=1 for testing
        self.confidences = deque(maxlen=window)

    def observe(self, prediction):
        self.confidences.append(prediction["confidence"])
        avg = sum(self.confidences) / len(self.confidences)
        return {
            "avg_confidence": avg,
            "num_predictions": len(self.confidences)
        }
