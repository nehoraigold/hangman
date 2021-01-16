from game import Game

if __name__ == "__main__":
    is_playing = True
    while is_playing:
        game = Game()
        is_playing = game.play()
