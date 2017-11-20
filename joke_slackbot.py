import os
import urllib
import random


BOT_TOKEN = os.environ["BOT_TOKEN"]

SLACK_URL = "https://slack.com/api/chat.postMessage"


def lambda_handler(data, context):
    if "challenge" in data:
        return data["challenge"]
    slack_event = data['event']
    
    jokes = [
        "There are so many scams on the Internet these days....but for $19.95 I can show you how to avoid them",
        "I was gonna tell a time travelling joke but you guys didn't like it",
        "Apparently I snore so loudly that it scares everyone in the car I'm driving",
        "If your parachute doesn't deploy, you have the rest of your life to fix it",
        "My three favorite things are eating my family and not using commas",
        "Accordion to a recent survey, replacing words with the names of musical instruments in a sentence, often goes undetected",
        "I just made up a new word: plagiarism",
        "RIP boiling water, you will be mist"
        ]
    
    if "bot_id" in slack_event:
        print("Ignore bot")
    else:
        channel_id = slack_event["channel"]
        data = urllib.parse.urlencode(
            (
                ("token", BOT_TOKEN),
                ("channel", channel_id),
                ("text", random.choice(jokes))
            )
        )
        data = data.encode("ascii")
        
        request = urllib.request.Request(
            SLACK_URL, 
            data=data, 
            method="POST"
        )
        request.add_header(
            "Content-Type", 
            "application/x-www-form-urlencoded"
        )
        
        urllib.request.urlopen(request).read()

    return "200 OK"
