from __future__ import annotations

import random
import ctypes
from webview import Window
from dataclasses import dataclass, field

from .. import annoying_cat_logger, LoggerAdapter, log
from .meows import CuteMeows, Meows

previous_meow:Meows = None

@dataclass
class Cat:
    """A cat, duhhhh!"""
    name:str
    gender:str

    __window:Window|str|None = field(init=False, default=None, repr=False)

    def meow(self, meow:Meows=None, vol:float=0.5) -> Cat:
        """Forces the cat to MEOW!"""
        global previous_meow

        if meow is None:
            meow = random.choice(list(CuteMeows))

            if not previous_meow is None:
                if meow.value == previous_meow.value:
                    return self.meow()

        meow.play(vol)
        previous_meow = meow
        return self

    def talk(self, text:str, rm_delay:int = 5) -> Cat:
        """Let's the cat talk. It displays text under the cat, duhhhh! What else did you think."""
        window = self.get_window()

        if not window is None:
            
            window.evaluate_js("""
                var cat_talk_box = document.getElementById("cat_talk_box");
                cat_talk_box.innerText = "{text}";

                setTimeout(function() {
                    cat_talk_box.innerText = "...";
                }, {rm_delay})
                """.replace("{rm_delay}", str(rm_delay * 1000)).replace("{text}", text)
            )

            annoying_cat_logger.debug(f"Cat '{self.name}' said '{text}'.")
        
        return self

    def bind_window(self, window:Window) -> None:
        """Bind a pywebview window to this cat."""
        self.__window = str(window)
        return None

    def get_window(self) -> Window|None:
        """Get the window from this cat."""
        if self.__window is None:
            return None
        
        return ctypes.cast(int(self.__window[-19:-1], 16), ctypes.py_object).value