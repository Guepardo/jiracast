from models.issue import Issue


class IssueMapper:

    @staticmethod
    def fromRawData(data) -> Issue:
        return Issue(
            id=data['id'],
            key=data['key'],
            assignee_display_name=data['fields']['assignee']['displayName'],
            updated=data['fields']['updated'],
            created=data['fields']['created'],
            description=data['fields']['description'],
            summary=data['fields']['summary'],
            status_name=data['fields']['status']['name']
        )
