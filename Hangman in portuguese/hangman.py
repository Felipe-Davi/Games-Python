import random
from words import words
from hangmanvisual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()
print('-----------------------------------------------------------------------------------------------')

print ('TEMA: OBJETO')

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7


    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('Você possui', lives, 'vidas, e você usou estas letras: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Digite uma letra: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nA letra,', user_letter, 'não está na palavra.')

        elif user_letter in used_letters:
            print('\nTente outra letra.')

        else:
            print('\nLetra inválda.')


    if lives == 0:
        print(lives_visual_dict[lives])
        print('Você matou o homem,:( A palavra correta era: ', word)
    else:
        print('Parabéns, você encontrou a palavra: ', word, '!!')


if __name__ == '__main__':
    hangman()