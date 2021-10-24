import copy
import sys


class Map(object):
    def __init__(self, _location_neighbours_map, _location_colors_map):
        self.neighbours_mapping = _location_neighbours_map
        self.colors_mapping = _location_colors_map
        self.visited = set()

    def forward_checking(self, location):
        for neighbour in self.neighbours_mapping[location]:
            self.colors_mapping[neighbour] = self.colors_mapping[neighbour] - self.colors_mapping[location]

    def is_not_consistent(self):
        for location in self.colors_mapping:
            if len(self.colors_mapping[location]) == 0:
                return True
        return False

    def __str__(self) -> str:
        str = self.colors_mapping.__str__()
        return str           


def solve_via_fc(map):
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
            print(f"DEBUG:\t Checking color {color} for location {location} in map {map}")
            next_map.forward_checking(location)
            solve_via_fc(next_map)
        

if __name__ == '__main__':
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

    solve_via_fc(problem)


