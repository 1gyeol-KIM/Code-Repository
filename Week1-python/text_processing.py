
def normalize(input_string):
    words = input_string.split()
    normalized_string = ''
    for word in words:
        normalized_string += word.lower() + ' '
    return normalized_string[:-1]


def no_vowels(input_string):
    word_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    no_vowel_string = ''
    for word in input_string:
        if word not in word_set:
            no_vowel_string += word
    return no_vowel_string
