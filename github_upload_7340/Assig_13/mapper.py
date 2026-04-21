import sys

for line in sys.stdin:
    data = line.strip().split(",")
    
    temp = int(data[1])
    dew = int(data[2])
    wind = int(data[3])
    
    print("temp\t{}".format(temp))
    print("dew\t{}".format(dew))
    print("wind\t{}".format(wind))