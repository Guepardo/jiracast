# import pyttsx3
# engine = pyttsx3.init()

# voices = engine.getProperty('voices')

# for voice in voices:
#     print(voice)

# engine.setProperty('voice', 'brazil')
# engine.say('Cade o Ei Merd pra pedir pro meu patrão me demitir agora? Vai reclamar com o batman q eu tô lacrando')
# engine.runAndWait()

# from atlassian import Jira

from IPython import embed

# jira = Jira(
#     url='',
#     username='',
#     password='')


from podcast_editor import PodcastBlocksEditor

pbe = PodcastBlocksEditor()
pbe.assemble()
embed()