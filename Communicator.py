

from os import listdir
from os.path import isfile, join
from datetime import datetime

import matplotlib.pyplot as plt
import os
import Acc_Processor

def main():
    print("Hello World!")
    path = os.path.abspath("Training Files/dataset_fog_release/dataset")
    dataset = []
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for file in onlyfiles:
        samples = Acc_Processor.load_file(join(path, file))
        dataset.append(samples)

    print(dataset)
    print(len(dataset))
    print(dataset[1].columns)
    #windowed_set = Acc_Processor.windowed_view(dataset[1], 256, 128)

    plt.clf()
    plt.plot(dataset[1][["time"]], dataset[1][["shank_x", "shank_y", "shank_z"]])
    plt.show()
    # file = Acc_Processor.load_file(join(path, onlyfiles[1]))
    # print(file)

if __name__ == "__main__":
    main()










