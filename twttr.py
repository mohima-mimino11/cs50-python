"""
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase._summary_
"""
def main():
  user_input = input("Input: ").strip()
  twttr_sentence = [letter for letter in user_input]
  for letter in user_input:
    if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
      twttr_sentence.remove(letter)
  twttr_sentence = "".join(twttr_sentence)
  print(f"Output : {twttr_sentence}")


main()


