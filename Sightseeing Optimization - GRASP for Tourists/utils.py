from matplotlib import pyplot as plt
import numpy as np

def plot_tour(coords, city_tour, title="Tourist Route"):
    xy = np.zeros((len(city_tour[0]), 2))
    for i in range(len(city_tour[0])):
        xy[i,0] = coords[city_tour[0][i],0]
        xy[i,1] = coords[city_tour[0][i],1]
    plt.figure(figsize=(8,6))
    plt.plot(xy[:,0], xy[:,1], marker='o', color='black')
    plt.plot(xy[0,0], xy[0,1], marker='o', color='red', label='Start')
    plt.plot(xy[1,0], xy[1,1], marker='o', color='orange', label='Second city')
    plt.title(title)
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.legend()
    plt.show()
