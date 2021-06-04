from dotenv import load_dotenv
from IPython import embed

from services.podcast_editor import PodcastBlocksEditor

load_dotenv()

# jira = Jira(
#     url='',
#     username='',
#     password='')

print()
# pbe = PodcastBlocksEditor()
# pbe.assemble()

from services.jira_data_synchronizer import JiraDataSynchronizer

synch = JiraDataSynchronizer()
embed()
synch.sync()