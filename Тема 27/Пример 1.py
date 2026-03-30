from math import *


def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def cluster_centers(points):
    sum_distances = [sum([distance(p1, p2) for p1 in points]) for p2 in points]
    return points[sum_distances.index(min(sum_distances))]


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


# Решение для файла А
points = list(list(map(float, line.replace(',', '.').split())) for line in open('Пример 1 A.txt').readlines())
clusters = clusterize(points, 1)
center1 = cluster_centers(clusters[0])
center2 = cluster_centers(clusters[1])
print(min(int(center1[0] * 10000),int(center2[0] * 10000)), min(int(center1[1] * 10000), int(center2[1] * 10000)))

# Решение для файла В
points = list(list(map(float, line.replace(',', '.').split())) for line in open('Пример 1 B.txt').readlines())
clusters = clusterize(points, 1)
clusters.sort(key=len, reverse=True)
clusters = clusters[:3]
print(int(distance(cluster_centers(clusters[0]), cluster_centers(clusters[-1])) * 10000))

total_max_distance = 0
for cluster in clusters:
    center = cluster_centers(cluster)
    max_distance = max(distance(center, point) for point in cluster)
    total_max_distance = max(total_max_distance, max_distance)
print(int(total_max_distance * 10000))