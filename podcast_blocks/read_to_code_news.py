from models import Block
from models import Dialog

from .base_podcast_block import BasePodcastBlock


class ReadToCodeNews(BasePodcastBlock):
    SOUND_COMMA = 'transition'

    def assemble(self) -> Block:
        content = """
          Agora é a hora de falar sobre as tarefas que entraram em Ready To Code de ontem para hoje.

          As tarefas são:

          [VOD] Remoção de chave em upload de vídeos e adição de chave dinâmica
          [VOD] Criar rotina para arquivar conteúdos de canais inativados
          [VOD] Erro ao finalizar transmissão utilizando CDN customizada
        """

        dialog = Dialog(voice='male', content=content)

        self._block.add_dialog(dialog)

        return self._block
