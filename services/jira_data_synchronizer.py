import os
import json
from time import sleep
from datetime import datetime
from atlassian import Jira


from IPython import embed


class JiraDataSynchronizer:
    JQL_QUERY = "project = NET order by updated DESC"
    LIMIT_TO_RETRIEVE = 100
    BATCH_SIZE = 20

    def __init__(self, date=datetime.now()):
        self.date = date
        self.issues = []
        self.jira = Jira(
            url=os.getenv('JIRA_URL'),
            username=os.getenv('JIRA_USERNAME'),
            password=os.getenv('JIRA_PASSWORD'))

    def sync(self) -> list:
        self.fetch_data_from_jira()
        self.save_on_database()

    def save_on_database(self) -> None:
        dumped_issues = json.dumps(self.issues)

        with open(f'data/{self.file_name()}.json', 'w') as file:
            file.write(dumped_issues)

    def file_name(self):
        return self.date.strftime("%Y_%m_%d")

    def fetch_data_from_jira(self) -> None:
        start = 0

        while start < self.LIMIT_TO_RETRIEVE:
            data = self.jira.jql(
                self.JQL_QUERY,
                start=start,
                limit=self.LIMIT_TO_RETRIEVE
            )

            print("Querying...")

            for issue in data['issues']:
                self.issues.append(issue)

            start += self.BATCH_SIZE

            sleep(0.5)
