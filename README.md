# Gmail Email Agent

A command-line email assistant that uses an OpenRouter chat model and Gmail SMTP to help compose and send emails.

## Requirements

- Python 3
- An OpenRouter API key and a model supported by OpenRouter
- A Gmail account with an app password

## Setup

1. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install the dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory with your credentials and model:

   ```dotenv
   OPENROUTER_API_KEY=your_openrouter_api_key
   MODEL=your_openrouter_model
   GMAIL_USER=your_gmail_address
   GMAIL_APP_PASSWORD=your_gmail_app_password
   ```

   Use a Gmail app password rather than your regular account password. Keep `.env` private and never commit it.

## Run

```powershell
python app.py
```

Enter a message at the prompt to chat with the assistant. Type `quit` or `exit` to end the session.

## Notes

- The conversation state is kept in memory for the current run and is lost when the application exits.
- Email is sent through Gmail's SMTP server (`smtp.gmail.com`, port `587`).
- Keep your API key and Gmail app password secret.
