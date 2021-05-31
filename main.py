from dotenv import load_dotenv
from IPython import embed

load_dotenv()

# jira = Jira(
#     url='',
#     username='',
#     password='')


from services.podcast_editor import PodcastBlocksEditor

pbe = PodcastBlocksEditor()
pbe.assemble()
