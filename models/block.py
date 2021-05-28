from models.dialog import Dialog
from IPython import embed


class Block:
    def __init__(self, dialogs=[], type=None, sound_comma=None):
        print(dialogs)
        self.dialogs = dialogs
        self.type = type
        self.sound_comma = sound_comma

    def add_dialog(self, dialog: Dialog) -> None:
        self.dialogs.append(dialog)

    def set_sound_comma(self, sound_comma) -> None:
        self.sound_comma = sound_comma
