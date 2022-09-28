from .jira_data import JiraData
from typing import List
from models import Issue


class JiraDataDifferentiator:
    def __init__(self):
        jira_data = JiraData()

        self._today_data = jira_data.today()
        self._yesterday_data = jira_data.yesterday()

    def get_issues_status_changed_for(self, status_name) -> List[Issue]:
        issues = []

        for yesterday_issue in self._yesterday_data:
            for today_issue in self._today_data:
                if yesterday_issue.id == today_issue.id:
                    if yesterday_issue.status_name != today_issue.status_name and  \
                            today_issue.status_name == status_name:
                        issues.append(today_issue)

        return issues

    def get_today_issues_by_status_name(self, status_name: str):
        return [issue for issue in self._today_data if issue.status_name == status_name]
