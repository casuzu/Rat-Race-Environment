def disqualification_check(self):
    # Check if any tire of any car is at the track boundary (pixel value of 0 or 1)
    for car in self.__carlist:
        tires_coordinates = car.get_tires_coordinates()
        for tire in tires_coordinates:
            x, y = tire
            if self.track_mat[x][y] == 0:
                return True #Car is off track.
    return False # All cars are on the track.
    #Add code for crossing the finish line.
           
