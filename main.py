import random

words = ('rabbit', 'cat', 'elephant', 'mouse', 'parrot')

hangman_art = {
    0: ("  ", "  ", "  "),
    1: (" o ", "  ", "  "),
    2: (" o ", " | ", "  "),
    3: (" o ", " /| ", "  "),
    4: (" o ", "/|\\", "  "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\")
}

def display_man(wrong_guess):
    for line in hangman_art[wrong_guess]:
        print(line)

def display_hint(hint):
    print("Word:", " ".join(hint))

def display_answer(answer):
    print("The word was:", answer)

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guess = 0
    guessed_letters = set()
    max_wrong = 6

    while wrong_guess < max_wrong and "_" in hint:
        display_man(wrong_guess)
        display_hint(hint)

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter ONE letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guess += 1
            print("Wrong guess!")

        print()

    display_man(wrong_guess)
    display_hint(hint)

    if "_" not in hint:
        print("🎉 You won!")
    else:
        print("💀 You lost!")
        display_answer(answer)

if __name__ == "__main__":
    main()
