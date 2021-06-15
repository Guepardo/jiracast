import json
from datetime import datetime, timedelta
from typing import List
from models.issue import Issue

from data_mappers.issue_mapper import IssueMapper


class DataLoader:
    def __init__(self, date):
        self.date = date

    def load_file(self):
        data = None

        with open(f"data/{self.get_file_name()}.json", 'r') as file:
            data = file.read()

        return json.loads(data)

    # TODO: Refactor this to a suitable util class.
    def get_file_name(self):
        return self.date.strftime("%Y_%m_%d")


class JiraData:
    def __init__(self):
        self.today_date = datetime.now()

        # TODO: Refactor this using arrow.
        self.yesterday_date = self.today_date - timedelta(days=1)

    def today(self) -> List[Issue]:
        return self._map_data(
            DataLoader(self.today_date).load_file()
        )

    def yesterday(self) -> List[Issue]:
        return self._map_data(
            DataLoader(self.yesterday_date).load_file()
        )

    def _map_data(self, data) -> list:
        issues = []

        for item in data:
            try:
                issues.append(
                    IssueMapper.fromRawData(item)
                )
            except:
                pass

        return issues
