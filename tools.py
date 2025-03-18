from googlesearch import search
import webbrowser

def searchGoogle(query: str) -> str:
    query = f"cifraclub/{query}"
    return list(search(query, tld="com", num=10, stop=10, pause=2))[0]

def openBrowser(url: str) -> None:
    webbrowser.open(url)