class VideoReader:
    def __init__(self, total_frames=50):
        self.total_frames = total_frames
        self.current = 0

    def get_frame(self):
        if self.current < self.total_frames:
            self.current += 1
            return f"frame_{self.current}"
        else:
            return None  # no more frames
