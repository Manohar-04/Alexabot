# Alexabot
This project is a voice-activated virtual assistant built using Python. The assistant leverages various libraries to provide a range of functionalities, including:

Speech Recognition: Utilizing the speech_recognition library to capture and process voice commands.
Text-to-Speech: Employing the pyttsx3 library to convert text responses to speech.
YouTube Integration: Using pywhatkit to play videos on YouTube based on voice commands.
Time Query: Providing the current time using the datetime library.
Wikipedia Search: Fetching summaries from Wikipedia for specified queries.
Joke Telling: Generating jokes using the pyjokes library.
Dictionary Look-Up: Retrieving word meanings from an online dictionary API using the requests library.
The assistant is designed to respond to various commands such as playing songs, telling the time, providing information about people, telling jokes, and looking up word meanings. It also includes personalized responses to certain queries. The assistant listens for commands starting with the keyword "alexa" and processes them accordingly.

Features
---------------
Play Songs: Command the assistant to play any song on YouTube.
Current Time: Ask for the current time.
Wikipedia Information: Get summaries of people or topics from Wikipedia.
Humor: Listen to jokes.
Word Meanings: Look up meanings of English words.
Personalized Interaction: Custom responses to specific questions.

How It Works
----------------------
Voice Recognition: The assistant continuously listens for the keyword "alexa" and processes the subsequent command.
Command Processing: Depending on the command, the assistant performs actions like playing a song, fetching information, or telling a joke.
Speech Response: The assistant responds to the user through text-to-speech, making the interaction seamless and engaging.
Getting Started
To run the project, ensure you have the required Python libraries installed:

pip install SpeechRecognition pyttsx3 pywhatkit wikipedia pyjokes requests

Run the run_alexa function in a loop to start the assistant:

while True:
    run_alexa()
This project provides a foundation for building more advanced voice-activated assistants by integrating additional APIs and expanding command capabilities.
