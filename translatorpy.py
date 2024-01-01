from translate import Translator
import pyttsx3
engine=pyttsx3.init()
n='y'
while n=='y':
    text = input("Enter the text to translate: ")
    source= input("Enter the source language: ")
    target= input("Enter the target language: ")

    translator = Translator(from_lang=source, to_lang=target)
    translation = translator.translate(text)


    print("Translated text:", translation)

    engine.say(translation)
    engine.runAndWait()
    n=input("want to translate more words (y/n)=")
