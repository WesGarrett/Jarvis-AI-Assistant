
# J.A.R.V.I.S - Python AI Personal Assistant

.A.R.V.I.S (Just A Rather Very Intelligent System) is a Python-based AI personal assistant designed to assist users with a wide range of tasks using natural language processing (NLP) and artificial intelligence (AI) technologies.
## Features

- **Speech Recognition and Synthesis:** J.A.R.V.I.S can understand spoken commands and respond with synthesized speech, providing a natural interaction experience.
- **OpenAI Integration:** J.A.R.V.I.S leverages the OpenAI API to generate intelligent responses to user queries. This allows J.A.R.V.I.S to provide informative and helpful answers.
- **Website Interaction:** J.A.R.V.I.S can open websites based on user requests. By simply mentioning a website's name, J.A.R.V.I.S will open the corresponding website in the default web browser.
- **Customizable Responses:** The assistant's responses are designed to be concise and to the point. You can customize the responses to suit your preferences or add new responses for specific queries.
- **User-Friendly Interface:** J.A.R.V.I.S provides a user-friendly interface for interacting with the assistant. Users can speak commands or questions, and J.A.R.V.I.S will respond appropriately.


## Installation

**Clone the repository**
```bash
    git clone https://github.com/WesGarrett/Jarvis-AI-Assistant.git
```

**Install dependencies**
```bash
    pip install -r requirements.txt
```

**Set up environment variables**
- Create a '.env' file in the project directory.
- Add your OpenAI API key.
```bash
    OPENAI_API_KEY=your_openai_api_key_here
```

**Run the J.A.R.V.I.S assistant**
```bash
    python jarvis.py
```
- Speak to J.A.R.V.I.S and ask questions or give commands.

- J.A.R.V.I.S will respond verbally and perform tasks based on your requests.

- To exit, say "bye", "exit", or "that's all".



## Configuration
- Adjust the website_mapping dictionary in jarvis.py to add or modify websites that J.A.R.V.I.S can open.
## API Usage
J.A.R.V.I.S utilizes the following APIs:

- **OpenAI API:** Used for generating intelligent responses to user queries. You need to provide your OpenAI API key in the .env file to use this feature.
