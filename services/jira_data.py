import json
from datetime import datetime, timedelta
from IPython import embed

class DataLoader:
    def __init__(self, date):
        self.date = date

    def load_file(self):
        data = None

        with open(f"data/{self.get_file_name()}.json", 'r') as file:
            data = file.read()

        embed()
        return json.loads(data)

    # TODO: Refactor this to a suitable util class.
    def get_file_name(self):
        return self.date.strftime("%Y_%m_%d")


class JiraData:
    def __init__(self):
        self.today_date = datetime.now()
        self.yesterday_date = self.today_date - timedelta(days=1)

    def today(self):
        return DataLoader(self.today_date).load_file()

    def yesterday(self):
        return DataLoader(self.yesterday_date).load_file()
