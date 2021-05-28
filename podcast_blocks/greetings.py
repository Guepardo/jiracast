from models.block import Block
from models.dialog import Dialog

from .base_podcast_block import BasePodcastBlock


class Greetings(BasePodcastBlock):
    SOUND_COMMA = 'greetings'

    def assemble(self) -> Block:
        dialog = Dialog(
            voice='male',
            content="Bom dia. Hoje são 29 de maio de 2021. Eu sou o Terminator e Bem-vindo ao JiraCast, o seu podcast diário sobre tudo que acontece no Jira."
        )

        self._block.add_dialog(dialog)

        return self._block
