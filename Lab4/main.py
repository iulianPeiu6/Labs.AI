import copy
import sys


class Map(object):
    def __init__(self, _location_neighbours_map, _location_colors_map):
        self.answer = {}
        self.neighbours = _location_neighbours_map
        self.colors = _location_colors_map
        self.visited = set()
        self.init_answer()
        
    def init_answer(self):
        self.answer = dict(self.colors)

    def forward_checking(self, location):
        for neighbour in self.neighbours[location]:
            self.colors[neighbour] = self.colors[neighbour] - self.colors[location]

    def is_not_consistent(self):
        for color in self.colors:
            print(f"Checking color: {color, len(color)}")
            if len(color) == 0:
                return True
        print(f"Consisten: {self.colors}")
        return False

    def __str__(self) -> str:
        str = self.colors.__str__()
        return str           


def solve_via_fc(map):
    for location in map.colors:
        colors = map.colors[location]
        if location in map.visited:
            continue
        map.visited.add(location)
        #daca nu avem culorile disponibile
        if map.is_not_consistent():
            #inconsistance
            print(f"DEBUG:\t Inconsistent solution:{map} ")
            pass
        if len(map.visited) == len(map.colors.keys()):
            print(f"INFO:\t Solution found: {map}")
            sys.exit()
        #daca avem culori disponibile
        for color in colors:
            next_map = copy.deepcopy(map)
            next_map.colors[location] = {color}
            print(f"DEBUG:\t Checking color {color} for location {location} in map {map}")
            #forward checking
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
    #print(problem.answer)
    solve_via_fc(problem)


