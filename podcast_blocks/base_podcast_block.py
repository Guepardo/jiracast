from services.jira_data import JiraData
from typing import List
from models import Issue
from models import Block


class BasePodcastBlock:
    def __init__(self):
        self._block = Block(dialogs=[], sound_comma=self.SOUND_COMMA)

        jira_data = JiraData()

        self._today_data = jira_data.today()
        self._yesterday_data = jira_data.yesterday()

    def assemble(self) -> Block:
        raise NotImplementedError("Please, implemented this method")

    def get_issues_status_changed_for(self, status_name) -> List[Issue]:
        issues = []

        for yesterday_issue in self._yesterday_data:
            for today_issue in self._today_data:
                if yesterday_issue.id == today_issue.id:
                    if yesterday_issue.status_name != today_issue.status_name and  \
                            today_issue.status_name == status_name:
                        issues.append(today_issue)

        return issues
