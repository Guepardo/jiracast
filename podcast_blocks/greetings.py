import arrow

from models import Block
from models import Dialog

from .base_podcast_block import BasePodcastBlock


class Greetings(BasePodcastBlock):
    SOUND_COMMA = 'greetings'

    def __init__(self):
        super(Greetings, self).__init__()

        self.current_month_name = arrow.now().format('MMMM', locale='pt-BR')
        self.date = arrow.now()

    def assemble(self) -> Block:
        content = f"""
            Bom dia. Hoje são {self.date.day} de {self.current_month_name} de {self.date.year}.
            Eu sou o Terminator e Bem-vindo ao JiraCast, o seu podcast diário sobre tudo que acontece no Jira.
        """

        dialog = Dialog(
            voice='male',
            content=content
        )

        self._block.add_dialog(dialog)

        return self._block
