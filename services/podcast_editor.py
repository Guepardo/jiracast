from podcast_blocks import Greetings
from podcast_blocks import NewsSummary
from podcast_blocks import ReadToCodeNews
from podcast_blocks import InProgressNews
from podcast_blocks import DangerZoneNews

from services.podcast_assembler import PodcastAssembler


class PodcastBlocksEditor:
    ASSEMBLE_BLOCKS_CLASSES = [
        Greetings,
        NewsSummary,
        ReadToCodeNews,
        InProgressNews,
        DangerZoneNews
    ]

    def __init__(self):
        self.blocks = []

    def assemble(self) -> str:
        self.assemble_blocks()
        self.assemble_podcast()

        return ''

    def assemble_blocks(self) -> None:
        for assemble_block in self.ASSEMBLE_BLOCKS_CLASSES:
            assemble_block_instance = assemble_block()

            block = assemble_block_instance.assemble()

            if block.skip:
                continue

            self.blocks.append(block)

    # TODO: remover isso daqui e parar para a classe JiraCast
    def assemble_podcast(self) -> None:
        podcast_assembler_service = PodcastAssembler(self.blocks)
        podcast_assembler_service.assemble()
