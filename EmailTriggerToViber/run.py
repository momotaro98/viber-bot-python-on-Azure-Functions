import os
import os.path
import sys
import json

# Print Python version
import platform
message = "Using Python '{0}'".format(platform.python_version())
print(message)

# Add library path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'site-packages')))

# Print path
print("sys.path", sys.path)

from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

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
