import re
import random
import math
import matplotlib.pyplot as plt

def get_distance(x,y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)


def kmeans(num_clusters,data):
    clusters = []
    #setting arbitrary initial clusters
    for x in range(0,num_clusters):
        rand =random.randint(0,len(data))
        clusters.append(data[x])
    #adding cluster tags to the data
    for datum in data:
        datum.append(0)

    changes_made = 1
    while(changes_made):
        for datum in data:
            for x in range(0,num_clusters):
                if(get_distance(clusters[x],datum) < get_distance(datum,clusters[datum[-1]])):
                    datum[-1] = x


        changes_made = 0

        for x in range(0,num_clusters):
            totals = [0] * (len(data[0])-1)
            num = 0
            for datum in data:
                if(datum[-1] == x):
                    num+=1
                    for y in range(0,len(data[0])-1):
                        totals[y]+=datum[y]
            averages = []
            if(num):
                for total in totals:
                    averages.append(total/num)
                for y in range(0,len(data[0])-1):
                    if(averages[y] != clusters[x][y]):
                        changes_made +=1
                        clusters[x] = averages
            #else:
               # rand =random.randint(0,len(data))
               # clusters[x] = data[rand]
    return data

def parseData(file_name):
    f = open(file_name,"r")
    data = []
    for line in f:
        line = re.split(r'\t+',line)
        data.append([float(line[1]),float(line[2])])
    return data


if __name__ == "__main__":
    data = kmeans(4,parseData("cluster_data.txt"))

    x,y,c = [],[],[]

    for point in data:
        x.append(point[0])
        y.append(point[1])

        if(point[2] == 0):
            c.append("red")
        elif(point[2] == 1):
            c.append("blue")
        elif(point[2] == 3):
            c.append("yellow")
        else:
            c.append("green")

    plt.scatter(x,y,color = c)
    plt.show()
















