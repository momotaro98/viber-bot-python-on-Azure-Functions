import os
import json

from viberbot_lib.viberbot import Api
from viberbot_lib.viberbot.api.bot_configuration import BotConfiguration
from viberbot_lib.viberbot.api.messages.text_message import TextMessage
from viberbot_lib.viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot_lib.viberbot.api.viber_requests import ViberFailedRequest
from viberbot_lib.viberbot.api.viber_requests import ViberMessageRequest
from viberbot_lib.viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot_lib.viberbot.api.viber_requests import ViberUnsubscribedRequest

viber = Api(BotConfiguration(
  name='InternalOpeBot',
  avatar='',
  auth_token=os.getenv('VIBER_API_KEY') or 'default'
))

postreqdata = json.loads(open(os.environ['req']).read())
print(postreqdata)
response = open(os.environ['res'], 'w')
response.write("hello world from "+postreqdata['name'])
response.close()
