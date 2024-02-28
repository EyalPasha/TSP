import sys

from tsp_ga import *


class Point:
    def __init__(self) -> None:
        self.x = random.randint(-100, 100)
        self.y = random.randint(-100, 100)


def dist(p1, p2):
    return float(math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2))


def fitness(points1):
    sum1 = 0
    for i1 in range(1, len(points1)):
        sum1 += dist(points1[i1 - 1], points1[i1])
    return sum1


def randSol(points11, size):
    mn = sys.maxsize
    for i11 in range(size):
        ps = points11.copy()
        random.shuffle(ps)
        f = fitness(ps)
        if f < mn:
            mn = f
            best = ps
    return best


for i in range(5):
    print(f"test {i}")
    points = [Point() for i in range(100)]
    rs = fitness(randSol(points, 20))
    gas = fitness(solve(points))
    if gas > rs:
        print("your GA did not have a better result than the random algo (-20)")

print("done")
