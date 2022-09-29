from IPython import embed
import arrow
from models import Block
from models import Dialog
from services.jira_data_differentiator import JiraDataDifferentiator

from .base_podcast_block import BasePodcastBlock


class HappyBirthdayNews(BasePodcastBlock):
    SOUND_COMMA = 'transition'

    DAYS_COUNT_LIMIT = 15

    def __init__(self):
        self.jira_data_differ = JiraDataDifferentiator()
        super(HappyBirthdayNews, self).__init__()

    def assemble(self) -> Block:
        issues = list(
            map(lambda x: (x, (arrow.now() - arrow.get(x.updated)).days),
                self.jira_data_differ._today_data)
        )

        issues = list(filter(lambda x: x[-1] >= self.DAYS_COUNT_LIMIT, issues))
        issues.sort(key=lambda x: x[-1], reverse=True)

        content = """
          Neste bloco falaremos das tarefas que estão a mais de {self.DAYS_COUNT_LIMIT} sem nenhuma atualização.

          As tarefas são:
        """

        list_normalized = list(
            map(lambda x: f"A tarefa {x[0].summary} está com {x[-1]} dias parada no board", issues)
        )

        dialog = Dialog(voice='male', content=content +
                        "\n".join(list_normalized))

        self._block.add_dialog(dialog)

        return self._block
