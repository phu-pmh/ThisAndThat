import sys
from wit import Wit

if len(sys.argv) != 2:
    exit(1)
access_token = sys.argv[1]

# Quickstart example
# See https://wit.ai/ar7hur/Quickstart

def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def send(request, response):
    print(response['text'])

def get_forecast(request):
    context = request['context']
    entities = request['entities']
    print(context)
    print(entities)

    loc = first_entity_value(entities, 'location')
    if loc:
        context['forecast'] = 'cloudy'
    else:
        context['forecast'] = 'rainy'
        context['missingLocation'] = True
 
    return context

actions = {
    'send': send,
    'getForecast': get_forecast
}

client = Wit(access_token=access_token, actions=actions)
session_id = 'my-user-session-42'
context0 = {}
context1 = client.run_actions(session_id, 'What is the forecast in Yangon?', context0)
print('The session state is now: ' + str(context1))