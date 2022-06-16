STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def make_lowercase(read_file):
    lowercase_version = []
    for word in read_file:
        lowercase = word.lower()
        lowercase_version.append(lowercase)
        # print(lowercase)
    # print (lowercase_version)
    return lowercase_version

def remove_punctuations(lowercase_version):
    line_list = []
    for line in lowercase_version:
        no_period = line.replace(".", "")
        no_comma = no_period.replace (",", "")
        no_colon = no_comma.replace (":", "")
        no_question = no_colon.replace ("?", "")
        line_list.append (no_question)
    return line_list

def add_to_dictionary(remove_punctuations):
    word_dictionary = {}
    word_list = []
    for line in remove_punctuations:
        for word in line.split ():
            word_list.append(word)
    for word in word_list:
        word_dictionary[word] = word_list.count(word)
    return word_dictionary

def remove_stop_words (add_to_dictionary):
    new_dictionary = add_to_dictionary.copy()
    for word_key in add_to_dictionary.keys():
        if word_key in STOP_WORDS:
            del new_dictionary [word_key]
    print ("HELLO", new_dictionary)
    return new_dictionary

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    print (f'Your file is:{file}')
    with open (file) as open_file:
            read_file = open_file.readlines()
    lowercase_version = make_lowercase(read_file)
    print_all = remove_punctuations(lowercase_version)
    word_dict = add_to_dictionary(print_all)
    last_one = remove_stop_words(word_dict)
    # print (last_one)

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
