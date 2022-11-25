import speech_recognition as sr
from gtts import gTTS
import pyperclip

comandos = ["copiar"]


class Microphone:

    @staticmethod
    def watch():
        microphone = sr.Recognizer()

        with sr.Microphone() as source:

            microphone.adjust_for_ambient_noise(source)
            audio = microphone.listen(source)

            try:

                frase = microphone.recognize_google(audio, language='pt-BR')

                return frase

            except sr.UnknownValueError:
                return False


class ComanderCenter:

    def __init__(self, comandoT):
        print("Iniciando Comander")
        self.comando = comandoT

    def __contains__(self, substring):
        if substring in self.comando:
            return True
        else:
            return False

    def reconhecer(self):
        print(self.comando.split(" "))
        for cmd in comandos:
            if cmd in self.comando.split(" "):
                pyperclip.copy(self.comando)
                print("Comando copiado Comander")


def __main__():
    ComanderCenter(Microphone.watch()).reconhecer()


if __name__ == '__main__':
    __main__()
