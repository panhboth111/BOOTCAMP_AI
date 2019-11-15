import matplotlib.pyplot as mp
import pandas as pd
import math
class PieChartData:
    def __init__(self,filename,names,values):
        self.csv = pd.read_csv(filename)
        self.labels = [i for i in self.csv[names]]
        self.values = [i for i in self.csv[values]]
class PieChartContainer:
    def __init__(self,pc_data_arr):
        self.arr = pc_data_arr
        labels = [i.labels for i in self.arr]
        values = [i.values for i in self.arr]
        row = 0
        isZero = True
        for i in range (len(self.arr)):
            mp.subplot2grid((math.ceil(len(self.arr)/2),2),(row,0 if isZero else 1)).pie(values[i],labels=labels[i])
            isZero = not isZero
            row += 1 if isZero else 0 
    def show(self):
        mp.show()
    def save(self,filename):
        name = str(filename) if '.png' in filename else str(filename)+'.png'
        mp.savefig(name)