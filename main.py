count_dict = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}


def lower_words(lists):
    lowered_list = []
    for word in lists:
        lowered_word = str(word).lower()
        lowered_list.append(lowered_word)
    return lowered_list
        


def count_letters(string):
    for word in string:
        for letter in word:
            if letter in count_dict:
                count_dict[letter] += 1
    return count_dict

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    new_list = lower_words(words)
    letter_counts = count_letters(new_list)
    sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    print(sorted_counts)