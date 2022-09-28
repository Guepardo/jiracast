from typing import List
from podcast_blocks.base_podcast_block import BasePodcastBlock

from models import Block
from models import Dialog
from services.jira_data_differentiator import JiraDataDifferentiator
from IPython import embed

from .base_podcast_block import BasePodcastBlock


class DangerZoneNews(BasePodcastBlock):
    SOUND_COMMA = 'transition'

    WIP_COUNT_LIMIT = 2
    TEAM_DANGER_ZONE_LIMIT = 3

    DANGER_ZONE_STATUS_NAMES = [
        'In Progress',
        'QA - BDD',
        'Homolog - Doing',
        'Fixing',
        'FIX - Code Review',
        'Under Review',
        'CR - DONE'
    ]

    def __init__(self):
        self.jira_data_differ = JiraDataDifferentiator()
        super(DangerZoneNews, self).__init__()

    def generate_report(self) -> List:
        developers = list(
            set([x.assignee_display_name for x in self.jira_data_differ._today_data])
        )

        developer_danger_zone_count = []

        for developer in developers:
            developer_issues = filter(
                lambda x: x.assignee_display_name == developer, self.jira_data_differ._today_data
            )

            count = len(
                [x for x in developer_issues
                 if x.status_name in self.DANGER_ZONE_STATUS_NAMES]
            )

            developer_danger_zone_count.append(
                (developer, count)
            )

        return list(
            filter(lambda x: x[-1] > self.WIP_COUNT_LIMIT,
                   developer_danger_zone_count)
        )

    def assemble(self) -> Block:
        report = self.generate_report()

        if len(report) == 0:
            self._block.skip = True

        list_normalized = list(
            map(lambda issue: f"{issue[0]} tem {issue[1]} tarefas",
                report)
        )

        content = """
          Neste bloco falaremos sobre os desenvolvedores que estão com muitas tarefas em andamento.

          Os desenvolvedores são:
        """

        dialog = Dialog(voice='male', content=content +
                        "\n".join(list_normalized))

        self._block.add_dialog(dialog)

        if len(report) > self.TEAM_DANGER_ZONE_LIMIT:
            content = f"""
            A zona perigosa significa que a tarefa pode potencialmente volarar para o desenvolvedor em algum momento da sprint.
            Hoje temos {len(report)} dos desenvolvedores na zona perigosa os prazos de entrega podem ser comprometidos.
          """

            dialog = Dialog(voice='male', content=content)
            self._block.add_dialog(dialog)

        return self._block
