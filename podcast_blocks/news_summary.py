from models import Block
from models import Dialog

from .base_podcast_block import BasePodcastBlock


class NewsSummary(BasePodcastBlock):
    SOUND_COMMA = 'transition'

    def __init__(self):
        super(NewsSummary, self).__init__()

    def assemble(self) -> Block:
        chenged_to_in_progress = self.status_changed_count('In Progress')
        chenged_to_done = self.status_changed_count('Done')
        chenged_to_selected_for_release = self.status_changed_count(
            'Selected for Release')
        chenged_to_live = self.status_changed_count('Live')

        content = f"""
            De ontem para hoje tivemos várias movimentações nos nossos boards.

            {chenged_to_in_progress} tarefas saíram de Ready To Code para em progresso.
            {chenged_to_done} tarefas foram homologadas.
            {chenged_to_selected_for_release} tarefas foram selecionadas para produção.
            E {chenged_to_live} estão em produção.
        """

        dialog = Dialog(voice='male', content=content)

        self._block.add_dialog(dialog)

        return self._block

    def status_changed_count(self, status_target):
        return len(
            super().get_issues_status_changed_for(status_target)
        )
