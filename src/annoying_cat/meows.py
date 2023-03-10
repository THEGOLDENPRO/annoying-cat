import os
from pygame import mixer
from enum import Enum
from . import LoggerAdapter, annoying_cat_logger

mixer.init()

class Meows(Enum):
    """Cute cat meows, what else. 🙄"""
    def __init__(self, meow_value:str):
        self.logger = LoggerAdapter(annoying_cat_logger, prefix="Meows")

    MEOW_1 = "meow_1.mp3"
    MEOW_2 = "meow_2.mp3"
    MEOW_3 = "meow_3.mp3"
    MEOW_4 = "meow_4.mp3"
    MEOW_5 = "meow_5.mp3"
    MEOW_6_LONG = "meow_6_long.mp3"
    MEOW_7 = "meow_7.mp3"

    def play(self, type:str, volume:float):
        """Plays that meow at specified volume."""
        try:
            sound = mixer.Sound(f"{os.path.abspath('./sounds')}/{type}/{self.name}")
            sound.set_volume(volume)
            sound.play()
            self.logger.debug(f"Played '{self.name}' at volume {volume}.")
        except Exception as e:
            self.logger.error(f"Couldn't play '{self.name}'! Error --> {e}")