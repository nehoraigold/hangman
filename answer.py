from getpass import getpass
import random
import csv
from os import path

class Answer():
    def __init__(self, settings):
        self.value, self.hint = self.set_answer_and_hint(settings)
        self.letters = self.set_answer_letters()

    def set_answer_and_hint(self, settings):
        if settings.opponent_is_friend:
            answer = getpass(
                "\nGreat! Without peeking, have your friend enter in their secret phrase now.\n")
            hint = getpass(
                "\nNow, without peeking, have your friend enter in a hint for the secret phrase.\n")
            print(
                "The secret phrase and accompanying hint have been entered successfully.\n")
            return (answer, hint)
        else:
            current_path = '\\'.join(path.abspath(__file__).split('\\')[:-1])
            print(current_path)
            with open(current_path + '\\answers.csv') as csv_file:
                read_csv = csv.reader(csv_file, delimiter=',')
                row = random.choice(list(read_csv))
            answer = row[0]
            hint = row[1]
            print("\nThe secret phrase has been determined by the computer.\n")
            return (answer, hint)

    def set_answer_letters(self):
        answer_letters = []
        for c in self.value:
            if c.isalpha():
                answer_letters.append(c.lower())
        return set(answer_letters)

    def equals(self, guess):
        return guess.lower() == self.lower() or guess.lower() == self.without_punctuation()

    def without_punctuation(self):
        return str(''.join(ch for ch in self.lower() if ch.isalpha() or ch == " "))

    def ends_with_punctuation(self):
        return not self.value[len(self.value) - 1].isalpha()

    def lower(self):
        return self.value.lower()

    def __len__(self):
        return len(self.value)

    def __repr__(self):
        return self.value
