import pandas as pd
import matplotlib.pyplot as mp
import os
class PieChartData:
    def __init__(self,csv_filename,names_key,values_key):
        try:
            self.filename = csv_filename
            self.namesKey = names_key
            self.valuesKey = values_key
            self.csv = pd.read_csv(csv_filename)
            self.labels = [i for i in self.csv[names_key]]
            self.values = [i for i in self.csv[values_key]]
        except:
            pass
    def isValid(self):
        try:
            return (self.namesKey in self.csv.columns and self.valuesKey in self.csv.columns and len(self.labels)==len(self.values) and sum(self.values)==100)
        except:
            return False
pie = PieChartData('random_data.csv','names','values')
print(pie.isValid())