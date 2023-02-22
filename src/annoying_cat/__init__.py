from __future__ import annotations

import random
import webview
import pyautogui
from threading import Thread
from devgoldyutils import Colours

from .logging import add_custom_handler, log, LoggerAdapter

LOGGER_NAME = f"{Colours.RED.value}Annoying {Colours.ORANGE.value}Cat{Colours.RESET_COLOUR.value}"
annoying_cat_logger = add_custom_handler(log.getLogger(LOGGER_NAME)); annoying_cat_logger.setLevel(log.DEBUG)

from .no_close import NoClose

class AnnoyingCat():
    def __init__(self) -> None:
        self.master_cat = CatGenerator().create_cat()
        """The main/first cat essentially."""

        self.logger = LoggerAdapter(annoying_cat_logger, prefix="AnnoyingCat")
    
    def start(self):
        webview.start(debug=True)


from .cat.generator import CatGenerator