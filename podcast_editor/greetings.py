from models import Block
from models import Dialog

from .base_podcast_block import BasePodcastBlock


class Greetings(BasePodcastBlock):
    SOUND_COMMA = 'greetings'

    def assemble(self) -> Block:
        dialog = Dialog(
            voice='male',
            content="Bem-vindo ao JiraCast. O seu podcast diário sobre tudo que acontece no Jira."
        )

        self.block.add_dialog(dialog)

        return self.block