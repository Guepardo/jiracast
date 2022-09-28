from models import Block
from models import Dialog
from services.jira_data_differentiator import JiraDataDifferentiator

from .base_podcast_block import BasePodcastBlock


class NewsSummary(BasePodcastBlock):
    SOUND_COMMA = 'transition'

    def __init__(self):
        self.jira_data_differ = JiraDataDifferentiator()
        super(NewsSummary, self).__init__()

    def assemble(self) -> Block:
        changed_to_in_progress = self.status_changed_count('In Progress')
        changed_to_done = self.status_changed_count('Done')
        changed_to_selected_for_release = self.status_changed_count(
            'Selected for Release')
        changed_to_live = self.status_changed_count('Live')

        content = f"""
            De ontem para hoje tivemos várias movimentações nos nossos boards.

            {changed_to_in_progress} tarefas saíram de Ready To Code para em progresso.
            {changed_to_done} tarefas foram homologadas.
            {changed_to_selected_for_release} tarefas foram selecionadas para produção.
            E {changed_to_live} foram entregues em produção.
        """

        dialog = Dialog(voice='male', content=content)

        self._block.add_dialog(dialog)

        return self._block

    def status_changed_count(self, status_target):
        return len(
            self.jira_data_differ.get_issues_status_changed_for(status_target)
        )
