import random
import pyautogui
from threading import Thread
from . import LoggerAdapter, annoying_cat_logger

from .cat import Cat

class NoClose(Thread):
    def __init__(self, cat:Cat) -> None:
        self.cat = cat
        self.window = cat.get_window()
        self.logger = LoggerAdapter(annoying_cat_logger, prefix="NoClose")
        
        self.move_count = 0
        super().__init__(daemon=True)

    def run(self):
        while True:
            if not self.window is None:
                your_mouse_pos = pyautogui.position()

                if -(self.window.y - your_mouse_pos.y) < 30 and -(self.window.y - your_mouse_pos.y) > 0:
                    if -(self.window.x - your_mouse_pos.x) < 300 and -(self.window.x - your_mouse_pos.x) > 245:
                        self.window.move(
                            random.randint(50, pyautogui.size().width - 300),
                            random.randint(50, pyautogui.size().height - 300)
                        )
                        self.logger.debug(f"Cat moved to {(self.window.x, self.window.y)}!")
                        self.cat.meow(vol=0.5)

                        # Some funny messages.
                        # ----------------------
                        if self.move_count == 3:
                            self.cat.talk("You can't close me! 😜", 1.5)

                        elif self.move_count == 6:
                            self.cat.talk("Quit trying, you can't hit the close button! 😂", 3)

                        self.move_count += 1