def get_input_distances(self, car):
    distances = [] # Distance of the car's eight radars to the boundary
    x, y = car.front_bumper_pos
    distances.append(self.__get_distance_to_boundary(x, y))

    return distances # A list of eight integers.


def __get_distance_to_boundary(self, x, y):
    distances = []

    # Define directions (north, 45 degrees northeast, east, etc.)
    directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

    # Iterate through each direction
    for direction in directions:
        dx, dy = direction
        distance = 0

        # Move in the current direction until reaching the track boundary
        while self.track_mat[x, y] != 0:  # Assuming 0 represents the grass
            x += dx
            y += dy
            distance += 1

        distances.append(distance)

    return distances
