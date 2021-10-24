import copy
import sys


class Map(object):
    def __init__(self, _neighbours_mapping, _colors_mapping):

        self.neighbours_mapping = _neighbours_mapping
        self.all_locations = set(self.neighbours_mapping.keys())
        self.colors_mapping = _colors_mapping
        self.answer = dict(self.colors_mapping)
        self.visited = set()

    def forward_checking(self, location):
        for neighbour in self.neighbours_mapping[location]:
            self.colors_mapping[neighbour] = self.colors_mapping[neighbour] - self.colors_mapping[location]

    def is_not_consistent(self):
        for location in self.colors_mapping:
            if len(self.colors_mapping[location]) == 0:
                return True
        for location in self.neighbours_mapping:
            for neighbour in self.neighbours_mapping[location]:
                if location != neighbour:
                    if location in self.visited and neighbour in self.visited:
                        if self.colors_mapping[location] <= self.colors_mapping[neighbour] or self.colors_mapping[location] >= self.colors_mapping[neighbour]:
                            return True
        return False

    def get_next_location(self):
        next_location = None
        unvisited_location = self.all_locations - self.visited
        for location in unvisited_location:
            if next_location is None:
                next_location = location
                continue
            if len(self.colors_mapping[location]) < len(self.colors_mapping[next_location]):
                next_location = location

        return next_location

    def __str__(self) -> str:
        return self.colors_mapping.__str__()


def solve_fc(map):
    for location in map.colors_mapping:
        current_colors = map.colors_mapping[location]
        if location in map.visited:
            continue
        map.visited.add(location)

        if map.is_not_consistent():
            print(f"DEBUG:\t Inconsistent solution:{map} ")
            return

        if len(map.visited) == len(map.colors_mapping.keys()):
            print(f"INFO:\t Solution found: {map}")
            sys.exit()

        for color in current_colors:
            next_map = copy.deepcopy(map)
            next_map.colors_mapping[location] = {color}
            print(f"DEBUG:\t Checking color {color} for location {location} in map {next_map}")
            next_map.forward_checking(location)
            solve_fc(next_map)


def solve_fc_mrv(map):
    while True:
        location = map.get_next_location()
        if location is None:
            break
        current_colors = map.colors_mapping[location]
        if location in map.visited:
            continue
        map.visited.add(location)

        if map.is_not_consistent():
            print(f"DEBUG:\t Inconsistent solution:{map} ")
            return

        if len(map.visited) == len(map.colors_mapping.keys()):
            print(f"INFO:\t Solution found: {map}")
            sys.exit()

        for color in current_colors:
            next_map = copy.deepcopy(map)
            next_map.colors_mapping[location] = {color}
            print(f"DEBUG:\t Checking color {color} for location {location} in map {next_map}")
            next_map.forward_checking(location)
            solve_fc(next_map)


def run_test_fc_1():
    location_neighbours_map = {
        "SA": {"NSW", "V"},
        "NSW": {"SA", "V"},
        "V": {"SA", "NSW"}

    }

    location_colors_map = {
        "SA": {"red", "blue", "green"},
        "NSW": {"red", "blue", "green"},
        "V": {"red", "blue", "green"}
    }
    problem = Map(location_neighbours_map, location_colors_map)

    solve_fc(problem)


def run_test_fc_2():
    location_neighbours_map = {
        "T": {"V"},
        "WA": {"NT", "SA"},
        "NT": {"WA", "Q", "SA"},
        "SA": {"WA", "NT", "Q", "NSW", "V"},
        "Q": {"NT", "SA", "NSW"},
        "NSW": {"Q", "SA", "V"},
        "V": {"SA", "NSW", "T"}

    }

    location_colors_map = {
        "WA": {"red", "blue", "green"},
        "NT": {"red", "blue", "green"},
        "SA": {"red", "blue", "green"},
        "Q": {"red", "blue", "green"},
        "NSW": {"red", "blue", "green"},
        "V": {"red", "blue", "green"},
        "T": {"red", "blue", "green"}
    }
    problem = Map(location_neighbours_map, location_colors_map)

    solve_fc(problem)


def run_test_fc_3():
    location_neighbours_map = {
        "T": {"V"},
        "WA": {"NT", "SA"},
        "NT": {"WA", "Q", "SA"},
        "SA": {"WA", "NT", "Q", "NSW", "V"},
        "Q": {"NT", "SA", "NSW"},
        "NSW": {"Q", "SA", "V"},
        "V": {"SA", "NSW", "T"}

    }

    location_colors_map = {
        "WA": {"red"},
        "NT": {"red", "blue", "green"},
        "SA": {"red", "blue", "green"},
        "Q": {"green"},
        "NSW": {"red", "blue", "green"},
        "V": {"red", "blue", "green"},
        "T": {"red", "blue", "green"}
    }
    problem = Map(location_neighbours_map, location_colors_map)

    solve_fc(problem)


def run_test_fc_mrv_1():
    location_neighbours_map = {
        "SA": {"NSW", "V"},
        "NSW": {"SA", "V"},
        "V": {"SA", "NSW"}

    }

    location_colors_map = {
        "SA": {"red", "blue", "green"},
        "NSW": {"red", "blue", "green"},
        "V": {"red", "blue", "green"}
    }
    problem = Map(location_neighbours_map, location_colors_map)

    solve_fc_mrv(problem)


def run_test_fc_mrv_2():
    location_neighbours_map = {
        "T": {"V"},
        "WA": {"NT", "SA"},
        "NT": {"WA", "Q", "SA"},
        "SA": {"WA", "NT", "Q", "NSW", "V"},
        "Q": {"NT", "SA", "NSW"},
        "NSW": {"Q", "SA", "V"},
        "V": {"SA", "NSW", "T"}

    }

    location_colors_map = {
        "WA": {"red", "blue", "green"},
        "NT": {"red", "blue", "green"},
        "SA": {"red", "blue", "green"},
        "Q": {"red", "blue", "green"},
        "NSW": {"red", "blue", "green"},
        "V": {"red", "blue", "green"},
        "T": {"red", "blue", "green"}
    }
    problem = Map(location_neighbours_map, location_colors_map)

    solve_fc_mrv(problem)


def run_test_fc_mrv_3():
    location_neighbours_map = {
        "T": {"V"},
        "WA": {"NT", "SA"},
        "NT": {"WA", "Q", "SA"},
        "SA": {"WA", "NT", "Q", "NSW", "V"},
        "Q": {"NT", "SA", "NSW"},
        "NSW": {"Q", "SA", "V"},
        "V": {"SA", "NSW", "T"}

    }

    location_colors_map = {
        "WA": {"red"},
        "NT": {"red", "blue", "green"},
        "SA": {"red", "blue", "green"},
        "Q": {"green"},
        "NSW": {"red", "blue", "green"},
        "V": {"red", "blue", "green"},
        "T": {"red", "blue", "green"}
    }
    problem = Map(location_neighbours_map, location_colors_map)

    solve_fc_mrv(problem)

if __name__ == '__main__':
    #run_test_fc_1()
    #run_test_fc_2()
    #run_test_fc_3()

    #run_test_fc_mrv_1()
    #run_test_fc_mrv_2()
    run_test_fc_mrv_3()


