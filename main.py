from googlesearch import search
import webbrowser

query = "mateus bino belode"

lista = list(search(query, tld="co.in", num=10, stop=10, pause=2))

print(lista, len(lista))