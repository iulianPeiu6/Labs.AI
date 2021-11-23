import random
import sys
import ast
from itertools import product


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
        self.combinations = \
            [list(combination) for combination in product(range(self.num_of_colors), repeat=self.num_of_slots)]
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
        return self.check_code(self.answers[self.last_answer], self.correct_answer)

    def play_as_human(self):
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

    def play_as_ai(self):
        print(f"DEBUG:\t Ai started solving...")
        num_of_attempts = 1
        won = False

        current_answer = self.create_random_answer()

        candidate_solutions = list(self.combinations)
        print(f"DEBUG:\t All possible answers: \r\n\t\t {candidate_solutions}")

        while not won:
            self.create_answer(current_answer)
            self.show()
            response = self.check_last_answer()
            if self.last_answer_is_correct():
                return f"Ai won in {num_of_attempts} turns"
            try_remove(candidate_solutions, current_answer)
            try_remove(self.combinations, current_answer)
            self.prune_codes(candidate_solutions, current_answer, response)
            next_guesses = self.minimax(candidate_solutions)
            current_answer = self.get_next_guess(next_guesses, candidate_solutions)
            num_of_attempts += 1

    def prune_codes(self, candidate_solutions, current_answer, response):
        for sol in candidate_solutions:
            if self.check_code(sol, current_answer) != response:
                candidate_solutions.remove(sol)

    def minimax(self, candidate_solutions):
        score_count = {}
        score_map = {}
        for combination in self.combinations:
            for candidate in candidate_solutions:
                score = self.check_code(combination, candidate)
                if score in score_count:
                    score_count[score] += 1
                else:
                    score_count[score] = 1
            score_map[combination.__str__()] = max(score_count.values())
            score_count.clear()
        min_score = min(score_map.values())

        next_guesses = [ast.literal_eval(guess) for guess in score_map if score_map[guess] == min_score]
        return next_guesses

    def get_next_guess(self, next_guesses, candidate_solutions):
        for guess in next_guesses:
            if guess in candidate_solutions:
                return guess
        for guess in next_guesses:
            if guess in self.combinations:
                return guess

    def check_code(self, current_code, code):
        color_matching_result = 0
        position_matching_result = 0

        current_code_cpy = list(current_code)
        code_cpy = list(code)

        for index in range(0, self.num_of_slots):
            if current_code_cpy[index] in code_cpy:
                color_matching_result += 1
                code_cpy.remove(current_code_cpy[index])
            if current_code_cpy[index] == code[index]:
                position_matching_result += 1

        return position_matching_result

    def show(self):
        print(f"INFO:\t Given answers: \r\n\t\t {self.answers}")
        print(f"INFO:\t Balls Matched: {self.check_last_answer()}")


def try_remove(container, element):
    try:
        container.remove(element)
    except ValueError:
        pass


def run_multiple_simulations():
    positive_simulations = 0
    total_simulations = 20
    for simulation in range(0, total_simulations):
        game = Game(6, 4, 4)
        try:
            print(f"DEBUG:\t {game.play_as_ai()}")
            positive_simulations += 1
        except IndexError:
            print(f"DEBUG:\t Ai lost the game")
    print(f"Win rate: {positive_simulations / simulation}")


def run_single_simulation():
    game = Game(6, 4, 4)
    try:
        print(f"DEBUG:\t {game.play_as_ai()}")
    except IndexError:
        print(f"DEBUG:\t Ai lost the game")


if __name__ == '__main__':
    #run_single_simulation()
    run_multiple_simulations()

