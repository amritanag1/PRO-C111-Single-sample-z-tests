import pandas as pd
import statistics
import random
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()

def get_random100_sample_average():
    samples = []
    for i in range(0, 100):
        random_no = random.randint(0, len(data)-1)
        datavalue = data[random_no]
        samples.append(datavalue)

    mean = statistics.mean(samples)
    return(mean)

def make_average_list():
    average_list = []
    for i in range(0, 100):
        average = get_random100_sample_average()
        average_list.append(average)
    
    return(average_list)
    
    
def calculations():
    averages = make_average_list()
    show_plot(averages)

    total_average = statistics.mean(averages)
    deviation = statistics.stdev(averages)
    print("Total average: " + str(total_average), ", Standard Deviation: " + str(deviation))


def show_plot(averages):
    fig = ff.create_distplot([averages], ["Average Distribution"], show_hist=False) 
    fig.show()

calculations()

mean_before_intervention = 302.7773
std_before_intervention = 84.19637874425756

mean = statistics.mean(data)

zscore = (mean_before_intervention - mean)/std_before_intervention
print(zscore)