import numpy as np
#import math as m
from matplotlib import pyplot as plt
from Car import CarObj

def TRACK_ROW():
    return 1572

def TRACK_COL():
    return 2000

def RACE_TRACK(filename):
    listnum = np.genfromtxt(filename, delimiter=',')
    reshaped_listnum = listnum.reshape(TRACK_ROW(), TRACK_COL())
    return reshaped_listnum

def track_displayer(list_data):
    #list1 = np.array([[1000, 300]])
    #list1 = np.array([[1, 2, 3], [4, 5, 6]])
    #reshaped_list1 = np.reshape(list1, (2,1))

    plt.imshow(list_data, interpolation='nearest')
    #plt.imshow(reshaped_list1, alpha=0.5)
    plt.show()
    #plt.draw()

def NUM_OF_DRIVERS():
     return len(racers_name)

def PIXEL_LENGTH():
    return 50




class Environment:
    def __init__(self, track_file, start_position, orientation):
        # Matrix for the track
        self.TRACK_MAT = RACE_TRACK(track_file)
        self.__carlist = []
        self.__cars_adjust(orientation)  # orient the cars'facing directions
        self.__all_cars_start_pos = start_position.copy()
        self.__load_cars()  # loads the cars into their starting positions and stores in carlist


    def __load_cars(self):

        for i in range(0, NUM_OF_DRIVERS()):  # initialize the drivers car starting positions
            __car_obj = CarObj(racers_name[i], self.__all_cars_start_pos, self.orient_angle)
            self.__carlist.append(__car_obj)


    def reset_cars(self):
        for i in range(0, NUM_OF_DRIVERS()):
            self.__carlist[i].front_bumper_pos = self.__all_cars_start_pos
            self.__carlist[i].car_theta = self.orient_angle
            self.__carlist[i].update_Carposition()

    def __cars_adjust(self, orientation):
        orientation = orientation.upper()

        if orientation == "NORTH":
            self.orient_angle = 0

        elif orientation == "WEST":
           self.orient_angle = 90

        elif orientation == "SOUTH":
           self.orient_angle = 180

        elif orientation == "EAST":
           self.orient_angle = 270


    def track(self, x, y):
        z = self.TRACK_MAT[x, y]
        return z

    def car_get(self, i):
        result = self.__carlist[i]
        return result



file_name = r"Track.csv"

#racers_name = ["Chibu", "Kefe", "Dan", "Nick", "Rupo", "Mike"]
racers_name = ["Chibu"]

#                     start_position     car_orientation
env = Environment(file_name, [1000, 300], "East")


for j in range(0, NUM_OF_DRIVERS()):
    car_item = env.car_get(j)
    print("============================")
    print(car_item.racer_name)
    print("============================")
    car_item.run()

    for step in range(0, len(car_item.tires_history)):
        print(step)
        #print(car_item.tires_history[step])
        #print(car_item.front_bumper_history[step])

    track_displayer(env.TRACK_MAT)









