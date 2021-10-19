class Map(object):
    def __init__(self, _location_neighbours_map, _location_colors_map):
        self.answer = {}
        self.location_neighbours_map = _location_neighbours_map
        self.location_colors_map = _location_colors_map
        self.init_answer()

    def init_answer(self):
        for key in self.location_colors_map:
            self.answer.setdefault(key, next(iter(self.location_colors_map[key])))


if __name__ == '__main__':
    location_neighbours_map = {
        "WA": {"SA", "NT"},
        "SA": {"WA", "NT"},
        "NT": {"WA", "SA"}
    }

    location_colors_map = {
        "WA": {"red", "green", "blue"},
        "SA": {"red", "green"},
        "NT": {"green"}
    }
    problem = Map(location_neighbours_map, location_colors_map)
    print(problem.answer)


