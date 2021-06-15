from IPython import embed

from models import Block
from models import Dialog

from .base_podcast_block import BasePodcastBlock


class ReadToCodeNews(BasePodcastBlock):
    SOUND_COMMA = 'transition'

    def assemble(self) -> Block:
        issues_chenged_to_ready_to_code = super().get_issues_status_changed_for('Live')

        list_normalized = list(
            map(lambda issue: f"{issue.summary}, que foi atribuída para {issue.assignee_display_name}",
                issues_chenged_to_ready_to_code)
        )


        content = """
          Agora é a hora de falar sobre as tarefas que entraram em Ready To Code de ontem para hoje.

          As tarefas são:
        """

        dialog = Dialog(voice='male', content=content + "\n".join(list_normalized))

        self._block.add_dialog(dialog)

        return self._block
