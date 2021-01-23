def digits_to_words(input_string):
    digit_dict = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    digit_string = ''
    for c in input_string:
        if c.isdigit():
            digit_string += digit_dict[ord(c) - ord('0')] + ' '
    return digit_string[:-1]


def to_camel_case(underscore_str):
    _splited = underscore_str.split('_')
    # print("splited=", _splited)
    modified_splited = []
    for i in _splited:
        if i != '':
            modified_splited.append(i)
    # print("modifeid=", modified_splited)
    if modified_splited:
        camelcase_str = modified_splited[0]
    else:
        camelcase_str = ''
    if len(modified_splited) > 1:
        camelcase_str = modified_splited[0].lower()
        for word in modified_splited[1:]:
            for i, v in enumerate(word):
                if i == 0:
                    camelcase_str += v.upper()
                else:
                    camelcase_str += v.lower()
    return camelcase_str

# print(digits_to_words("Zip Code: 19104"))
# print(to_camel_case("to_camel_case"))
# print(to_camel_case("__EXAMPLE__NAME__"))
# print(to_camel_case("alreadyCamel"))
# print(to_camel_case("________"))