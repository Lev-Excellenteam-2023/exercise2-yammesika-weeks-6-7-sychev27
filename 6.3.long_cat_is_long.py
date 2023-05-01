import string

my_text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""


def count_words(text):
    words = (word.translate(str.maketrans('', '', string.punctuation)) for word in text.split())
    length_of_words = {word: len(word) for word in words}
    return length_of_words


if __name__ == "__main__":
    print(count_words(my_text))
