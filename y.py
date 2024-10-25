import random

class Yahtzee:
    def __init__(self):
        self.scorecard = {
            'Ones': 0, 'Twos': 0, 'Threes': 0, 'Fours': 0, 'Fives': 0, 'Sixes': 0,
            'Three of a Kind': 0, 'Four of a Kind': 0, 'Full House': 0,
            'Small Straight': 0, 'Large Straight': 0, 'Yahtzee': 0, 'Chance': 0
        }
        self.dice = [0] * 5
        self.rounds = 13
        self.current_round = 0

    def roll_dice(self, keep=[]):
        for i in range(5):
            if i not in keep:
                self.dice[i] = random.randint(1, 6)
        print(f"Rolled: {self.dice}")

    def score_ones(self):
        return sum(d for d in self.dice if d == 1)

    def score_twos(self):
        return sum(d for d in self.dice if d == 2)

    def score_threes(self):
        return sum(d for d in self.dice if d == 3)

    def score_fours(self):
        return sum(d for d in self.dice if d == 4)

    def score_fives(self):
        return sum(d for d in self.dice if d == 5)

    def score_sixes(self):
        return sum(d for d in self.dice if d == 6)

    def score_three_of_a_kind(self):
        return self.score_n_of_a_kind(3)

    def score_four_of_a_kind(self):
        return self.score_n_of_a_kind(4)

    def score_full_house(self):
        counts = self.counts()
        if len(counts) == 2 and any(v == 3 for v in counts.values()):
            return 25
        return 0

    def score_small_straight(self):
        if any(all(num in self.dice for num in seq) for seq in [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]):
            return 30
        return 0

    def score_large_straight(self):
        if sorted(self.dice) in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]:
            return 40
        return 0

    def score_yahtzee(self):
        if len(set(self.dice)) == 1:
            return 50
        return 0

    def score_chance(self):
        return sum(self.dice)

    def counts(self):
        return {x: self.dice.count(x) for x in set(self.dice)}

    def score_n_of_a_kind(self, n):
        counts = self.counts()
        for value, count in counts.items():
            if count >= n:
                return sum(self.dice)
        return 0

    def play_round(self):
        print(f"\nRound {self.current_round + 1}")
        self.roll_dice()
        keep = input("Enter the indices of dice to keep (0-4) separated by spaces: ")
        keep_indices = list(map(int, keep.split()))
        self.roll_dice(keep_indices)
        self.current_round += 1

        print("Available categories to score:")
        for category in self.scorecard:
            if self.scorecard[category] == 0:
                print(f"{category}: {self.get_score(category)}")

        choice = input("Choose a category to score: ")
        if choice in self.scorecard and self.scorecard[choice] == 0:
            self.scorecard[choice] = self.get_score(choice)
        else:
            print("Invalid choice or category already scored.")

    def get_score(self, category):
        method_name = f"score_{category.lower().replace(' ', '_').replace('-', '_')}"
        if hasattr(self, method_name):
            return getattr(self, method_name)()
        return 0

    def play_game(self):
        while self.current_round < self.rounds:
            self.play_round()

        print("\nFinal Scores:")
        for category, score in self.scorecard.items():
            print(f"{category}: {score}")

        total_score = sum(self.scorecard.values())
        print(f"Total Score: {total_score}")


if __name__ == "__main__":
    game = Yahtzee()
    game.play_game()
