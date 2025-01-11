def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    l_text = text.lower()
    dict = {}
    for char in "abcdefghijklmnopqrstuvwxyz":
        counter = 0
        for char_text in l_text:
            if char == char_text:
                counter += 1
        dict[char] = counter
    return dict  


def sort_dict(dict):
    sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_dict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_used = count_characters(text)
    sorted_char_used = sort_dict(char_used)
    print("--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the documents\n\n")
    
    for c in sorted_char_used:
        print(f"The {c[0]} character was found {c[1]} times")
    
    print("--- End report ---")
            
main()