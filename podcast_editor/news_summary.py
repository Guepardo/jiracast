from models import Block
from models import Dialog

from .base_podcast_block import BasePodcastBlock


class NewsSummary(BasePodcastBlock):
    SOUND_COMMA = 'news_summary'

    def assemble(self) -> Block:
        content = """
          Ontem rolaram várias mudanças nos nossos boards

          Agora ficou bem mais claro, como é mais acessível em videos do youtube aulas de Orientação a Objetos em outras linguagens, como Java por exemplo, durante o aprendizado acabei ficando com alguns vícios e eu gosto do estilo de programação do Python bem mais que do java, portanto sempre que me deparo com situações onde no java seria feito de determinado jeito e a comunidade Python diz para evitar antes de aderir quero entender porque evitar (não menosprezando a comunidade é claro, com certeza são muito mais experientes que eu, é apenas questão de aprendizado). Muito obrigado pela ajuda.
        """

        dialog = Dialog(voice='male', content=content)

        self.block.add_dialog(dialog)

        return self.block
