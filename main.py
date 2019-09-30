from os import name, system
from constants import HANGMEN
from random_word import RandomWords

# Global words creator
r = RandomWords()


def found_word():
    word = r.get_random_word()
    while '-' in word:
        word = r.get_random_word()

    return word.lower()


def finish():
    print('Хотите сыграть еще? (yes/no)')
    answer = input()
    while True:
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            answer = input()


def clean():
    # for windows
    if name == 'nt':
        system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')
    print('В И С Е Л И Ц А\n')


def do_step(mistakes, guessed_letters, word):
    clean()
    print(word)
    mistakes_len = len(mistakes)

    print(HANGMEN[mistakes_len])

    if mistakes_len != 0:
        print('Ошибочные буквы: {}'.format(', '.join(mistakes)))

    letters = []
    for letter in list(word):
        if letter not in guessed_letters:
            letters.append('_')
        else:
            letters.append(letter)

    print(' '.join(letters))
    print('Введите букву:')
    letter = input().lower()
    while letter in guessed_letters or letter in mistakes or len(letter) != 1:
        if letter in guessed_letters:
            print('Вы уже угадали эту букву! Пробуйте снова!')
        elif letter in mistakes:
            print('Вы уже ошиблись на букву! Не повторяйте ошибок!')
        else:
            print('Введите одну букву!')
        letter = input().lower()

    return letter


def is_word_valid(guessed_letters, word):
    is_found = True
    for letter in list(word):
        if letter not in guessed_letters:
            is_found = False

    return is_found


def main():
    clean()
    is_word_guessed = False
    word_to_guess = found_word()
    mistakes = []
    guessed_letters = []

    print(word_to_guess)

    while True:
        if len(mistakes) >= len(HANGMEN) - 1:
            clean()
            print('Вы НЕ угадали слово! На виселицу!')
            print(HANGMEN[6])
            if not finish():
                return

            word_to_guess = found_word()
            mistakes = []
            guessed_letters = []
            continue

        if is_word_valid(guessed_letters, word_to_guess) and not is_word_guessed:
            is_word_guessed = True
            continue

        if is_word_guessed:
            clean()
            print('Да! Секретное слово "{}"! Вы угадали!'.format(word_to_guess))
            if not finish():
                return

            word_to_guess = found_word()
            is_word_guessed = False
            mistakes = []
            guessed_letters = []
            continue

        letter = do_step(mistakes, guessed_letters, word_to_guess)
        if letter in word_to_guess:
            guessed_letters.append(letter)
        else:
            mistakes.append(letter)


# Start the main logic
main()
