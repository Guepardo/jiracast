from podcast_blocks.greetings import Greetings
from podcast_blocks.news_summary import NewsSummary
from podcast_blocks.read_to_code_news import ReadToCodeNews

from services.podcast_assembler_service import PodcastAssemblerService

class PodcastBlocksEditorService:
    ASSEMBLE_BLOCKS_CLASSES = [
        Greetings,
        NewsSummary,
        ReadToCodeNews
    ]

    def __init__(self):
        self.blocks = []

    def assemble(self) -> str:
        self.assemble_blocks()
        self.assemble_podcast()

        return ''

    def assemble_blocks(self) -> None:
        for assemble_block in self.ASSEMBLE_BLOCKS_CLASSES:
            block = assemble_block()

            self.blocks.append(block.assemble())


    def assemble_podcast(self) -> None:
        podcast_assembler_service = PodcastAssemblerService(self.blocks)
        podcast_assembler_service.assemble()