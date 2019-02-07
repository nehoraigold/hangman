class Settings():
    def __init__(self):
        self.opponent_is_friend = self.choose_opponent()

    def choose_opponent(self):
        print("Before we start, would you like to play against the computer or a friend?\n")
        is_valid_choice = False
        COMPUTER_CHOICE = ["computer", "c", "comp"]
        FRIEND_CHOICE = ["friend", "f"]
        while not is_valid_choice:
            comp_or_friend = input(
                'Type either "computer" or "friend" to continue: ')
            if comp_or_friend.lower() in COMPUTER_CHOICE:
                return False
            elif comp_or_friend.lower() in FRIEND_CHOICE:
                return True
