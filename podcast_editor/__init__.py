from .greetings import Greetings
from .news_summary import NewsSummary


class PodcastBlocksEditor:
    ASSEMBLE_BLOCKS_CLASSES = [
        Greetings,
        NewsSummary
    ]

    def __init__(self):
        self.blocks = []

    def assemble(self) -> str:
        self.assemble_blocks()

        return ''

    def assemble_blocks(self) -> None:
        for assemble_block in self.ASSEMBLE_BLOCKS_CLASSES:
            block = assemble_block()

            self.blocks.append(block.assemble())
