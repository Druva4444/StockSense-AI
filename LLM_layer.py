from transformers import pipeline
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

classifier = pipeline(
    "text-classification",
    model="ProsusAI/finbert"
)

result = classifier("Tesla is going to buy Twitter")
#[{'label', 'score'}]


def get_result(text):
    result = classifier(text)
    return result[0]['label'],result[0]['score']


llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)

analysis_prompt = ChatPromptTemplate.from_messages([
    ("system",
    """You are an experienced Indian equity research analyst specializing in NSE and BSE listed companies.

Analyze only the information in the news article.

Rules:
- Consider ONLY Indian publicly listed companies (NSE/BSE).
- Ignore foreign companies, cryptocurrencies, ETFs, and private companies.
- If no Indian listed company is directly affected, return Company: None.
- Identify the primary Indian company affected.
- Estimate only the short-term market reaction based on the news.
- Base your estimate only on the article. Do not invent facts.
- Use realistic price movement ranges:
  Small: 0% to ±2%
  Moderate: ±2% to ±5%
  Large: >±5% (only for exceptional news)
- If the news is insignificant or uncertain, return:
  Impact: Neutral
  Move: No significant move

Return ONLY in this format:

Company: <Company Name or None>
Ticker: <NSE Symbol or None>
Impact: Bullish | Bearish | Neutral
Move: <e.g. +1% to +3%, -1% to -2%, No significant move>
Time: <1 day | 2-5 days | 1-2 weeks>

Example:

Company: HDFC Bank
Ticker: HDFCBANK
Impact: Bullish
Move: +1% to +3%
Time: 2-5 days
"""),
    ("user", "{article}")
])
analysis_chain = analysis_prompt | llm