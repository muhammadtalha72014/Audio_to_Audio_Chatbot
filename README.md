# Audio_to_Audio_Chatbot

## Description
This project builds an interactive question-answering system that takes audio input, processes it through a large language model (LLM) via the Groq API, and returns the answer in audio format. The interface is developed using Gradio for ease of use and accessibility.

## Features
- Audio Input: Users can ask questions by speaking directly to the interface.

- Whisper Integration: Converts the audio input into text using OpenAI's Whisper model.

- LLM with Groq API: The transcribed text is processed by a large language model via Groq's API to generate accurate responses.

- Audio Output: The generated response is converted back to audio and presented to the user.

- Gradio Interface: A user-friendly web interface created using Gradio for seamless interaction.

## Installation

- Clone the repository:

```http
git clone https://github.com/muhammadtalha72014/Audio_to_Audio_Chatbot
cd  Audio_to_Audio_Chatbot
```
- Install the required dependencies:

```http
pip install -r requirements.txt
```
- Setup your GROQ API KEY:

```http
export GROQ_API_KEY='your_api_key_here'  
```
## Output

![image](https://github.com/user-attachments/assets/0f950cca-5623-41b5-95e4-70e241a35f58)
