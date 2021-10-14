import pandas as pd,statistics as st,plotly.figure_factory as pff,random

data=pd.read_csv('medium_data.csv')
newData=data["reading_time"].tolist()

population_mean=st.mean(newData)
print(population_mean)

def dataSet():
    dataSetList=[]
    for i in range(0,30):
        index=random.randint(0,len(newData)-1)
        value=newData[index]
        dataSetList.append(value)
    dataSetmean=st.mean(dataSetList)
    return dataSetmean

def plot_graph(mainDataList):
    graph=pff.create_distplot([mainDataList],['reading_time'],show_hist=False)
    graph.show()

def setup():
    mainDataList=[]
    for i in range(0,100):
        dMean=dataSet()
        mainDataList.append(dMean)
    dataMean=st.mean(mainDataList)
    plot_graph(mainDataList)
    print(dataMean)

setup()