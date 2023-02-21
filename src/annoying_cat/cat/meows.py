import os
from pygame import mixer
from enum import Enum
from .. import LoggerAdapter, annoying_cat_logger

mixer.init()

class Meows(Enum):
    def __init__(self, meow_value:str):
        self.logger = LoggerAdapter(annoying_cat_logger, prefix="MeowManager")
        mixer.init()

    def play(self, volume:float):
        """Plays that meow at specified volume."""
        try:
            meow_sound = mixer.Sound(f"{os.path.abspath('./sounds')}/{self.value}")
            meow_sound.set_volume(volume)
            meow_sound.play()
            self.logger.debug(f"Played '{self.name}' at volume {volume}.")
        except Exception as e:
            self.logger.error(f"Couldn't play '{self.name}'! Error --> {e}")


class CuteMeows(Meows):
    """Cute cat meows, what else. 🙄"""
    MEOW_1 = "/cute_meows/meow_1.mp3"
    MEOW_2 = "/cute_meows/meow_2.mp3"
    MEOW_3 = "/cute_meows/meow_3.mp3"
    MEOW_4 = "/cute_meows/meow_4.mp3"
    MEOW_5 = "/cute_meows/meow_5.mp3"
    MEOW_6_LONG = "/cute_meows/meow_6_long.mp3"
    MEOW_7 = "/cute_meows/meow_7.mp3"