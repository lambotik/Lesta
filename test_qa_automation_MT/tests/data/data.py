from dataclasses import dataclass


@dataclass
class Person:
    player: str = None
    credits: int = None
    gold: int = None
