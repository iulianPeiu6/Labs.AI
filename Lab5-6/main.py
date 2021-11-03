import random


class Game(object):
    def __init__(self, num_of_colors, num_of_same_color_balls, num_of_slots):
        self.num_of_colors = num_of_colors
        self.num_of_same_color_balls = num_of_same_color_balls
        self.num_of_slots = num_of_slots
        self.balls_pool = list(range(self.num_of_colors)) * self.num_of_same_color_balls
        self.correct_answer = self.create_random_answer()
        print(f"DEBUG:\t Correct answer: {self.correct_answer}")
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

    def check_last_answer(self):
        color_matching_result = 0
        position_matching_result = 0

        correct_answer = list(self.correct_answer)
        answer = list(self.answers[self.last_answer])

        for index in range(0, self.num_of_slots):
            if answer[index] in correct_answer:
                color_matching_result += 1
                correct_answer.remove(answer[index])
            if answer[index] == self.correct_answer[index]:
                position_matching_result += 1

        return color_matching_result, position_matching_result

    def run(self):
        for stage in range(len(self.answers)):
            while True:
                answer = list(map(int, input(f"INFO:\t Insert {self.num_of_slots} balls. Balls: ").split()))
                if len(answer) != self.num_of_slots:
                    print(f"ERROR:\t {self.num_of_slots} balls are required")
                else:
                    self.create_answer(answer)
                    if self.last_answer_is_correct():
                        return "You won!"
                    break
            self.show()
        return "You lost!"

    def show(self):
        print(f"INFO:\t Given answers: \r\n\t\t {self.answers}")
        print(f"INFO:\t Balls Matched: {self.check_last_answer()}")


if __name__ == '__main__':
    game = Game(8, 4, 4)
    print(f"INFO:\t {game.run()}")


