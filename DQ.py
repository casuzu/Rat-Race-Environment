def disqualification_check(self):
    # Check if any tire of any car is at the track boundary (pixel value of 0 or 1)
    for car in self.__carlist:
        tires_coordinates = car.get_tires_coordinates()
        for tire in tires_coordinates:
            x, y = tire
            if x == 0 or x == 1 or y == 0 or y == 1:
                # If any tire is at the boundary, disqualify the car and reset to the start line
                car.reset_to_start()
                print(f"{car.racer_name} disqualified! Resetting to the start line.")