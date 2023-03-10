import webview
from devgoldyutils.logging import LoggerAdapter, Colours, log, add_custom_handler

LOGGER_NAME = f"{Colours.RED.value}Annoying {Colours.ORANGE.value}Cat{Colours.RESET_COLOUR.value}"
annoying_cat_logger = add_custom_handler(log.getLogger(LOGGER_NAME)); annoying_cat_logger.setLevel(log.DEBUG)

from .cat_generator import CatGenerator

class AnnoyingCat():
    def __init__(self) -> None:
        """The main class."""
        self.cat_generator = CatGenerator()

        self.logger = LoggerAdapter(
            annoying_cat_logger, 
            prefix="AnnoyingCat"
        )
    
    def start(self):
        self.cat_generator.create_cat()
        webview.start(debug=True)