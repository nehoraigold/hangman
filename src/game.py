import utils
from settings import Settings
from answer import Answer
from strikes import Strikes
from turn import Turn


def display_introduction():
    utils.clear_screen()
    utils.print_header("HANGMAN")
    print('Welcome to Hangman! The objective of this game is to decode the secret word or phrase by guessing one '
          'letter at a time.')


def explain_rules():
    print("Here's how the game works: Each turn, you may guess a single letter to decode the secret word or "
          "phrase. If the letter you guess occurs in the phrase, we'll fill in all occurrences of that letter for "
          "you. If not, you'll get a strike. Strike out {} times, and it's game over. \n\nIf you think you've "
          "figured out what the secret phrase is before all the letters have been filled in, you may also enter "
          "in the complete answer as your guess. But if you're wrong, it'll count as a strike against you. "
          "Ready?\n".format(str(Strikes.LIMIT)))
    input("Hit enter to continue.")


class Game:
    def __init__(self):
        display_introduction()
        self.settings = Settings()
        self.answer = Answer(self.settings)
        self.strikes = Strikes()
        self.guessed_letters = []
        self.turn_number = 1

    def did_win(self):
        return self.answer.letters.issubset(self.guessed_letters)

    def play(self):
        explain_rules()
        answer_guessed = False
        while not self.did_win() and not self.strikes.limit_reached():
            utils.clear_screen()
            utils.print_header("Turn {}".format(str(self.turn_number)))
            turn = Turn(self.answer, self.guessed_letters, self.strikes)
            if self.answer.equals(turn.guess):
                answer_guessed = True
                break
            self.guessed_letters.append(turn.guess)
            if turn.guess not in self.answer.lower():
                self.strikes.add(turn.guess)
            self.turn_number += 1
        self.end_game(answer_guessed)
        return self.play_again()

    def end_game(self, answer_guessed):
        utils.clear_screen()
        if self.did_win() or answer_guessed:
            title = " YOU WON "
            message = "Correct!"
        else:
            title = "GAME OVER"
            message = "Game over."
        utils.print_header(title)
        self.strikes.display_hangman()
        print("{} The answer was \"{}{}\"".format(message, self.answer,
                                                  "" if self.answer.ends_with_punctuation() else "."))

    def play_again(self):
        again = input("\nWould you like to play again? ").lower()
        yes_answers = ['y', 'yes']
        no_answers = ['n', 'no']
        while again not in yes_answers and again not in no_answers:
            self.play_again()
        return again in yes_answers
