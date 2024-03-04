from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import OpenAI
from gtts import gTTS
from playsound import playsound
from pathlib import Path
import speech_recognition as sr
import webbrowser

load_dotenv()

llm = OpenAI(temperature=0)

conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=ConversationBufferMemory()
)

conversation.predict(
    input="Hello, you are Jarvis, an AI assistant designed to help with tasks in a respectful and efficient manner and you are to give short, precise to the point answers."
)


website_mapping = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "chatGPT": "https://chat.openai.com/"
    
}

def get_response(user_query, max_chars=100):
    temp = " .Make sure to provide answers in 50-100 words"
    response = conversation.predict(input=user_query + temp)

    
    for website_name, website_url in website_mapping.items():
        if website_name in user_query.lower():
            webbrowser.open(website_url)
            response = f"Opening {website_name} website."
            break

    return response[:max_chars]


def text_to_speech(text, output_path):
    tts = gTTS(text=text, lang='en')
    tts.save(output_path)

def stream_audio(response):
    speech_file_path = Path(__file__).parent / "speech.mp3"
    text_to_speech(response, speech_file_path)
    playsound(str(speech_file_path))

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('recognizing...')
        query = r.recognize_google(audio, language='en-us')
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return None
    except sr.RequestError as e:
        print(f"Sorry, there was an issue with the request: {e}")
        return None
    return query

def main():
    stream_audio('Hello I am Jarvis, your AI assistant. How may I assist you today?')

    while True:
        query = take_command()
        if not query:
            continue
        if 'bye' in query or 'exit' in query or "that's all" in query:
            break
        response = get_response(query)
        stream_audio(response)

if __name__ == "__main__":
    main()