class Game(object):
    def __init__(self, player1, player2, stones):
        self.player1 = player1
        self.player2 = player2
        self.stones = stones

    def get_winner(self):
        winner = self.player1 if self.stones % 2 != 0 else self.player2
        return winner

    def play(self):
        leftover = self.stones
        for i in range(1, self.stones):
            leftover -= 2
        self.stones = leftover


def main():
    n = int(input())
    game = Game('Alice', 'Bob', n)
    game.play()
    winner = game.get_winner()
    print(winner)


if __name__ == "__main__":
    main()
