from __future__ import annotations

import json
import random
import webview
from typing import Dict, overload

from . import LoggerAdapter, annoying_cat_logger
from .cat import Cat

class CatGenerator():
    """Cat generator? WTF! Yes we generate cats here, welcome!"""
    def __init__(self) -> None:
        json_file = open("./cat_types.json", mode="r")

        self.cat_types:Dict[str, str] =  json.load(json_file); json_file.close()
        self.cat_types_count = len(self.cat_types)

        self.logger = LoggerAdapter(annoying_cat_logger, prefix="CatGenerator")
    
    @overload
    def create_cat(self) -> Cat:
        """Creates and returns random cat."""
        ...

    @overload
    def create_cat(self, cat_id:str|int) -> Cat:
        """Creates and returns cat with that id."""
        ...

    def create_cat(self, cat_id:str|int = None) -> Cat:
        if cat_id is None:
            cat_id = random.randint(0, self.cat_types_count - 1)

        cat_dict = self.cat_types[f"{cat_id}"]

        cat = Cat(
            name = cat_dict["name"],
            gender = cat_dict["gender"],
            window = webview.create_window(
                title=cat_dict["name"],
                width=300,
                height=300,
                resizable=False,
                on_top=True,

                url="./web/index.html"
            )
        )

        # TODO: Create a system with a method that can bind all events to the cat.
        #NoClose(cat).start()

        return cat