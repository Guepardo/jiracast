from models import Block


class BasePodcastBlock:
    def __init__(self):
        self.block = Block(sound_comma=self.SOUND_COMMA)

    def assemble(self) -> Block:
        raise NotImplementedError("Please, implemented this method")
