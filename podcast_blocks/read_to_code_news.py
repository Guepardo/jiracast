from IPython import embed

from models import Block
from models import Dialog
from services.jira_data_differentiator import JiraDataDifferentiator

from .base_podcast_block import BasePodcastBlock


class ReadToCodeNews(BasePodcastBlock):
    SOUND_COMMA = 'transition'

    def __init__(self):
        self.jira_data_differ = JiraDataDifferentiator()
        super(ReadToCodeNews, self).__init__()

    def assemble(self) -> Block:
        issues_changed_to_ready_to_code = self.jira_data_differ.get_issues_status_changed_for(
            'Live')

        if len(issues_changed_to_ready_to_code) == 0:
            self._block.skip = True

        list_normalized = list(
            map(lambda issue: f"{issue.summary}, que foi atribuída para {issue.assignee_display_name}",
                issues_changed_to_ready_to_code)
        )

        content = """
          Agora é a hora de falar sobre as tarefas que entraram em Ready To Code de ontem para hoje.

          As tarefas são:
        """

        dialog = Dialog(voice='male', content=content +
                        "\n".join(list_normalized))

        self._block.add_dialog(dialog)

        return self._block
