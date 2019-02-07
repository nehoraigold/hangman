class Turn():
    def __init__(self, answer, guessed_letters, strikes):
        self.answer = answer
        self.guessed_letters = guessed_letters
        self.strikes = strikes
        self.begin_turn()
        self.guess = self.get_valid_guess()

    def get_valid_guess(self):
        self.guess = input("\nYour guess: ").lower()
        while self.guess in self.guessed_letters:
            print("\nYou already guessed that.")
            self.get_valid_guess()
        while self.guess == "" or (len(self.guess) == 1 and not self.guess.isalpha()):
            print("\nPlease guess a letter or phrase.")
            self.get_valid_guess()
        return self.guess

    def begin_turn(self):
        self.strikes.display_hangman()
        self.display_answer()
        if self.strikes.count == self.strikes.LIMIT - 1:
            print("\nCategory: {}".format(self.answer.hint))
        print("\nOther guessed letters: " + self.strikes.display_letters())

    def display_answer(self):
        display = ""
        for c in self.answer.value:
            if c.lower() in self.guessed_letters:
                display += c + " "
            elif c.isalpha() == False and c != " ":
                display += c + " "
            elif c == " ":
                display += "   "
            else:
                display += "_ "
        print(display)
