from operator import itemgetter

def main():
    print(f"--- Begin report of /books/frankenstein.txt ---")
    text =  get_book_text("./books/frankenstein.txt")

    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    count_chars = get_num_characters(text)
    sorted_chars_dict = dict(sorted(count_chars.items(), key=itemgetter(1), reverse=True))

    for alpha, num in sorted_chars_dict.items():
        print(f"The '{alpha}' character was found {num} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    count_dict = dict()
    for s in text.lower():
        if s.isalpha():
            if s in count_dict:
                count_dict[s] += 1
            else:
                count_dict[s] = 1
    return count_dict

main()
