import random

words_bank = [
   'secret', 'world', 'forest',
   'table', 'library', 'informatics',
   'olympiad', 'snowboard', 'christmas'
]

secret_word = random.choice(words_bank)
# print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

errors_counter = 0
while True:
   letter = input('Еnter ONE English letter: ').lower()
   if len(letter) != 1:
       continue

   if letter in secret_word:  # hit
       for idx, symbol in enumerate(secret_word):
           if symbol == letter:
               gamer_word[idx] = letter
       if '*' not in gamer_word:  # O(n)
           print('You are winner!')
           break
   else:  # miss
       # errors_counter = errors_counter + 1
       errors_counter += 1
       print('mistakes were made', errors_counter)
       if errors_counter == 8:
           print('You are loser!')
           break

   print(''.join(gamer_word))
