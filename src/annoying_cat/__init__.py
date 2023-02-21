from __future__ import annotations

import random
import webview
import pyautogui
from threading import Thread
from devgoldyutils import Colours

from .logging import add_custom_handler, log, LoggerAdapter

LOGGER_NAME = f"{Colours.RED.value}Annoying {Colours.ORANGE.value}Cat{Colours.RESET_COLOUR.value}"
annoying_cat_logger = add_custom_handler(log.getLogger(LOGGER_NAME)); annoying_cat_logger.setLevel(log.DEBUG)

from .js_api import JSApi
from .no_close import NoClose

class AnnoyingCat():
    def __init__(self) -> None:
        self.cat, self.window = self.create_cat()
        self.logger = LoggerAdapter(annoying_cat_logger, prefix="AnnoyingCat")

        self.no_close = NoClose(self.window, self.cat, self.logger)

    def start(self):
        self.no_close.start()

        webview.start(debug=True)

    def create_cat(self):
        cat = CatGenerator().get_cat()
        window = webview.create_window(
            title = f"{cat.name}",
            width=300,
            height=300,
            resizable=False,
            
            js_api=JSApi(cat),

            url="./web/index.html"
        )

        return cat, window


from .cat.generator import CatGenerator