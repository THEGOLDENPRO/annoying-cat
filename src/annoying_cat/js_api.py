from .cat import Cat

class JSApi():
    def __init__(self, cat:Cat) -> None:
        self.cat = cat
    
    def get_cat(self) -> dict:
        return self.cat.__dict__