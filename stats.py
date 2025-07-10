def get_book_text (file_path):
    with open(file_path) as f:
        book_contents = f.read()
    return book_contents

def get_num_words(book_path):
    frank_content = get_book_text(book_path)
    num_words = len(frank_content.split())
    return num_words

def get_char_dict(book_path):
    num_chars = {}

    #getting the book content again!
    frank_content = get_book_text(book_path)

    #a nested loop to get the char count, and more loops to check the dict
    for word in frank_content.split():
        lower_case_word = word.lower()
        for char in lower_case_word:
            if char not in num_chars:
                num_chars[char] = 1
            else:
                num_chars[char] += 1

    #the whitespaces added at the end, as they are missing in the earlier list
    num_chars[" "] = len(frank_content.split()) -1

    return num_chars

def get_sorted_list(dict):

    #adding new formatted dicts into the unsorted list
    new_list = []
    for key in dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = dict[key]
        new_list.append(new_dict)
    
    #sorting the list
    def sort_on(list):
        return list["num"]
    
    new_list.sort(key=sort_on, reverse=True)
    return new_list