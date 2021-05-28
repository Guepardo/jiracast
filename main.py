from dotenv import load_dotenv
from IPython import embed

load_dotenv()

# jira = Jira(
#     url='',
#     username='',
#     password='')


from services.podcast_editor_service import PodcastBlocksEditorService

pbe = PodcastBlocksEditorService()
pbe.assemble()
