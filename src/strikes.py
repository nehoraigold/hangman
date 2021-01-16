class Strikes:
    LIMIT = 6

    def __init__(self):
        self.count = 0
        self.letters = []

    def add(self, guess):
        self.count += 1
        self.letters.append(guess)

    def display_letters(self):
        return ", ".join(list(set([letter.upper() for letter in self.letters if len(letter) == 1])))

    def limit_reached(self):
        return self.count >= Strikes.LIMIT

    def display_hangman(self):
        if self.count == 1:
            print('_________\n\
|       |\n\
|       O\n\
|\n\
|\n\
|\n\
|_________\n')
        elif self.count == 2:
            print('_________\n\
|       |\n\
|       O\n\
|       |\n\
|\n\
|\n\
|_________\n')
        elif self.count == 3:
            print('_________\n\
|       |\n\
|       O\n\
|       |\n\
|      / \n\
|\n\
|_________\n')
        elif self.count == 4:
            print('_________\n\
|       |\n\
|       O\n\
|      /|\n\
|      /\n\
|\n\
|_________\n')
        elif self.count == 5:
            print('_________\n\
|       |\n\
|       O\n\
|      /|\\\n\
|      / \n\
|\n\
|_________\n')
        elif self.count < 1:
            print('_________\n\
|       |\n\
|\n\
|\n\
|\n\
|\n\
|_________\n')
        else:
            print('________\n\
|       |\n\
|       O\n\
|      /|\\\n\
|      / \\\n\
|\n\
|_________\n')

    def __repr__(self):
        return self.count
