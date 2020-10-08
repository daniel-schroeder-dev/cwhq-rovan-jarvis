import threading
import sys
import speech_recognition as sr
from utils.utils import Utils
from intents.greetings import Greeting


class Jarvis:
    def __init__(self, logger, config):
        self.logger = logger
        self.config = config
        self.speech = sr.Recognizer()
        threading.Thread(target=self.run()).start()

    def read_voice_cmd(self):
        voice_input = ''
        try:
            with sr.Microphone() as source:
                audio = self.speech.listen(source=source, timeout=5, phrase_time_limit=5)
            voice_input = self.speech.recognize_google(audio)
            self.logger.info('User question: {}'.format(voice_input))
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print('Network error.')
        except sr.WaitTimeoutError:
            pass
        except TimeoutError:
            pass

        return voice_input.lower()

    def run(self):
        while True:
            voice_note = self.read_voice_cmd()
            question_match = Utils.match_pattern(voice_note, self.config['question'])
            if question_match:
                response = Utils.choose_random(self.config['response'])
            else:
                response = "Sorry, what was that?"
                Utils.playsound('Intent not found')

            Greeting(self.logger, response).speak()
