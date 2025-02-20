import os
import yaml


def distance(point1: list[float], point2: list[float]):
    eucl_dist = 0
    if not isinstance(point1, list):  # in the case it's not a list
        point1 = [
            point1,
        ]
    if not isinstance(point2, list):  # in the case it's not a list
        point2 = [
            point2,
        ]
    if len(point1) != len(point2):
        raise ValueError(
            "the training dataset and the test point have different dimensionalities"
        )
    for i in range(len(point1)):
        eucl_dist += (point1[i] - point2[i]) ** 2
    return eucl_dist


def majority_vote(neighbors: list[int]):
    if type(neighbors) != list:
        raise TypeError("The input neighbors must be a list[int]")
    list_len = len(neighbors)
    dec_boundary = list_len / 2
    vote = sum(neighbors)
    if vote >= dec_boundary:
        majority = 1
    else:
        majority = 0

    return majority


def read_config(file):
    filepath = os.path.abspath(f"{file}.yaml")
    with open(filepath, "r") as stream:
        kwargs = yaml.safe_load(stream)
    return kwargs
