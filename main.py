from source.video_reader import VideoReader
from detector.service import DetectorService
from observer.metrics import Observer
from judge.rules import Judge
from trainer.train import Trainer
import time
import logging
import random
def notify():
    print("🚨 ALERT!")

# Initialize components
detector = DetectorService()
source = VideoReader(total_frames=50)
observer = Observer(window=1)  # window=1
judge = Judge(threshold=0.5, retrain_threshold=0.3)
trainer = Trainer()

while True:
    frame = source.get_frame()
    if frame is None:
        print("✅ End of video stream")
        break
    # if random.random() < 0.05: 
    #     frame = None


    prediction = detector.run(frame)
    metrics = observer.observe(prediction)
    decision = judge.evaluate(metrics)


    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    logging.info(f"{frame} | conf: {prediction['confidence']:.2f} | avg: {metrics['avg_confidence']:.2f} | decision: {decision}")

    if decision == "ALERT":
        notify()
    if decision == "RETRAIN":
        trainer.train()

    time.sleep(0.1)  # simulate frame interval
