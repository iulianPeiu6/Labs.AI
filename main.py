import copy
import sys


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


def solve_via_bk(current_stage, solution):
    print(solution)
    if Stage.is_final(current_stage):
        print("am gasit o taticule")
        print(solution)
        sys.exit()
    if current_stage.boat_location == Constants.left_bank():
        people_on_left_bank = []
        for person in current_stage.people:
            if person.location == Constants.left_bank():
                people_on_left_bank.append(person)
        for first_person in people_on_left_bank:
            for second_person in people_on_left_bank:
                if first_person == second_person:
                    continue
                move_result = current_stage.move2(current_stage, first_person, second_person, Constants.right_bank())
                Stage.show(move_result[1])
                if move_result[0]:
                    new_solution = list(solution)
                    new_solution.append(f"Move person { first_person } to { Constants.right_bank() }")
                    new_solution.append(f"Move person { second_person } to { Constants.right_bank() }")
                    solve_via_bk(move_result[1], new_solution)
    else:
        people_on_right_bank = []
        for person in current_stage.people:
            if person.location == Constants.right_bank():
                people_on_right_bank.append(person)
        for person in people_on_right_bank:
            move_result = current_stage.move1(current_stage, person, Constants.left_bank())
            Stage.show(move_result[1])
            if move_result[0]:
                new_solution = list(solution)
                new_solution.append(f"Move person { person } to {Constants.left_bank()}")
                solve_via_bk(move_result[1], new_solution)


if __name__ == '__main__':
    problem = Stage(3)
    Stage.show(problem)
    solve_via_bk(problem, [])
