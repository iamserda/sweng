from translate import Translator
from textblob import TextBlob
import pyttsx3
import nltk
import ssl

def dowload_nltk():
    """ Use this to download NLTK.download corpus and other files."""    
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    nltk.download()

# RUN this only if you don't already have the NLTK download files
# download_nltk()
# READ THIS FOR MORE DEETS: 
# "https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed"


audio_engine = pyttsx3.init()
english_text_content =  """The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
"""
translator = Translator(to_lang="fr")
french_text_content = translator.translate(english_text_content)
text_blob_eng = TextBlob(english_text_content)
text_blob_fr = TextBlob(french_text_content)


print(20 * "*")
print(f"English: {english_text_content}")
audio_engine.say(english_text_content)
print(20 * "*", "\n")
print(text_blob_eng.tags)
print(text_blob_eng.noun_phrases)
print(text_blob_eng.sentences)
print(text_blob_fr.tags)
print(text_blob_eng.words, "words-count: ", text_blob_eng.word_counts)
print(text_blob_eng.sentiment)

print("\n", 20 * "*")
print(f"French: {french_text_content}")
audio_engine.say(french_text_content)

print(20 * "*", "\n")
print(text_blob_fr.tags)
print(text_blob_fr.noun_phrases)
print(text_blob_fr.sentences)
print(text_blob_fr.tags)
print(text_blob_fr.words, "words-count: ", text_blob_fr.word_counts)
print(text_blob_fr.sentiment)

audio_engine.runAndWait()
audio_engine.stop()