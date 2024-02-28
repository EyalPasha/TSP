# TSP
Generic Algorithm for Solving the TSP Problem.
The Traveling Salesman Problem (TSP) involves finding the cheapest route that visits a given set of cities exactly once and returns to the starting city. Essentially, it is a weighted, fully connected graph, and we are looking for the minimum cumulative weight route that passes through each node once and returns to the starting node. This problem is an NP-complete problem.

Solved a variation of the TSP problem using a generic algorithm. In this version, the weight is simply the Euclidean distance between the points representing cities, and it doesn't matter which city we start or end with, as long as we visit each city exactly once.
Given an array of points (of type Point, defined in mainTrain), the function should return the best route found by the genetic algorithm as a list of points.

The solution should be better than the output of the random algorithm for the same input (random algorithm run 5 times).
