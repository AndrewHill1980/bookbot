def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_character = get_num_character(text)
    sorted_character = sort_char(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for char in sorted_character:
        print(f"The '{char['name']}' character was found {char['num']} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]


def sort_char(text):
    
    char_count = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter in char_count:
                char_count[letter] += 1
            else:
                char_count[letter] = 1
    
    char_list = []
    for letter, count in char_count.items():
        char_dict = {"name":letter, "num": count}
        char_list.append(char_dict)        
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    

def get_num_character(text):
    char = {}
    letters = text.lower()
    for letter in letters:
        if letter in char:
            char[letter] = char[letter] + 1
        else:
            char[letter] = 1
    return char


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
