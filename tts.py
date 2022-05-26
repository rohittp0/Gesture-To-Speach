import pyttsx3
import threading


# To play audio text-to-speech during execution
class TTSThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()
        self.text = ''

    def say(self, text):
        self.text = text

    def run(self):
        tts_engine = pyttsx3.init()
        tts_engine.startLoop(False)
        last = ''
        while True:
            if self.text != last:
                last = self.text
                if self.text == "~exit~":
                    break
                tts_engine.say(self.text)
            else:
                tts_engine.iterate()

        tts_engine.endLoop()
