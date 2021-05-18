import csv
from os import stat
import pandas as pd
import statistics
import random
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
population_mean = statistics.mean(data)
std_dev = statistics.stdev(data)

def rand_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        val = data[random_index]
        dataset.append(val) 
    sample_mean = statistics.mean(dataset)

    return sample_mean

def rand_set_of_std_dev(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        val = data[random_index]
        dataset.append(val) 
    sample_stdv = statistics.stdev(dataset)

    return sample_stdv


def show_fig(mean_data):
    df = mean_data
    fig = ff.create_distplot([df], ["Temp"], show_hist=False)
    fig.show()

def setup():
    mean_data = []
    for i in range(0, 1000):
        set_of_mean = rand_set_of_mean(100)
        mean_data.append(set_of_mean)
    show_fig(mean_data)

# setup()
sample_std_dev = rand_set_of_std_dev(100)
std_data = []
std_data.append(sample_std_dev)
show_fig(std_data)