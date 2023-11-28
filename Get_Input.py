def get_input_distances(self):
    distances = []

    for car in self.__carlist:
        x, y = car.front_bumper_pos
        distances.append(self.__get_distance_to_boundary(x, y))

    return distances


def __get_distance_to_boundary(self, x, y):
    distances = []

    # Define directions (north, 45 degrees northeast, east, etc.)
    directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

    # Iterate through each direction
    for direction in directions:
        dx, dy = direction
        distance = 0

        # Move in the current direction until reaching the track boundary
        while self.track(x, y) != 1:  # Assuming 1 represents the track boundary
            x += dx
            y += dy
            distance += 1

        distances.append(distance)

    return distances