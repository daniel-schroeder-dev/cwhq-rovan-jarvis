import json, logging
from assistant.jarvis import Jarvis

config = {
    "question": [
      "jarvis",
      "wake up jarvis",
      "hello jarvis",
      "hello",
    ],
    "response": [
      "Hello sir, how may I help you?",
      "Greetings sir",
      "My name is Jarvis, how are you?",
    ],
}


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%Y-&m-%d %H:%M:%S'
    )

    Jarvis(logger=logging, config=config)
