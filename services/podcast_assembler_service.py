import uuid
from .tts.local_text_to_speech import LocalTextToSpeechService
from .audio_concatenator_service import AudioConcatenatorService


class PodcastAssemblerService:
    def __init__(self, blocks: list):
        self.blocks = blocks
        self.audio_concatenator = AudioConcatenatorService('episode.mp3')

    def assemble(self) -> str:
        for block in self.blocks:
            self.audio_concatenator.add_file(
                self.find_file_path_from_assets(
                    block.sound_comma
                )
            )

            for dialog in block.dialogs:
                temp_path = uuid.uuid4()

                service = LocalTextToSpeechService(dialog, temp_path)
                file_path = service.tts()

                self.audio_concatenator.add_file(file_path)

        self.audio_concatenator.concat()

    def find_file_path_from_assets(self, sound_comma) -> str:
        return f'assets/{sound_comma}.mp3'
