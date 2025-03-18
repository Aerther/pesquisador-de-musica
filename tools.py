from googlesearch import search
import webbrowser

def searchGoogle(query: str) -> str:
    query = f"cifraclub/{query}"
    return list(search(query, tld="com", stop=1, pause=0))[0]

def openBrowser(url: str) -> None:
    webbrowser.open(url)