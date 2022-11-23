import random
lives = 3

words = ['пицца', 'змейка', 'зеленый', 'интерактивный', 'ведро', 'отель']
secret_word = random.choice(words)
f = '?'
clue = list(f'{f * len(secret_word)}')
heart_symbol = u'\u2764'

guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

while lives > 0:
    print(clue)
    print(f'жизней осталось: {heart_symbol} {lives}')
    guess = input('Угадай букву или слово целиком: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print('ошибся. минус жизнь')
        lives = lives - 1

if guessed_word_correctly:
    print('Ты выйграл' + secret_word)
else:
    print('Ты проиграл' + secret_word)