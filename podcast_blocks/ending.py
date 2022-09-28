import arrow

from models import Block
from models import Dialog

from .base_podcast_block import BasePodcastBlock


class Ending(BasePodcastBlock):
    SOUND_COMMA = 'transition'

    def __init__(self):
        super(Ending, self).__init__()

    def assemble(self) -> Block:
        return self._block
