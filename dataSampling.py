import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random
import pandas as pd
import csv

df=pd.read_csv("data1.csv")
data=df["temp"].tolist()
mean=statistics.mean(data)
std_deviation=statistics.stdev(data)

fig=ff.create_distplot([data],["temp"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
fig.show()

dataset=[]
for i in range(0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)

mean=statistics.mean(dataset)
std_deviation=statistics.stdev(dataset)



def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean
    
def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean=statistics.mean(mean_list)
    print("Mean of Sampling Distribuiton:= ",mean)

setup()