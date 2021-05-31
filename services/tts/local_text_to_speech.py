from models import Dialog
from gtts import gTTS


class LocalTextToSpeechService:
    VOLUME = 1.0
    VOICE = 'brazil'

    def __init__(self, dialog: Dialog, temp_path: str):
        self.dialog = dialog
        self.temp_path = temp_path

        self.configure_engine()

    def tts(self) -> str:
        file_path = f'tmp/{self.temp_path}.mp3'
        self.engine.save(file_path)

        return file_path

    def configure_engine(self):
        self.engine = gTTS(self.dialog.content, lang='pt', tld='com.br')
