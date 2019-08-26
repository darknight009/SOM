import numpy as np
from PIL import Image
import math


def dist(node1, node2):
    return np.linalg.norm(node1-node2)


def som(nodes, data):
    weights = np.zeros((nodes, nodes, 3), dtype=np.uint8)
    weights[..., 0] = np.random.randint(256, size=(nodes, nodes))
    weights[..., 1] = np.random.randint(256, size=(nodes, nodes))
    weights[..., 2] = np.random.randint(256, size=(nodes, nodes))
    Image.fromarray(weights, 'RGB').save('out.png')
    sig0 = nodes
    it = 1000
    lam = it/(math.log(sig0, 2))
    for i in range(it):
        for d in data:
            bmd = 1000
            bmu = np.array([])
            for wy in range(len(weights)):
                for wx in range(len(weights[wy])):
                    dd = dist(weights[wy][wx], np.array(d))
                    if dd < bmd:
                        bmd = dd
                        bmu = np.array([wy, wx])
            # print(weights[bmu[0]][bmu[1]])
            radius = sig0*(math.exp(-1*i/lam))
            lR = 0.1*(math.exp(-1*i/it))
            for wy in range(len(weights)):
                for wx in range(len(weights[wy])):
                    dd = dist(bmu, np.array([wy, wx]))
                    if dd <= radius:
                        thet = math.exp(-0.5*(dd**2)/(radius**2))
                        weights[wy][wx] = np.add(weights[wy][wx], thet*lR*(np.subtract(d, weights[wy][wx])))
        print("Saving Image")
        Image.fromarray(weights, 'RGB').save('out' + str(i) + '.png')
    Image.fromarray(weights, 'RGB').save('out_fin.png')


colors = [[255, 0, 0], [0, 255, 0], [0, 0, 255]]
som(800, colors)
