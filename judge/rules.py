class Judge:
    def __init__(self, threshold=0.5, retrain_threshold=0.3):
        self.threshold = threshold
        self.retrain_threshold = retrain_threshold
        self.low_count = 0

    def evaluate(self, metrics):
        avg = metrics["avg_confidence"]

        if avg < self.retrain_threshold:
            self.low_count += 1
            if self.low_count >= 3:
                self.low_count = 0
                return "RETRAIN"
        elif avg < self.threshold:
            # alert but do not reset low_count
            return "ALERT"
        else:
            # avg above threshold → reset low_count
            self.low_count = 0

        return "OK"
