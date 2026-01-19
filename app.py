import json
from flask import Flask, render_template, request, jsonify, send_file
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
import os
import io
from openai import OpenAI
from pydub import AudioSegment


load_dotenv()

app = Flask(__name__)

SPEECH_KEY = os.getenv('AZURE_SPEECH_KEY')
SPEECH_REGION = os.getenv('AZURE_SPEECH_REGION')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

model = "gpt-3.5-turbo"
voiceToChoose = {
    "plf": "pl-PL-ZofiaNeural",
    "plm": "pl-PL-MarekNeural",
    "enf": "en-US-JennyNeural",
    "enm": "en-US-AndrewNeural",
    "engf": "en-GB-AbbiNeural",
    "engm": "en-GB-RyanNeural",
    "frf": "fr-FR-DeniseNeural",
    "frm": "fr-FR-HenriNeural",
    "frcf": "fr-CA-SylvieNeural",
    "frcm": "fr-CA-AntoineNeural"
}

language = {
    "plf": "pl-PL",
    "plm": "pl-PL",
    "enf": "en-US",
    "enm": "en-US",
    "engf": "en-GB",
    "engm": "en-GB",
    "frf": "fr-FR",
    "frm": "fr-FR",
    "frcf": "fr-CA",
    "frcm": "fr-CA"
}

error_translations = {
    "pl": {
        "azure_error": "Nie rozpoznano mowy (Azure)",
        "openai_error": "Błąd OpenAI: {e}",
    },
    "en": {
        "azure_error": "Speech not recognized (Azure)",
        "openai_error": "OpenAI Error: {e}",
    },
    "fr": {
        "azure_error": "Parole non reconnue (Azure)",
        "openai_error": "Erreur OpenAI : {e}",
    }
}


current_voice_key = "plf"
current_voice_name = "pl-PL-ZofiaNeural"
voice_name_key = {}

@app.route('/')
def index():
    return render_template('index.html', history_json="[]")

@app.route('/choosingVoice', methods=['POST'])
def choosing_voice():
    global current_voice_key
    selected = request.form.get('voiceChoice')
    if selected in voiceToChoose:
        current_voice_key = selected
        global current_voice_name
        current_voice_name = voiceToChoose.get(selected,"pl-PL-ZofiaNeural")
        voice_name_key["current_voice_key"] = current_voice_key
        voice_name_key["current_voice_name"] = current_voice_name
    return voice_name_key

@app.route('/recognize', methods=['POST'])
def recognize():
    audio_file = request.files['audio']
    audio_data = audio_file.read()
    audio = AudioSegment.from_file(io.BytesIO(audio_data))
    audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
    wav_buffer = io.BytesIO()
    audio.export(wav_buffer, format='wav')
    wav_data = wav_buffer.getvalue()
    speech_config = speechsdk.SpeechConfig(SPEECH_KEY, SPEECH_REGION)
    lang = language.get(current_voice_key, "pl-PL")
    speech_config.speech_recognition_language = lang
    stream = speechsdk.audio.PushAudioInputStream()
    audio_config = speechsdk.audio.AudioConfig(stream=stream)
    recognizer = speechsdk.SpeechRecognizer(speech_config, audio_config)
    stream.write(wav_data)
    stream.close()
    result = recognizer.recognize_once()
    lang_code = current_voice_key[:2]

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        user_text = result.text

        try:
            conversation_history_json = request.form.get('history', '[]')
            conversation_history = json.loads(conversation_history_json)
            conversation_history.append({"role": "user", "content": user_text})

            response = client.chat.completions.create(
                model=model,
                messages=conversation_history,
                temperature=0.7
            )

            chat_answer = response.choices[0].message.content
            conversation_history.append({"role": "assistant", "content": chat_answer})
            history_json = json.dumps(conversation_history)

            return jsonify({
                'success': True,
                'recognized_text': user_text,
                'chat_response': chat_answer,
                'history_json': history_json
            })

        except Exception as e:
            return jsonify({'success': False, 'error': error_translations[lang_code]['openai_error'].format(e=str(e))})
    return jsonify({'success': False, 'error': error_translations[lang_code]['azure_error']})


@app.route('/synthesize', methods=['POST'])
def synthesize():
    text = request.form.get('text')
    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        region=SPEECH_REGION
    )
    chosen_voice = voiceToChoose.get(current_voice_key, "pl-PL-ZofiaNeural")
    speech_config.speech_synthesis_voice_name = chosen_voice
    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=None
    )

    result = synthesizer.speak_text_async(text).get()

    return send_file(
        io.BytesIO(result.audio_data),
        mimetype='audio/wav',
        as_attachment=False,
        download_name='speech.wav'
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
