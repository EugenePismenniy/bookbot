def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def char_stats(text):
    char_dict = {}

    for ch in text:
        
        low_ch = ch.lower()
        if low_ch in char_dict:
            char_dict[low_ch] += 1
        else:
            char_dict[low_ch] = 1

    return char_dict


def sort_on_num(item):
    return item["num"]

def sorted_char_stats(char_stats):

    sorted_stats = []

    for ch in char_stats:
        sorted_stats.append({"char": ch, "num": char_stats[ch]})

    sorted_stats.sort(reverse=True, key=sort_on_num)

    return sorted_stats

