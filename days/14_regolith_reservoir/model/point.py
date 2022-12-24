from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0
