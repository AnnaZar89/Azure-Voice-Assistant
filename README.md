# Azure Voice Assistant
**Azure Voice Assistant** to aplikacja webowa stworzona we frameworku **Flask**, która umożliwia konwersację z modelem **ChatGPT** za pomocą głosu.

## Funkcje
- **konwersacja w wielu językach**: wybór języka dla konwersacji 
- **zwracanie inteligentnych odpowiedzi**: generowanie odpowiedzi przez modele OpenAI
- **rozpoznawanie mowy**: przetwarzanie głosu użytkownika na tekst (Speech-To-Text)
- **synteza mowy**: przetwarzanie tekstu zwróconego przez OpenAI na mowę (Text-To-Speech)

## Motywacja i napotkane problemy

## Biblioteki i programy niezbędne do działania projektu
- **Flask**: framework do budowy aplikacji webowych
- **OpenAI Library**: integracja z modelami OpenAI
- **Azure Cognitive Services (speech)**: przetwarzanie mowy
- **Python-dotenv**: zarządzanie zmiennymi środowiskowymi
- **Pydub & FFmpeg**: konwersja formatów audio (WebM/Opus do WAV)

## Konfiguracja zmiennych środowiskowych
Do uruchomienia projektu konieczne jest utworzenie pliku `.env` zawierającego zmienne środowiskowe, 
które umożliwią aplikacji połączenie z chmurą Azure. 
W pliku należy zdefiniować klucz oraz region zasobu Azure Speech, 
a także klucz API do modelu OpenAI, wygenerowany po utworzeniu konta na platformie OpenAI.

```env
AZURE_SPEECH_KEY=twój_klucz_azure
AZURE_SPEECH_REGION=twój_region_azure
OPENAI_API_KEY=twój_klucz_openai
```

## Uruchomienie aplikacji
Po skonfigurowaniu kluczy w pliku `.env`, uruchom serwer komendą:

```env
python main.py
```
Aplikacja będzie dostępna pod adresem: http://127.0.0.1:5000

## Struktura projektu

```text

├── main.py              # Główny plik aplikacji (logika Flask, Azure, OpenAI)
├── .env                 # Plik ze zmiennymi środowiskowymi (klucze API)
├── static/              # Pliki używane przez interfejs użytkownika (style i skrypty)
│   ├── style.css        # Style CSS (w tym Media Queries)
│   └── city.png         # Obraz tła dla aplikacji
└── templates/           # Szablony HTML
    └── index.html       # Główny interfejs użytkownika
```
## Autor i Kontakt

**Autor:** Anna Zaryczańska

**Kontakt:** annazar00@gmail.com









