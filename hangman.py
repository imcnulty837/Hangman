word_to_guess = "university"
hidden_word = ['*'] * len(word_to_guess)
hidden_word_combined = ""
letters_guessed = list()
tries_to_guess = 5
win_flag = False

while not win_flag:
    hidden_word_combined = ""
    for letter in hidden_word:
        hidden_word_combined += letter

    print("Guessed letters: ")
    for letter in letters_guessed:
        print(letter, end=' ')
    print('')

    print(hidden_word_combined)
    correct_flag = False

    if tries_to_guess is 0:
        print("Sorry! You ran out of tries!")
        print("The word was " + word_to_guess)
        break
    if '*' not in hidden_word:
        print("Congratulations! You won!")
        win_flag = True
        break

    guess = input("Input letter: ")
    while guess in letters_guessed or len(guess) > 1:
        guess = input("Error: Input letter: ")

    for index, letter in enumerate(word_to_guess):
        if letter in guess:
            hidden_word[index] = letter
            correct_flag = True

    letters_guessed.append(guess)
    if correct_flag:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")
        tries_to_guess -= 1