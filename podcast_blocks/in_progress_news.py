from podcast_blocks.base_podcast_block import BasePodcastBlock

from models import Block
from models import Dialog
from services.jira_data_differentiator import JiraDataDifferentiator

from .base_podcast_block import BasePodcastBlock


class InProgressNews(BasePodcastBlock):
    SOUND_COMMA = 'transition'

    def __init__(self):
        self.jira_data_differ = JiraDataDifferentiator()
        super(InProgressNews, self).__init__()

    def assemble(self) -> Block:
        issues_changed_to_in_progress = self.jira_data_differ.get_issues_status_changed_for(
            'In Progress')

        if len(issues_changed_to_in_progress) == 0:
            self._block.skip = True

        list_normalized = list(
            map(lambda issue: f"{issue.summary}, que foi atribuída para {issue.assignee_display_name}",
                issues_changed_to_in_progress)
        )

        content = """
          Neste bloco falaremos das tarefas que estão em progresso e foram atribuídas para algum desenvolvedor nas últimas 24 horas.

          As tarefas são:
        """

        dialog = Dialog(voice='male', content=content +
                        "\n".join(list_normalized))

        self._block.add_dialog(dialog)

        return self._block
