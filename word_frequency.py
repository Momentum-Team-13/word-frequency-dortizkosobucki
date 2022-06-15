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
    for line in lowercase_version:
        no_period = line.replace(".", "")
        # no_comma = no_period.remove(",")
        print (line)

    # no_punctuations = []
    # expression = [".", ",", "!", "?"]
    # no_punctuations = l.remove(".")
    # print (no_punctuations)
    # for sentence in lowercase_version:
    #     for 
    #     no_punctuations.append(lowercase_version)
    #     print (no_punctuations)
    #     # expression = [".", ",", "!", "?"]
    #     # no_punctuations = del [. : , : !]
    #     # print (no_punctuations)



def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    print (f'Your file is:{file}')
    with open (file) as open_file:
            read_file = open_file.readlines()
    lowercase_version = make_lowercase(read_file)
    remove_punctuations(lowercase_version)
    print (lowercase_version)



# - remove punctuation
# - normalize all words to lowercase
# - remove "stop words" -- words used so frequently they are ignored
# - go through the file word by word and keep a count of how often each word is used

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
