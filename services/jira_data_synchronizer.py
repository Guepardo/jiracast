import os
from time import sleep
from datetime import datetime
from atlassian import Jira


from IPython import embed

class JiraDataSynchronizer:
    JQL_QUERY = "project = NET order by updated DESC"
    LIMIT_TO_RETRIEVE = 500
    BATCH_SIZE = 20

    def __init__(self, date=datetime.now()):
        self.date = date
        self.jira = Jira(
            url=os.getenv('JIRA_URL'),
            username=os.getenv('JIRA_USERNAME'),
            password=os.getenv('JIRA_PASSWORD'))

    def sync(self) -> list:
        tasks = []
        start = 0

        while start < self.LIMIT_TO_RETRIEVE:
            data = self.jira.jql(
                self.JQL_QUERY,
                start=start,
                limit=self.LIMIT_TO_RETRIEVE
            )

            embed()

            tasks.append(data)
            start += self.BATCH_SIZE

            sleep(0.5)

        return tasks

