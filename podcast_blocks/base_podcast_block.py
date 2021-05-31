from models import Block

class BasePodcastBlock:
    def __init__(self):
        self._block = Block(dialogs=[], sound_comma=self.SOUND_COMMA)

    def assemble(self) -> Block:
        raise NotImplementedError("Please, implemented this method")
