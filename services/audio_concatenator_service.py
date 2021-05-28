from pydub import AudioSegment
from os.path import basename
from IPython import embed


class AudioConcatenatorService:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_paths = []

    def add_file(self, file_path):
        self.file_paths.append(file_path)

    def concat(self):
        audio = None

        for file_path in self.file_paths:
            embed()
            if audio:
                audio += AudioSegment.from_file(file_path, file_path.split(".")[-1]) # Refatorar forma de pegar extensão do arquivo
            else:
                audio = AudioSegment.from_file(file_path, file_path.split(".")[-1])

        audio.export(f"tmp/{self.file_name}", format="mp3")
