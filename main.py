import sys
from stats import get_num_words, get_char_dict, get_sorted_list

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #decorating the output below

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")

    num_words = get_num_words(sys.argv[1])
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_dict = get_char_dict(sys.argv[1])
    sorted_list = get_sorted_list(char_dict)
    for char in sorted_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")

main()
