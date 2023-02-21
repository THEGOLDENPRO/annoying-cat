import random
from dataclasses import dataclass
from .meows import CuteMeows, Meows

previous_meow:Meows = None

@dataclass
class Cat:
    """A cat, duhhhh!"""
    name:str
    gender:str

    def meow(self, meow:Meows=None, vol:float=0.5) -> None:
        """Forces the cat to MEOW!"""
        global previous_meow

        if meow is None:
            meow = random.choice(list(CuteMeows))

            if not previous_meow is None:
                if meow.value == previous_meow.value:
                    return self.meow()

        meow.play(vol)
        previous_meow = meow
        return None