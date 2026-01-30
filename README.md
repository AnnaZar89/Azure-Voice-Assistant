# Azure Voice Assistant

A web-based voice assistant built with **Flask** that enables natural conversation with **ChatGPT** using voice commands.

## 🎯 Features

- **Multilingual Conversation**: Support for multiple languages and voice options
- **Intelligent Responses**: Powered by OpenAI's GPT models
- **Speech Recognition**: Real-time voice-to-text conversion (Speech-to-Text)
- **Speech Synthesis**: Text-to-speech conversion with natural-sounding voices (Text-to-Speech)
- **Conversation History**: Maintains context across multiple exchanges
- **Responsive Design**: Optimized for both desktop and mobile devices

## 🗣️ Available Languages and Voices

- **Polish**: Zofia (female), Marek (male)
- **English (US)**: Jenny (female), Andrew (male)
- **English (UK)**: Abbi (female), Ryan (male)
- **French (France)**: Denise (female), Henri (male)
- **French (Canada)**: Sylvie (female), Antoine (male)

## 🛠️ Technology Stack

### Backend
- **Flask**: Web application framework
- **OpenAI API**: Chat completion and AI responses
- **Azure Cognitive Services (Speech)**: Speech recognition and synthesis
- **Python-dotenv**: Environment variable management
- **Pydub & FFmpeg**: Audio format conversion (WebM/Opus to WAV)

### Frontend
- **JavaScript**: Dynamic UI and asynchronous communication
- **HTML/CSS**: Responsive interface with media queries
- **AJAX**: Seamless data updates without page reload

## 📋 Prerequisites

- Python 3.8+
- FFmpeg (for audio conversion)
- Azure subscription (for Speech Services)
- OpenAI API key

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/AnnaZar89/Azure-Voice-Assistant.git
cd Azure-Voice-Assistant
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

**Windows:**
1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract the archive
3. Add the `bin` folder to your system PATH environment variable

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

### 5. Configure Environment Variables

Create a `.env` file in the project root directory with the following variables:

```env
AZURE_SPEECH_KEY=your_azure_speech_key
AZURE_SPEECH_REGION=your_azure_region
OPENAI_API_KEY=your_openai_api_key
```

**How to obtain the keys:**

- **Azure Speech Key**: 
  1. Create an Azure account at [portal.azure.com](https://portal.azure.com)
  2. Create a "Speech" resource
  3. Copy the key and region from the resource's "Keys and Endpoint" section

- **OpenAI API Key**: 
  1. Create an account at [platform.openai.com](https://platform.openai.com/)
  2. Navigate to API keys section
  3. Generate a new API key

**Important**: Add `.env` to your `.gitignore` file to prevent exposing sensitive credentials:
```bash
echo ".env" >> .gitignore
```

## 🚀 Running the Application

### Local Development

```bash
python app.py
```

The application will be available at: `http://127.0.0.1:5000`

### Using Docker

Build the Docker image:
```bash
docker build -t azure-voice-assistant .
```

Run the container:
```bash
docker run -p 5000:5000 --env-file .env azure-voice-assistant
```

## 📁 Project Structure

```
Azure-Voice-Assistant/
│
├── .github/
│   └── workflows/
│       └── main_azure-voice-assistant.yml  # CI/CD workflow
│
├── static/                                  # Frontend assets
│   ├── style.css                            # CSS styles with media queries
│   └── city.png                             # Background image
│
├── templates/                               # HTML templates
│   └── index.html                           # Main user interface
│
├── venv/                                    # Virtual environment
│
├── .dockerignore                            # Docker build exclusions
├── .env                                     # Environment variables (not in repo)
├── .gitignore                               # Git exclusions
├── app.py                                   # Main Flask application
├── Dockerfile                               # Docker image definition
├── README.md                                # Project documentation
├── requirements.txt                         # Python dependencies
└── startup.sh                               # Startup script for Azure Web App
```

## 💻 How It Works

### 1. Voice Selection
User selects their preferred language and voice from the dropdown menu. The application supports 10 different voice options across multiple languages.
<br>
<br>
<img width="650" alt="obraz" src="https://github.com/user-attachments/assets/063631d4-e16c-49ad-9e81-aac49f336c96" />

### 2. Recording
- Click **RECORD** to start voice capture
- Speak your question or command
- Click **STOP** to end recording
- The browser captures audio in WebM format
<br>
<img width="400" alt="obraz" src="https://github.com/user-attachments/assets/4d3ad3d5-6da9-46f5-ad4d-ebc0ad59430d" /> <br>
<br>
<img width="400" alt="obraz" src="https://github.com/user-attachments/assets/de3ffff7-4e24-4c9f-9d6d-5a64a5194a45" /> <br>
<br>
<img width="400" alt="obraz" src="https://github.com/user-attachments/assets/6110632e-62a0-4e06-911a-10a437d57f29" /> <br>


### 3. Speech Recognition
- Click **SEND TO AZURE** to process the recording
- Audio is converted from WebM to WAV format using Pydub and FFmpeg
- Azure Speech Service performs Speech-to-Text conversion
<br>
<img width="400"alt="obraz" src="https://github.com/user-attachments/assets/ba33d5ea-7aa1-4671-b13c-3ce49d5dff1e" />


### 4. AI Processing
- The transcribed text is sent to OpenAI's GPT-3.5-Turbo model
- The AI generates a contextual response based on conversation history
- The response is sent back to the application

### 5. Speech Synthesis
- The AI's text response is sent to Azure Speech Service
- Text-to-Speech conversion occurs using the selected voice
- Audio is returned as WAV format binary data

### 6. Display and Playback
- Both the user's question and AI's response are displayed as text
- Audio player is automatically generated for the AI's response
- The latest response plays automatically
- Full conversation history is maintained and displayed
<br>
<img width="650" alt="obraz" src="https://github.com/user-attachments/assets/27cb63a9-eac5-48be-ba21-335df9f2abb1" />


### 7. History Management
- Click **CLEAR HISTORY** to reset the conversation
- This clears all messages and audio recordings
- Returns to the voice selection screen
- Allows starting a fresh conversation without prior context

## 🌐 Deployment

### Azure Web App Deployment

The application includes CI/CD configuration for automated deployment to Azure Web Apps:

1. The `.github/workflows/main_azure-voice-assistant.yml` file defines the deployment pipeline
2. On push to the main branch, GitHub Actions:
   - Builds a Docker image
   - Pushes it to Azure Container Registry
   - Deploys to Azure Web App

### Docker Benefits

- **Consistency**: Application runs identically across all environments
- **Isolation**: All dependencies packaged together
- **Portability**: Easy deployment to any platform with Docker
- **CI/CD Integration**: Automated build and deployment pipeline

## 🔒 Security Notes

- Never commit `.env` file to version control
- Keep your API keys confidential
- Regularly rotate API keys
- Use Azure Key Vault for production deployments
- Implement rate limiting for API calls

## 🐛 Troubleshooting

### FFmpeg Issues
- Ensure FFmpeg is properly installed and in system PATH
- Test with: `ffmpeg -version`
- On Windows, restart terminal after adding to PATH

### Azure Speech Service Errors
- Verify your subscription key and region are correct
- Check your Azure Speech Service quota and usage
- Ensure your Azure subscription is active

### OpenAI API Errors
- Verify API key is valid and active
- Check your OpenAI account has available credits
- Monitor rate limits and usage

### Microphone Access
- Grant microphone permissions in your browser
- Use HTTPS in production (required for microphone access)
- Check browser console for permission errors

## 📊 Demo

Live demo available at: [Azure Voice Assistant](https://azure-voice-assistant-1801-auh0htamc3hwdxe5.swedencentral-01.azurewebsites.net/)

## 🔗 Links

- **GitHub Repository**: [https://github.com/AnnaZar89/Azure-Voice-Assistant](https://github.com/AnnaZar89/Azure-Voice-Assistant)
- **Azure Speech Documentation**: [https://docs.microsoft.com/azure/cognitive-services/speech-service/](https://docs.microsoft.com/azure/cognitive-services/speech-service/)
- **OpenAI API Documentation**: [https://platform.openai.com/docs](https://platform.openai.com/docs)
- **Detailed project description (in polish)**: [link](https://docs.google.com/document/d/1vZkRJI-x8gmgDVdon7ySAcyJtnYi-Dw1/edit?usp=sharing&ouid=110635265648149776596&rtpof=true&sd=true)

## 📝 License

This project is available for educational and personal use.

## 👤 Author

Anna Zaryczańska
annazar00@gmail.com
