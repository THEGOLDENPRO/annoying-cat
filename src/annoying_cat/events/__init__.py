from __future__ import annotations

from typing import TYPE_CHECKING

from abc import ABC, abstractmethod
from threading import Thread
from .. import LoggerAdapter, annoying_cat_logger

if TYPE_CHECKING:
    from ..cat import Cat

class Event(ABC, Thread):
    """
    A class representing an event that can occur within a 🐈cat. 

    An event actually inherits from python's ``threading.Thread``.
    """
    def __init__(self, name:str, cat:Cat) -> None:
        """
        A class representing an event that can occur within a 🐈cat. 

        An event actually inherits from python's ``threading.Thread``.
        """

        self.cat = cat
        """The 🐈cat this event is attached to."""

        self.logger = LoggerAdapter(annoying_cat_logger, prefix=name)
        """⭐The event's logger. 🐈"""

        super().__init__(
            name = name + f" - ({self.cat.name})",
            daemon = True
        )

    @abstractmethod
    def run(self):
        """
        The entry point of this event. Make sure to start your processes within this method. 
        
        Each event is ran on a separate thread so blocking operations like while loops are allowed.
        """
        ...

from .no_close import NoClose