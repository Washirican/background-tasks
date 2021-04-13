# --------------------------------------------------------------------------- #
# D. Rodriguez, 2021-04-13, File created.
# --------------------------------------------------------------------------- #
import requests

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())
