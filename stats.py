
def get_num_words(file_contents):
    num_words = len(file_contents.split())
    return num_words

def get_letter_frequency(file_contents):
    letter_frequency = {}
    for char in file_contents:
        if char.lower() not in letter_frequency:
            letter_frequency[char.lower()] = 1
        else:
            letter_frequency[char.lower()] += 1
    return letter_frequency

                         
def sort_on(items):
    return items["num"]

def sorted_dictionary(letter_frequency):
    new_list = list(letter_frequency.items())
    newer_list = []
    for item in new_list:
        new_dict = {}
        new_dict["char"] = item[0]
        new_dict["num"] = item[1]
        newer_list.append(new_dict)
    newer_list.sort(reverse=True, key=sort_on)
    return newer_list
