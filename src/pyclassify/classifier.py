from pyclassify.utils import *


class kNN:
    def __init__(self, k):
        if isinstance(k, int):
            self.k = k
        else:
            raise TypeError(f"k should be an integer not a {type(k)}")

    def _get_k_nearest_neighbors(self, X: list[list[float]], y: list[int], x: float):
        dist_list = []
        for el in X:
            dist_list.append(distance(el, x))
        sorted_dist = sorted(
            enumerate(dist_list), key=lambda x: x[1]
        )  # lambda is the key function according to which it sorts
        kNNs_dist_labels = sorted_dist[: self.k]
        kNNs_labels = [y[el[0]] for el in kNNs_dist_labels]
        return kNNs_labels

    def __call__(
        self, training: tuple, new_points: list[list[float]]
    ):  # overrides the built in method. It is automatically called when creating a new instance. training should be a tuple with list[points] and list[labels]
        pred_classes = []
        for el in new_points:
            nearest_labels = self._get_k_nearest_neighbors(training[0], training[1], el)
            pred_label = majority_vote(nearest_labels)
            pred_classes.append(pred_label)
        return pred_classes
