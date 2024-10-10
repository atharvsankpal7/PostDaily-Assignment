from duckduckgo_search import DDGS


def fetch_news(query):
    results = DDGS().text(query, max_results=1, region="in")

    return results[0] if results else None
