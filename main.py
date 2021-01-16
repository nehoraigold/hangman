from game import Game

if __name__ == "__main__":
    play_again = True
    while play_again:
        game = Game()
        game.play()
        play_again = game.play_again()
