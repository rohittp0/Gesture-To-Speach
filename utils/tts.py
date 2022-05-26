import pyttsx3
import threading


# To play audio text-to-speech during execution
class TTSThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.running = True
        self.start()
        self.text = ''

    def say(self, text):
        self.text = text

    def run(self):
        tts_engine = pyttsx3.init()
        tts_engine.startLoop(False)
        last = ''
        while self.running:
            if self.text != last:
                last = self.text
                tts_engine.say(self.text)
            else:
                tts_engine.iterate()

        tts_engine.endLoop()

    def stop(self):
        self.running = False
