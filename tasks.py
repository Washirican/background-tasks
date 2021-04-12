# --------------------------------------------------------------------------- #
# D. Rodriguez, 2021-04-11, File created.
# --------------------------------------------------------------------------- #
import requests


def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())


def sum_numbers_from_string(string):
    numbers = []
    for each_character in string:
        if each_character.isdigit():
            numbers.append(int(each_character))
    total = 0
    for each_number in numbers:
        total = total + each_number

    return total
