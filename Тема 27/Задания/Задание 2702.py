# Решение

from math import *

def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def cluster_center(cluster):
    sum_distance = [sum([distance(p1, p2) for p1 in cluster]) for p2 in points]
    return points[sum_distance.index(min(sum_distance))]


def clusterize(points, eps):
    clusters = []

    for point in points:
        indexes = []

        for i in range(len(clusters)):
            for p in clusters[i]:
                if distance(p, point) <= eps:
                    indexes.append(i)
                    break

        if not indexes:
            clusters.append([point])
        else:
            clusters[indexes[0]].append(point)
            for i in indexes[1:]:
                clusters[indexes[0]].extend(clusters[i])
                del clusters[i]
                
    return clusters


total = []
points = list(list(map(float, ' '.join(line.split()[:-1]).replace(',', '.').split())) for line in open('2702_A.txt').readlines())

clusters = clusterize(points, 1)
print(len(clusters))
center_1 = cluster_center(clusters[0])
center_2 = cluster_center(clusters[1])
for i in clusters[0]:
    if i[2][0] == 'A' and i[2][-3:] == 'III':
        i.append(distance(center_1, i))
        total.append(i)
print(total)


# Ответ: значения через запятую
answer1 = ...
answer2 = ...

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(27, 2702, answer1 + answer2, 'e075d2d1b9c44148f6f4b2c6fb754850'))