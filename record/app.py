from flask import Flask, request, url_for
from tiniyo.rest import Client
from tiniyo.voice_response import VoiceResponse
from xmlhelp import tiniyoml
from config import *
from pprint import pprint

app = Flask(__name__)


@app.route('/voicecall-record/tiniyo', methods=['GET', 'POST'])
def record():
    response = VoiceResponse()
    response.say(message="Hello. Thank you for Calling." +
                         "We are unable to answer the phone right now." +
                         "Please leave your message with your name and contact information." +
                         "We wil return you call as soon as possible." +
                         "Please leave a message after the beep.")
    response.pause(length=5)
    response.record(
        recording_status_callback="https://en87k9qu34yyd.x.pipedream.net/",
        recording_status_callback_event='completed',
        max_length=3000,
        finish_on_key='*',
    )
    response.hangup()
    return tiniyoml(response)


if __name__ == '__main__':
    app.run()
