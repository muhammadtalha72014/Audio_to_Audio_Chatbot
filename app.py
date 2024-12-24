# Importing the libraries
import whisper
import os
from gtts import gTTS
import gradio as gr
from groq import Groq

# Load Whisper model for transcription
model = whisper.load_model("base")

#Set up Groq API client
GROQ_API_KEY = "Enter Your GROQ API KEY"
client = Groq(api_key=GROQ_API_KEY)

#Funtion to get LLM Response from Groq
def get_llm_response(user_input):
  chat_completion = client.chat.completions.create(
      messages=[{'role':'user','content':user_input}],
      model='llama3-8b-8192'
  )
  return chat_completion.choices[0].message.content

# Function to convert text to speech using gTTS
def text_to_speech(text, output_audio='output_audio.mp3'):
  tts = gTTS(text)
  tts.save(output_audio)
  return output_audio

#Main Chatbot Function
def chatbot(audio):
  result = model.transcribe(audio)
  user_text = result['text']

  response_text = get_llm_response(user_text)

  output_audio = text_to_speech(response_text)

  return response_text, output_audio

# Gradio Interface for real time interaction
iface = gr.Interface(
    fn=chatbot,
    inputs=gr.Audio(type='filepath'),
    outputs=[gr.Textbox(),gr.Audio(type='filepath')],
    live=True
)

#Launch the app
iface.launch()
