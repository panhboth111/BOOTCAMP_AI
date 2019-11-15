import matplotlib.pyplot as mp
class BasicPie:
    def __init__(self,title,data):
        self.title = title
        self.data = data
    def show(self):
        labels = [el[0] for el in self.data]
        sizes = [el[1] for el in self.data]
        explode = [0 for i in range(len(labels))]
        mp.pie(sizes,labels=labels,autopct='%1.1f%%')
        mp.title(self.title)
        mp.show()
    def save(self,filename):
        name = str(filename) if 'png' in filename else str(filename)+'.png'
        mp.savefig(name)