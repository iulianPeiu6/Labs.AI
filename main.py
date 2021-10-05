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


class SolutionStage:

    def __init__(self, n):
        self.couples = []
        self.all_men = []
        self.all_women = []

        for index in range(n):
            current_couple = Couple(index, Constants.left_bank())
            self.couples.insert(index, current_couple)
            self.all_men.insert(index, current_couple.man)
            self.all_women.insert(index, current_couple.woman)

    def show(self):
        for couple in self.couples:
            print(f"{ couple.id }: [{ couple.man } { couple.woman }]")

    def is_final(self):
        for couple in self.couples:
            if couple.man.location == Constants.left_bank():
                return False
            if couple.woman.location == Constants.left_bank():
                return False
        return True

    def move_person(self, person, to_bank):
        if to_bank not in [Constants.left_bank(), Constants.right_bank()]:
            print("ERR\tPlease provide a valid bank name")
            return False
        if person.location == to_bank:
            print("ERR\tCan\'t move a person from a bank to the same bank")
            return False
        person.location = to_bank
        return True

    def is_valid(self):
        for couple in self.couples:
            if couple.man.location == couple.woman.location:
                continue
            if self.are_men_on_location(couple.woman.location):
                return False
        return True

    def are_men_on_location(self, location):
        locations = [i.location for i in self.all_men]
        if location in locations:
            return True
        return False


class Couple:
    def __init__(self, _id, location):
        self.id = _id
        self.man = Person(Constants.man_genre(), location)
        self.woman = Person(Constants.female_genre(), location)


class Person:
    def __init__(self, genre, location):
        self.genre = genre
        self.location = location

    def __str__(self):
        return f"({ self.genre }, { self.location })"


if __name__ == '__main__':
    solution = SolutionStage(2)
    solution.show()
    print(solution.is_valid())
    solution.move_person(solution.couples[0].man, Constants.right_bank())
    print(solution.is_valid())
    solution.show()
    print(solution.is_final())
