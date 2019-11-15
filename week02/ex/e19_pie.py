import pandas as pd
import matplotlib.pyplot as mp
def gen_pie(title,csv_filename,out_filename,names_key,values_key):
    csv = pd.read_csv(csv_filename)
    labels = [i for i in csv[names_key]]
    values = [i for i in csv[values_key]]
    explode = tuple(0.1 if(i==values.index(max(values))) else 0.0 for i in range(len(values)))
    name = str(out_filename) if 'png' in out_filename else str(out_filename)+'.png'
    mp.pie(values,labels=labels,explode=explode,autopct='%1.1f%%',shadow=True)
    mp.savefig(out_filename)
    mp.title(title)
    mp.show()
    mp.close()