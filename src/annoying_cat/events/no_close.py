from __future__ import annotations

from typing import TYPE_CHECKING

import time
import random
import pyautogui
import _thread

if TYPE_CHECKING:
    from ..cat import Cat

from . import Event

class NoClose(Event):
    """⛔ Prevents you from hitting the ❌ close button on the cat's window."""
    def __init__(self, cat:Cat) -> None:
        self.window = cat.window

        self.move_count = 0

        super().__init__(
            name = "No Close",
            cat = cat
        )

    def run(self):
        while True:
            your_mouse_pos = pyautogui.position()

            if -(self.window.y - your_mouse_pos.y) < 30 and -(self.window.y - your_mouse_pos.y) > 0:
                if -(self.window.x - your_mouse_pos.x) < 300 and -(self.window.x - your_mouse_pos.x) > 245:
                    self.window.move(
                        random.randint(50, pyautogui.size().width - 300),
                        random.randint(50, pyautogui.size().height - 300)
                    )
                    self.logger.debug(f"Cat moved to {(self.window.x, self.window.y)}!")
                    self.cat.meow(vol=0.5)

                    # Some funny messages and sub events.
                    # -------------------------------------
                    if self.move_count == 3:
                        self.cat.talk("You can't close me! 😜", 1.5)

                    elif self.move_count == 6:
                        self.cat.talk("Quit trying, you can't hit the close button! 😂", 3)

                    elif self.move_count == 15:
                        self.cat.talk("Okay seriously stop now!", 3)

                    elif self.move_count == 25:
                        self.cat.talk("Bro ACTUALLY STOP, it's not funny anymore!", 3)

                    elif self.move_count == 50:
                        self.cat.talk("I'm telling you man, YOU CAN'T CLOSE ME! 🤬", 5)

                    elif self.move_count == 100:
                        self.cat.talk("💀 Bro's still doing it. 💀", 5)

                    elif self.move_count == 200:
                        self.cat.talk("You have no life you know.", 5)

                    elif self.move_count == 250:
                        self.cat.talk("Fu#K IT I'M CLOSING MYSELF!!!", 2)
                        time.sleep(3)
                        self.cat.talk("In 3...", 1)
                        time.sleep(1.1)
                        self.cat.talk("2...", 1)
                        time.sleep(1.1)
                        self.cat.talk("1...", 1)
                        time.sleep(1.1)
                        self.cat.window.destroy()
                        _thread.interrupt_main()

                    self.move_count += 1