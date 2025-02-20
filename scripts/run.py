from pyclassify.classifier import kNN
from pyclassify.utils import read_config
from os.path import abspath

parms = read_config("experiments/config")

path2data = parms["dataset"]


def read_data(path2data: str):
    data_list = []
    labels_list = []
    with open(path2data, "r") as f:
        for line in f:
            current_data = line.strip().split(",")
            if current_data[-1] == "g":
                current_label = 1
            elif current_data[-1] == "b":
                current_label = 0

            labels_list.append(current_label)
            current_data = [float(x) for x in current_data[:-1]]
            data_list.append(current_data[:-1])
    return data_list, labels_list


# EOF
x, y = read_data(path2data)
N = len(x)
train_len = int(N * 0.2)
test_len = N - train_len
a = kNN(parms["k"])
pred = a((x[:train_len], y[:train_len]), x[train_len:])
# accur = sum(pred == y[train_len:]) / test_len
ground_truth = y[train_len:]
tot_corr = 0
for i in range(test_len):
    tot_corr += pred[i] == ground_truth[i]
print("total accuracy: ", round(tot_corr / test_len, 3))
