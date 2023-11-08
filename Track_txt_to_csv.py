import numpy as np
from matplotlib import pyplot as plt

def displayer(listx):
    plt.imshow(listx, interpolation='nearest')
    plt.show()
    #for row in listx:
     #   for col in row:
      #     if col == 0:
       #         print("*")

listnum  = []
filename = r"Track.txt"
#f = open(filename, "r")
#print(f.read())
#print(filename)
count = 0
with open(filename) as opened_file:
    for line in opened_file:
        #print (line)  # The comma to suppress the extra new line char
        for c in line:
            if c != "\n" :
                if ord(c) != 32:
                    if int(c) == 1 or int(c) == 0:
                        listnum.append(int(c))


#print("length = ", len(listnum))

reshaped_listnum = np.reshape(listnum, (1572, 2000))
np.savetxt("Track.csv", reshaped_listnum, delimiter=",")
displayer(reshaped_listnum)




