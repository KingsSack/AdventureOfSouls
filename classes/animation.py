from dataclasses import dataclass


@dataclass
class Animation:
    path: str
    name: str
    num_frames: int
    fps: int
    frames: list
    index: int = 0
