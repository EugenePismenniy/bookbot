
import sys
from stats import get_book_text, count_words, char_stats, sorted_char_stats

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    path_to_book = sys.argv[1]

    text = get_book_text(path_to_book)
    num_words = count_words(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    chars_dict = char_stats(text)
    sorted_chars = sorted_char_stats(chars_dict)

    for ch in sorted_chars:
        print(f"{ch['char']}: {ch['num']}")

    print("============= END ===============")

main()