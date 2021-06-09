import arrow

class Issue:
    def __init__(self,
                 id='', key='', assignee_display_name="", updated="",
                 created="", description="", summary="", status_name=""):
        self.assignee_display_name = assignee_display_name
        self.updated = updated
        self.created = created
        self.description = description
        self.summary = summary
        self.status_name = status_name
        self.id = id
        self.key = key

    def created_timestamp(self):
        return arrow.get(self.created).timestamp()

    def updated_timestamp(self):
        return arrow.get(self.updated).timestamp()