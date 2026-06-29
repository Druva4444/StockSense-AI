from DB import get_connection
from LLM_layer import get_result
from LLM_layer import analysis_chain
conn =get_connection()
cur = conn.cursor()

def get_article():
    cur.execute("SELECT * FROM article")
    data = cur.fetchall()
    return data

def sentiment_filter(title,content,description):
    [label,score] = get_result(title+content+description)
    return label,score

def job():
    articles = get_article()

    with open("analysis.txt", "a", encoding="utf-8") as f:
        for article in articles:
            title = article[0]
            content = article[3]
            description = article[2]

            label, score = sentiment_filter(title, content, description)

            if label in ("positive", "negative"):
                print(title, label, score)

                response = analysis_chain.invoke({
                    "label": label,
                    "article": f"{title}\n\n{description}\n\n{content}"
                })

                print("Analysis:")
                print(response.content)
                print("-" * 80)

                f.write(f"Title: {title}\n")
                f.write(f"Sentiment: {label} ({score:.4f})\n")
                f.write("Analysis:\n")
                f.write(response.content + "\n")
                f.write("-" * 80 + "\n")

            else:
                print("Nothing")
