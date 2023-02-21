from __future__ import annotations

import json
import random
from typing import Dict, overload

from . import Cat

class CatGenerator():
    """Cat generator? WTF! Yes we generate cats here, welcome!"""
    def __init__(self) -> None:
        json_file = open("./cats.json", mode="r")

        self.cats_dict:Dict[str, str] =  json.load(json_file); json_file.close()

        self.cat_count = len(self.cats_dict)
    
    @overload
    def get_cat(self) -> Cat:
        """Returns random cat."""
        ...

    @overload
    def get_cat(self, cat_id:str|int) -> Cat:
        """Returns cat with that id."""
        ...

    def get_cat(self, cat_id:str|int = None) -> Cat:
        if cat_id is None:
            cat_id = random.randint(0, self.cat_count - 1)

        cat_dict = self.cats_dict[f"{cat_id}"]

        return Cat(
            name = cat_dict["name"],
            gender = cat_dict["gender"]
        )