from pydub import AudioSegment


class AudioConcatenator:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_paths = []

    def add_file(self, file_path):
        self.file_paths.append(file_path)

    def concat(self) -> str:
        audio = None

        for file_path in self.file_paths:
            file_extension = file_path.split(".")[-1]

            if audio:
                audio += AudioSegment.from_file(file_path, file_extension)
            else:
                audio = AudioSegment.from_file(file_path, file_extension)

        episode_path = f"tmp/{self.file_name}"

        audio.export(episode_path, format="mp3")
