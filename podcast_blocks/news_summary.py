from models import Block
from models import Dialog

from .base_podcast_block import BasePodcastBlock


class NewsSummary(BasePodcastBlock):
    SOUND_COMMA = 'transition'

    def assemble(self) -> Block:
        content = """
            De ontem para hoje tivemos várias movimentações nos nossos boards.

            Dez tarefas saíra de Ready To Code para em progresso.
            Duas tarefas foram homologadas.
            Três tarefas foram selecionadas para produção.
            E duas estão em produção.

        """

        dialog = Dialog(voice='male', content=content)

        self._block.add_dialog(dialog)

        return self._block
