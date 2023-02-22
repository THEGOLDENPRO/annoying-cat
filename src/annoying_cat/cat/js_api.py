from . import Cat

class CatApi():
    def __init__(self, cat:Cat) -> None:
        self.cat = cat
    
    def get_cat(self) -> dict:
        """Returns cat info as dict."""
        return self.cat.__dict__

    def talk(self, text:str, rm_delay:int=5) -> None:
        """Makes cat display text."""
        self.cat.talk(text, rm_delay)
        return None