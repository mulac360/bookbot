def num_words(book_text):
    num_words = book_text.split()
    print(f"Found {len(num_words)} total words")

def char_count(book_text):
    char_count_dict = {}
    for letter in book_text:
        lowercase_letter = letter.lower()
        current_count = char_count_dict.get(lowercase_letter, 0)
        current_count += 1
        char_count_dict[lowercase_letter] = current_count
    return char_count_dict

def sort_on(dict):
    return list(dict.values())[0]

def get_sorted_dict_list(char_dict):
    my_list = []
    for k, v in char_dict.items():
        if k.isalpha():
            my_list.append({k: v})
    
    my_list.sort(reverse=True, key=sort_on)

    return my_list
