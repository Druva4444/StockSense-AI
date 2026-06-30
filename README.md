# 📈 StockSense AI

StockSense AI is an AI-powered stock news analysis system focused on the Indian stock market. It automatically fetches financial news, performs sentiment analysis using **FinBERT**, and leverages **Groq's Llama 3.3 70B** to estimate the short-term impact of financial news on NSE/BSE-listed companies.

## 🚀 Features

- 📰 Fetches the latest financial news using NewsAPI.
- 🤖 Performs financial sentiment analysis using FinBERT.
- 🧠 Uses Groq LLM to identify:
  - Affected company
  - Market impact (Bullish/Bearish/Neutral)
  - Expected short-term price movement
  - Expected time horizon
- 🗄️ Stores articles in PostgreSQL (Neon).
- ⏰ Runs automatically using a scheduler.
- 🇮🇳 Focuses on Indian publicly listed companies (NSE/BSE).

---

# 🛠️ Tech Stack

- Python
- PostgreSQL (Neon)
- NewsAPI
- FinBERT (ProsusAI/finbert)
- LangChain
- Groq API
- Schedule

---

# 📂 Project Structure

```text
.
├── Main.py
├── Scrapper.py
├── Pipeline.py
├── LLM_layer.py
├── DB.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/StockSenseAI.git
cd StockSenseAI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
NEWS_API=your_newsapi_key
GROQ_API_KEY=your_groq_api_key
DATABASE_URL=your_neon_postgresql_connection_string
```

---

# 🗄️ Database Schema

```sql
CREATE TABLE IF NOT EXISTS article (
    id SERIAL PRIMARY KEY,
    title TEXT,
    author TEXT,
    description TEXT,
    content TEXT,
    source TEXT,
    site TEXT
);
```

---

# ▶️ Running the Project

```bash
python Main.py
```

The scheduler will:

1. Fetch the latest stock news.
2. Store articles in PostgreSQL.
3. Perform sentiment analysis using FinBERT.
4. Analyze the news using Groq LLM.
5. Repeat automatically at the configured interval.

---

# 📊 Workflow

```text
            NewsAPI
               │
               ▼
       Fetch Latest News
               │
               ▼
        PostgreSQL (Neon)
               │
               ▼
     FinBERT Sentiment Analysis
               │
               ▼
      Groq LLM Market Analysis
               │
               ▼
   ┌─────────────────────────────┐
   │ Company                     │
   │ Impact                      │
   │ Expected Price Movement     │
   │ Time Horizon                │
   └─────────────────────────────┘
```

---

# 📝 Example Output

```text
Title: HDFC Bank reports strong quarterly earnings

Sentiment: Positive (0.97)

Company: HDFC Bank
Ticker: HDFCBANK
Impact: Bullish
Move: +2% to +4%
Time: 2-5 days
```

---

# 🔮 Future Improvements

- Real-time dashboard
- Stock price integration
- Portfolio tracking
- Email/Telegram notifications
- FastAPI REST API
- Historical sentiment analytics
- Backtesting of news predictions

---

# 📄 License

This project is licensed under the MIT License.
