import random


class Game(object):
    def __init__(self, num_of_colors, num_of_same_color_balls, num_of_slots):
        self.num_of_colors = num_of_colors
        self.num_of_same_color_balls = num_of_same_color_balls
        self.num_of_slots = num_of_slots
        self.balls_pool = list(range(self.num_of_colors)) * self.num_of_same_color_balls
        self.correct_answer = self.create_random_answer()
        self.answers = []
        self.last_answer = -1
        for slot in range(2 * self.num_of_colors):
            self.answers.append([None] * self.num_of_slots)

    def create_random_answer(self):
        return random.sample(self.balls_pool, self.num_of_slots)

    def last_answer_is_correct(self):
        if self.last_answer == -1:
            print(f"ERROR:\t No answers provided in slots")
            return False
        if self.last_answer > len(self.answers):
            print(f"ERROR:\t Out of answer slots")
            return False

        return self.answers[self.last_answer] == self.correct_answer

    def ended(self):
        if self.last_answer_is_correct():
            return "You won!"
        return "You lost!"

    def create_answer(self, answer):
        self.last_answer += 1
        self.answers[self.last_answer] = list(answer)


if __name__ == '__main__':
    game = Game(8, 4, 4)
    print(game.answers)
    print(game.balls_pool)
    print(game.correct_answer)
    game.create_answer(game.create_random_answer())
    print(game.answers)
    print(game.ended())


