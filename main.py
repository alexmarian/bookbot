def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_word_count(text)
  char_count = get_character_count(text)
  char_count.sort(reverse=True,key=sort_on)
  print(f"--- Begin report of {book_path} ---")
  print(f"{num_words} words found in the document")
  for k in char_count:
    if not k["char"].isalpha():
      continue
    print(f"The '{k["char"]}' character was found {k["num"]} times")


def sort_on(chars):
  return chars["num"]


def get_book_text(path):
  with open(path) as f:
    return f.read()


def get_word_count(text):
  return len(text.split())


def get_character_count(text):
  char_count = {}
  lst = text.lower()
  for c in lst:
    if c in char_count:
      char_count[c] += 1
    else:
      char_count[c] = 1
  char_count_lst = []
  for k,v in char_count.items():
    char_count_lst.append({"char": k, "num": v})
  return char_count_lst


main()
