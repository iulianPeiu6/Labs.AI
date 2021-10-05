class Constants:
    @staticmethod
    def left_side_land():
        return "left_land"

    @staticmethod
    def right_side_land():
        return "right_land"

    @staticmethod
    def female_genre():
        return "F"

    @staticmethod
    def man_genre():
        return "M"


class SolutionStage:
    def __init__(self, n):
        self.couples = []
        for index in range(n):
            self.couples.insert(index, Couple(index, Constants.left_side_land()))

    def print_current_solution(self):
        for couple in self.couples:
            print(f"{ couple.id }: [{ couple.man } { couple.woman }]")

    def solution_is_final(self):
        for couple in self.couples:
            if couple.man.location == Constants.left_side_land():
                return False
            if couple.woman.location == Constants.left_side_land():
                return False
        return True


class Couple:
    def __init__(self, id, location):
        self.id = id
        self.man = Person(Constants.man_genre(), location)
        self.woman = Person(Constants.female_genre(), location)


class Person:
    def __init__(self, genre, location):
        self.genre = genre
        self.location = location

    def __str__(self):
        return f"({ self.genre }, { self.location })"


if __name__ == '__main__':
    solution = SolutionStage(4)
    solution.print_current_solution()
    print(solution.solution_is_final())
