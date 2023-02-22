from __future__ import annotations

import json
import random
import webview
from typing import Dict, overload

from . import Cat
from .js_api import CatApi

from .. import LoggerAdapter, annoying_cat_logger
from ..no_close import NoClose

class CatGenerator():
    """Cat generator? WTF! Yes we generate cats here, welcome!"""
    def __init__(self) -> None:
        json_file = open("./cats.json", mode="r")

        self.cats_dict:Dict[str, str] =  json.load(json_file); json_file.close()

        self.cat_count = len(self.cats_dict)

        self.logger = LoggerAdapter(annoying_cat_logger, prefix="CatGenerator")
    
    @overload
    def create_cat(self) -> Cat:
        """Creates and returns random cat."""
        ...

    @overload
    def create_cat(self, cat_id:str|int) -> Cat:
        """Creates amd returns cat with that id."""
        ...

    def create_cat(self, cat_id:str|int = None) -> Cat:
        if cat_id is None:
            cat_id = random.randint(0, self.cat_count - 1)

        cat_dict = self.cats_dict[f"{cat_id}"]

        cat = Cat(
            name = cat_dict["name"],
            gender = cat_dict["gender"]
        )

        cat.bind_window(
            webview.create_window(
                title = f"{cat.name}",
                width=300,
                height=300,
                resizable=False,
                on_top=True,

                js_api=CatApi(cat),

                url="./web/index.html"
            )
        )

        NoClose(cat).start()

        return cat