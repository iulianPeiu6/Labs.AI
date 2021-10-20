import copy
import sys
import random

all_stages = []


class Constants:
    @staticmethod
    def left_bank():
        return "left_bank"

    @staticmethod
    def right_bank():
        return "right_bank"

    @staticmethod
    def female_genre():
        return "F"

    @staticmethod
    def man_genre():
        return "M"


def exists(current_stage):
    for stage in all_stages:
        if stage.equals(current_stage):
            return True
    return False


class Stage:

    def __init__(self, n):
        self.couples = []
        self.people = []
        self.all_men = []
        self.all_women = []
        self.boat_location = Constants.left_bank()

        for index in range(n):
            current_couple = Couple(index, Constants.left_bank())
            self.couples.insert(index, current_couple)
            self.people.insert(index, current_couple.man)
            self.people.insert(index, current_couple.woman)
            self.all_men.insert(index, current_couple.man)
            self.all_women.insert(index, current_couple.woman)

    def equals(self, stage):
        if stage.boat_location != self.boat_location:
            return False;
        for [index, couple] in enumerate(self.couples):
            if couple.man.location != stage.couples[index].man.location:
                return False
            if couple.woman.location != stage.couples[index].woman.location:
                return False
        return True

    @staticmethod
    def show(stage):
        for couple in stage.couples:
            print(f"{ couple.id }: [{ couple.man } { couple.woman }]")

    @staticmethod
    def is_final(stage):
        for person in stage.people:
            if person.location == Constants.left_bank():
                return False
        return True

    @staticmethod
    def move2(stage, first_person, second_person, to_bank):
        print(f"Trying to move person {first_person} to {to_bank}")
        print(f"Trying to move person {second_person} to {to_bank}")

        initial_location = stage.boat_location
        response = stage.move_person(stage, first_person, to_bank)
        if not response:
            return False, stage
        second_response = stage.move_person(stage, second_person, to_bank)
        if not second_response:
            stage.move_person(stage, first_person, initial_location)
            return False, stage
        stage.boat_location = to_bank
        result = copy.deepcopy(stage)
        stage.move_person(stage, first_person, initial_location)
        stage.move_person(stage, second_person, initial_location)
        stage.boat_location = initial_location
        if Stage.is_valid(result):
            return True, result
        del result
        return False, stage

    @staticmethod
    def move1(stage, person, to_bank):
        print(f"Trying to move person {person} to {to_bank}")

        initial_location = stage.boat_location
        response = Stage.move_person(stage, person, to_bank)
        if not response:
            return False, stage
        stage.boat_location = to_bank
        result = copy.deepcopy(stage)
        Stage.move_person(stage, person, initial_location)
        stage.boat_location = initial_location
        if Stage.is_valid(result):
            return True, result
        del result
        return False, stage

    @staticmethod
    def move_person(stage, person, to_bank):
        if to_bank not in [Constants.left_bank(), Constants.right_bank()]:
            print("ERR\tPlease provide a valid bank name")
            return False
        if person.location == to_bank:
            print("ERR\tCan\'t move a person from a bank to the same bank")
            return False
        if stage.boat_location != person.location:
            print("ERR\tCan\'t move a person from a bank where the boat is not present")
            return False
        person.location = to_bank
        return True

    @staticmethod
    def is_valid(stage):
        for couple in stage.couples:
            if couple.man.location == couple.woman.location:
                continue
            if stage.are_men_on_location(stage, couple.woman.location):
                return False
        return True

    @staticmethod
    def are_men_on_location(stage, location):
        locations = [i.location for i in stage.all_men]
        if location in locations:
            return True
        return False

    @staticmethod
    def get_people_on_left_bank(stage):
        return len([person for person in stage.people if person.location == Constants.left_bank()])


class Couple:
    def __init__(self, _id, location):
        self.id = _id
        self.man = Person(_id, Constants.man_genre(), location)
        self.woman = Person(_id, Constants.female_genre(), location)


class Person:
    def __init__(self, _id, genre, location):
        self.id = _id
        self.genre = genre
        self.location = location

    def __str__(self):
        return f"({ self.id }, { self.genre }, { self.location })"


def get_people_on_current_bank(stage):
    people_on_current_bank = []
    for person in stage.people:
        if person.location == stage.boat_location:
            people_on_current_bank.append(person)
    return people_on_current_bank


def solve_via_bk(current_stage, solution):
    if exists(current_stage):
        return
    all_stages.append(current_stage)
    print(solution)
    if Stage.is_final(current_stage):
        print("Found it:")
        print(solution)
        sys.exit()

    destination = Constants.left_bank()
    if current_stage.boat_location == Constants.left_bank():
        destination = Constants.right_bank()

    people_on_current_bank = get_people_on_current_bank(current_stage)
    for first_person in people_on_current_bank:
        for second_person in people_on_current_bank:
            if first_person == second_person:
                continue
            move_result = current_stage.move2(current_stage, first_person, second_person, destination)
            Stage.show(move_result[1])
            if move_result[0]:
                new_solution = list(solution)
                new_solution.append(f"Move person {first_person} to {destination}")
                new_solution.append(f"Move person {second_person} to {destination}")
                solve_via_bk(move_result[1], new_solution)

    people_on_current_bank_2 = get_people_on_current_bank(current_stage)
    for person in people_on_current_bank_2:
        move_result_2 = current_stage.move1(current_stage, person, destination)
        Stage.show(move_result_2[1])
        if move_result_2[0]:
            new_solution = list(solution)
            new_solution.append(f"Move person {person} to {destination}")
            solve_via_bk(move_result_2[1], new_solution)


def solve_via_bfs(current_stage, solution):
    if exists(current_stage):
        return
    all_stages.append(current_stage)
    print(solution)
    if Stage.is_final(current_stage):
        print("Found it:")
        print(solution)
        sys.exit()

    future_stages = []
    future_solutions = []
    destination = Constants.left_bank()
    if current_stage.boat_location == Constants.left_bank():
        destination = Constants.right_bank()

    people_on_current_bank = get_people_on_current_bank(current_stage)
    for first_person in people_on_current_bank:
        for second_person in people_on_current_bank:
            if first_person == second_person:
                continue
            move_result = current_stage.move2(current_stage, first_person, second_person, destination)
            Stage.show(move_result[1])
            if move_result[0]:
                new_solution = list(solution)
                new_solution.append(f"Move person {first_person} to {destination}")
                new_solution.append(f"Move person {second_person} to {destination}")
                future_stages.append(move_result[1])
                future_solutions.append(new_solution)

    people_on_current_bank_2 = get_people_on_current_bank(current_stage)
    for person in people_on_current_bank_2:
        move_result_2 = current_stage.move1(current_stage, person, destination)
        Stage.show(move_result_2[1])
        if move_result_2[0]:
            new_solution_2 = list(solution)
            new_solution_2.append(f"Move person {person} to {destination}")
            future_stages.append(move_result_2[1])
            future_solutions.append(new_solution_2)

    for index in range(len(future_stages)):
        solve_via_bfs(future_stages[index], future_solutions[index])


all_nodes = []  # (stage, solution, depth)


def get_next_node(depth):
    next_node = None
    best_coef = None
    for node in all_nodes:
        if exists(node[0]):
            continue
        h_coef = Stage.get_people_on_left_bank(node[0])
        g_coef = depth
        coef = h_coef + g_coef
        if next_node is None:
            next_node = node
            best_coef = coef
        if coef < best_coef:
            next_node = node
            best_coef = coef
    return next_node


def solve_via_a_star(current_stage, solution, depth):
    if exists(current_stage):
        return
    all_stages.append(current_stage)
    print(depth)
    print(solution)
    if Stage.is_final(current_stage):
        print("Found it:")
        print(solution)
        sys.exit()

    destination = Constants.left_bank()
    if current_stage.boat_location == Constants.left_bank():
        destination = Constants.right_bank()

    people_on_current_bank = get_people_on_current_bank(current_stage)
    for first_person in people_on_current_bank:
        for second_person in people_on_current_bank:
            if first_person == second_person:
                continue
            move_result = current_stage.move2(current_stage, first_person, second_person, destination)
            Stage.show(move_result[1])
            if move_result[0]:
                new_solution = list(solution)
                new_solution.append(f"Move person {first_person} to {destination}")
                new_solution.append(f"Move person {second_person} to {destination}")
                all_nodes.append([move_result[1], new_solution, depth + 1])

    people_on_current_bank_2 = get_people_on_current_bank(current_stage)
    for person in people_on_current_bank_2:
        move_result_2 = current_stage.move1(current_stage, person, destination)
        Stage.show(move_result_2[1])
        if move_result_2[0]:
            new_solution_2 = list(solution)
            new_solution_2.append(f"Move person {person} to {destination}")
            all_nodes.append([move_result_2[1], new_solution_2, depth + 1])

    for node in all_nodes:
        next_node = get_next_node(depth)
        solve_via_a_star(next_node[0], next_node[1], next_node[2])


def try_greedy_right_move(stage):
    for first_person in stage.people:
        for second_person in stage.people:
            if first_person != second_person:
                move_result = Stage.move2(stage, first_person, second_person, Constants.right_bank())
                if move_result[0]:
                    hc_solution.append(f"Move person {first_person} to right bank")
                    hc_solution.append(f"Move person {second_person} to right bank")
                    stage = move_result[1]
                    return True, stage
    return False, stage


def try_not_greedy_right_move(stage):
    for person in stage.people:
        move_result = Stage.move1(stage, person, Constants.right_bank())
        if move_result[0]:
            hc_solution.append(f"Move person {person} to right bank")
            stage = move_result[1]
            return True, stage
    return False, stage


def try_not_greedy_left_move(stage):
    for first_person in stage.people:
        for second_person in stage.people:
            if first_person != second_person:
                move_result = Stage.move2(stage, first_person, second_person, Constants.left_bank())
                if move_result[0]:
                    hc_solution.append(f"Move person {first_person} to left bank")
                    hc_solution.append(f"Move person {second_person} to left bank")
                    stage = move_result[1]
                    return True, stage
    return False, stage


def try_greedy_left_move(stage):
    for person in stage.people:
        move_result = Stage.move1(stage, person, Constants.left_bank())
        if move_result[0]:
            hc_solution.append(f"Move person {person} to left bank")
            stage = move_result[1]
            return True, stage
    return False, stage


def next_neighbour(stage):
    new_stage = copy.deepcopy(stage)

    # first improvement - first good move
    # best improvement = best move
    # iterate in all moves - get first good move/best move
    # good move? - at least one person is moved to the right

    shuffled_people = list(new_stage.people)
    random.shuffle(shuffled_people)
    new_stage.people = shuffled_people

    move_greedy_right_result = try_greedy_right_move(new_stage)
    if not move_greedy_right_result[0]:
        new_stage = try_not_greedy_right_move(new_stage)[1]
    else:
        new_stage = move_greedy_right_result[1]

    Stage.show(new_stage)
    print(hc_solution)
    if Stage.is_final(new_stage):
        return new_stage

    move_greedy_left_result = try_greedy_left_move(new_stage)
    if not move_greedy_left_result[0]:
        new_stage = try_not_greedy_left_move(new_stage)[1]
    else:
        new_stage = move_greedy_left_result[1]

    Stage.show(new_stage)
    print(hc_solution)
    return new_stage


hc_solution = []


def solve_via_hc(starting_stage):
    num_of_restarts = 1

    for iteration in range(num_of_restarts):
        stage = copy.deepcopy(starting_stage)
        while stage is not None:
            if Stage.is_final(stage):
                print(hc_solution)
                return hc_solution
            stage = next_neighbour(stage)
            Stage.show(stage)
            #print(hc_solution)


if __name__ == '__main__':
    n = int(input("n="))
    problem = Stage(n)
    Stage.show(problem)
    method = input("method= ")
    if method == "bk":
        solve_via_bfs(problem, [])
    elif method == "bfs":
        solve_via_bfs(problem, [])
    elif method == "a*":
        solve_via_a_star(problem, [], 0)
    else:
        solve_via_hc(problem)
