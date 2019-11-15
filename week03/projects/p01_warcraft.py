import pandas as pd
import json
class UnitFactory:
    def __init__(self,data_info):
        self.data_info = data_info
        try:
            self.races = []
            self.filenames = []
            self.data = []
            for i in range(4):
                self.races.append(self.data_info[i]['race'])
                self.filenames.append(self.data_info[i]['filename'])
                self.data.append(pd.read_csv(self.filenames[i]).to_json(orient='records') if 'csv' in self.filenames[i] else pd.read_json(self.filenames[i]).to_json(orient='records'))
        except:
            raise ValueError(f"Unit Data Not Found {self.checkMissing()}")
    def checkMissing(self):
        expectedRaces = ['Human','Night_Elves','Orc','Undead']
        expectedFilenames = ['human.csv','human.json','night_elves.csv','night_elves.json','orc.csv','orc.json','undead.csv','undead.json']
        if(len(self.data_info)<4):
            return [i for i in expectedRaces if i not in self.races]
        else:
            return [i['race'] for i in self.data_info if i['filename'] not in expectedFilenames]
    def get_races(self):
        self.races.sort()
        self.races = json.dumps(self.races)
        return self.races
    def get_units_names(self,race):
        data = [json.loads(i)for i in self.data]
        result = []
        if(race.lower()=='human'):
            return [i['Unit'] for i in data[0]]
        elif(race.lower()=='night_elves'):
            return [i['Unit'] for i in data[1]]
        elif(race.lower()=='orc'):
            return [i['Unit'] for i in data[2]]
        elif(race.lower()=='undead'):
            return [i['Unit'] for i in data[3]]
        elif(race.lower()=='all'):
            expectedRaces = ['Human','Night_Elves','Orc','Undead']
            for i in range(4):
                for j in data[i]:
                    result.append(tuple([j['Unit'],expectedRaces[i]]))
            return sorted(result,key=lambda x: x[0])
    def get_units_gold_cost(self,race):
        expectedRaces = ['Human','Night_Elves','Orc','Undead']
        data = [json.loads(i)for i in self.data]
        if(race.lower()=='human'):
            return sorted([tuple([i['Unit'],i['Gold']]) for i in data[2]if i['Gold']!='None'],key=lambda x: x[1])
        elif(race.lower()=='night_elves'):
            return sorted([tuple([i['Unit'],i['Gold']]) for i in data[2]if i['Gold']!='None'],key=lambda x: x[1])
        elif(race.lower()=='orc'):
            return sorted([tuple([i['Unit'],i['Gold']]) for i in data[2]if i['Gold']!='None'],key=lambda x: x[1])
        elif(race.lower()=='undead'):
            return sorted([tuple([i['Unit'],i['Gold']]) for i in data[2]if i['Gold']!='None'],key=lambda x: x[1])
        elif(race.lower()=='all'):
            result = []
            for i in range(4):
                for j in data[i]:
                    result.append(tuple([j['Unit'],j['Gold'],expectedRaces[i]])) 
            result = [i for i in result if i[1]!='None' and i[1]!=None]      
            return sorted(result,key=lambda x: x[1])
    def get_units_speed(self,race):
        expectedRaces = ['Human','Night_Elves','Orc','Undead']
        data = [json.loads(i)for i in self.data]
        if(race.lower()=='human'):
            return sorted([tuple([i['Unit'],i['Speed']]) for i in data[0] if i['Speed']!='None'],key=lambda x: x[1])
        elif(race.lower()=='night_elves'):
            return sorted([tuple([i['Unit'],i['Speed']]) for i in data[1] if i['Speed']!='None'],key=lambda x: x[1])
        elif(race.lower()=='orc'):
            return sorted([tuple([i['Unit'],i['Speed']]) for i in data[2] if i['Speed']!='None'],key=lambda x: x[1])
        elif(race.lower()=='undead'):
             return sorted([tuple([i['Unit'],int(str(i['Speed']).split('/')[1]) if '/' in str(i['Speed']) else int(i['Speed'])]) for i in data[3] if i['Speed']!='None'],key=lambda x: x[1])
        elif(race.lower()=='all'):
            result = []
            res = []
            result.append([tuple([i['Unit'],i['Speed'],expectedRaces[0]]) for i in data[0] if i['Speed']!='None'])
            result.append([tuple([i['Unit'],i['Speed'],expectedRaces[1]]) for i in data[1] if i['Speed']!='None'])
            result.append([tuple([i['Unit'],i['Speed'],expectedRaces[2]]) for i in data[2] if i['Speed']!='None'])
            result.append([tuple([i['Unit'],int(str(i['Speed']).split('/')[1]) if '/' in str(i['Speed']) else int(i['Speed']),expectedRaces[3]]) for i in data[3] if i['Speed']!='None'])
            for i in range(len(result)):
                for j in range(len(result[i])):
                    res.append(result[i][j])
            return sorted(res,key=lambda x: x[1])
    def get_melee_units(self,race):
        data = [json.loads(i)for i in self.data]
        if(race.lower()=='human'):
            return sorted([i['Unit'] for i in data[0] if i['Range']=='Melee' or 'Melee' in str(i['Range'])])
        elif(race.lower()=='night_elves'):
            return sorted([i['Unit'] for i in data[1] if i['Range']=='Melee' or 'Melee' in str(i['Range'])])
        elif(race.lower()=='orc'):
            return sorted([i['Unit'] for i in data[2] if i['Range']=='Melee' or 'Melee' in str(i['Range'])])
        elif(race.lower()=='undead'):
            return sorted([i['Unit'] for i in data[3] if i['Range']=='Melee' or 'Melee' in str(i['Range'])])
        elif(race.lower()=='all'):
            res = []
            expectedRaces = ['Human','Night_Elves','Orc','Undead']
            res.append([tuple([i['Unit'],expectedRaces[0]]) for i in data[0] if i['Range']=='Melee' or 'Melee' in str(i['Range'])])
            res.append([tuple([i['Unit'],expectedRaces[1]]) for i in data[1] if i['Range']=='Melee' or 'Melee' in str(i['Range'])])
            res.append([tuple([i['Unit'],expectedRaces[2]]) for i in data[2] if i['Range']=='Melee' or 'Melee' in str(i['Range'])])
            res.append([tuple([i['Unit'],expectedRaces[3]]) for i in data[3] if i['Range']=='Melee' or 'Melee' in str(i['Range'])])
            result = []
            for i in range(len(res)):
                for j in range(len(res[i])):
                    result.append(res[i][j])
            return sorted(result) 
    def get_range_units(self,race):
        data = [json.loads(i)for i in self.data]
        if(race.lower()=='human'):
            return sorted([i['Unit'] for i in data[0] if len(str(i['Range']).split('/'))==2 or i['Range']!='Melee'])
        elif(race.lower()=='night_elves'):
            return sorted([i['Unit'] for i in data[1] if len(str(i['Range']).split('/'))==2 or i['Range']!='Melee'])
        elif(race.lower()=='orc'):
            return sorted([i['Unit'] for i in data[2] if len(str(i['Range']).split('/'))==2 or i['Range']!='Melee'])
        elif(race.lower()=='undead'):
            return sorted([i['Unit'] for i in data[3] if len(str(i['Range']).split('/'))==2 or i['Range']!='Melee'])
        elif(race.lower()=='all'):
            expectedRaces = ['Human','Night_Elves','Orc','Undead']
            res = []
            res.append([tuple([i['Unit'],expectedRaces[0]]) for i in data[0] if i['Range']!='Melee'])
            res.append([tuple([i['Unit'],expectedRaces[1]]) for i in data[1] if i['Range']!='Melee'])
            res.append([tuple([i['Unit'],expectedRaces[2]]) for i in data[2] if i['Range']!='Melee'])
            res.append([tuple([i['Unit'],expectedRaces[3]]) for i in data[3] if i['Range']!='Melee'])
            result = []
            for i in range(len(res)):
                for j in range(len(res[i])):
                    result.append(res[i][j])
            return sorted(result)
    def getUnit(self,name):
        data = [json.loads(i)for i in self.data]
        expectedRaces = ['Human','Night_Elves','Orc','Undead']
        info = []
        for i in range(len(data)):
            for j in range(len(data[i])):
                if(data[i][j]['Unit']==name):
                    info.append(data[i][j])
                    info.append(expectedRaces[i])
                    break
        return info if info else f"Invalid Unit Name [{name}]"

    def create_unit(self,name):
        return Unit(self.getUnit(name))

class Unit(UnitFactory):
    def __init__(self,name):
        self.info = name
    def get_data(self):
        return self.info
    def get_race(self):
        return self.info[1]
    def get_name(self):
        return self.info[0]['Unit']
    def get_gold_cost(self):
        return self.info[0]['Gold']
    def get_wood_cost(self):
        return self.info[0]['Wood']
    def get_food_cost(self):
        return self.info[0]['Food']
    def get_hit_points(self):
        return self.info[0]['Hit Points']
    def get_armor_type(self):
        return self.info[0]['Armor Type']
    def get_speed(self):
        return self.info[0]['Speed']
class UnitStats:
    def __init__(self,data_info):
        self.data_info = data_info
        try:
            self.races = []
            self.filenames = []
            self.data = []
            for i in range(4):
                self.races.append(self.data_info[i]['race'])
                self.filenames.append(self.data_info[i]['filename'])
                self.data.append(pd.read_csv(self.filenames[i]).to_json(orient='records') if 'csv' in self.filenames[i] else pd.read_json(self.filenames[i]).to_json(orient='records'))
                self.expectedRaces = {'Human':0,'Night_Elves':1,'Orc':2,'Undead':3} 
                self.data2 = [json.loads(i)for i in self.data]
        except:
            raise ValueError(f"Unit Data Not Found {self.checkMissing()}")
    def checkMissing(self):
        expectedRaces = ['Human','Night_Elves','Orc','Undead']
        expectedFilenames = ['human.csv','human.json','night_elves.csv','night_elves.json','orc.csv','orc.json','undead.csv','undead.json']
        if(len(self.data_info)<4):
            return [i for i in expectedRaces if i not in self.races]
        else:
            return [i['race'] for i in self.data_info if i['filename'] not in expectedFilenames]
    def armor_type(self,race,filename,maximum=0):
        expectedArmors = ['Heavy','Light','Unarmored','Medium']
        ArmorType = [i['Armor Type'] for i in self.data2[self.expectedRaces[race]]] if race.lower() !='all' else [j['Armor Type'] for i in self.data2 for j in i]
        labels = [j[0] for j in sorted([tuple([expectedArmors[i],ArmorType.count(expectedArmors[i])]) for i in range(len(expectedArmors))],key=lambda x: x[1])]
        numbers = sorted([ArmorType.count('Heavy'),ArmorType.count('Medium'),ArmorType.count('Unarmored'),ArmorType.count('Light')])
        resultNumbers = [numbers[i] for i in range(maximum)] if 0<maximum<=len(numbers) else numbers
        resultLabels = [labels[i] for i in range(maximum)] if 0<maximum<=len(numbers) else labels
        mp.pie(resultNumbers,labels=resultLabels,autopct='%1.1f%%')
        mp.title(f'Armor Type - {race}')
        mp.savefig(filename+'.png' if '.png' not in filename else filename)
        mp.show()

    def gold_cost_per_unit(self,race,filename,maximum=0):
        goldCost = sorted([tuple([i['Unit'],i['Gold']]) for i in self.data2[self.expectedRaces[race]] if i['Gold']!='None' and i['Gold']!=None],key=lambda x: x[1],reverse=True) if race.lower() !='all' else sorted([tuple([j['Unit'],j['Gold']]) for i in self.data2 for j in i if j['Gold']!='None' and j['Gold']!=None],key=lambda x: x[1])
        numbers = [i[1] for i in goldCost]
        labels = [i[0] for i in goldCost]
        resultNumbers = [numbers[i] for i in range(maximum)] if 0<maximum<=len(numbers) else numbers
        resultLabels = [labels[i] for i in range(maximum)] if 0<maximum<=len(numbers) else labels
        finalNumbers = sorted(resultNumbers)
        resultLabels.reverse()
        mp.barh(resultLabels,finalNumbers)
        mp.title(f'Gold Cost Per Unit - {race}')
        mp.savefig(filename+'.png' if '.png' not in filename else filename)
        mp.show()
    def wood_cost_per_unit(self,race,filename,maximum=0):
        woodCost = sorted([tuple([i['Unit'],i['Wood']]) for i in self.data2[self.expectedRaces[race]] if i['Wood']!='None' and i['Wood']!=None],key=lambda x: x[1],reverse=True) if race.lower() !='all' else sorted([tuple([j['Unit'],j['Wood']]) for i in self.data2 for j in i if j['Wood']!='None' and j['Wood']!=None],key=lambda x: x[1],reverse=True)
        numbers = [i[1] for i in woodCost]
        labels = [i[0] for i in woodCost]
        resultNumbers = [numbers[i] for i in range(maximum)] if 0<maximum<=len(numbers) else numbers
        resultLabels = [labels[i] for i in range(maximum)] if 0<maximum<=len(numbers) else labels
        finalNumbers = sorted(resultNumbers)
        resultLabels.reverse()
        mp.barh(resultLabels,finalNumbers)
        mp.title(f'Wood Cost Per Unit - {race}')
        mp.savefig(filename+'.png' if '.png' not in filename else filename)
        mp.show()
    def food_cost_per_unit(self,race,filename,maximum=0):
        foodCost = sorted([tuple([i['Unit'],i['Food']]) for i in self.data2[self.expectedRaces[race]] if i['Food']!='None' and i['Food']!=None],key=lambda x: x[1],reverse=True) if race.lower() !='all' else sorted([tuple([j['Unit'],j['Food']]) for i in self.data2 for j in i if j['Food']!='None' and j['Food']!=None],key=lambda x: x[1],reverse=True)
        numbers = [i[1] for i in foodCost]
        labels = [i[0] for i in foodCost]
        resultNumbers = [numbers[i] for i in range(maximum)] if 0<maximum<=len(numbers) else numbers
        resultLabels = [labels[i] for i in range(maximum)] if 0<maximum<=len(numbers) else labels
        finalNumbers = sorted(resultNumbers)
        resultLabels.reverse()
        mp.barh(resultLabels,finalNumbers)
        mp.title(f'Food Cost Per Unit - {race}')
        mp.savefig(filename+'.png' if '.png' not in filename else filename)
        mp.show()
    def speed_per_unit(self,race,filename,maximum=0):
        speed = sorted([tuple([i['Unit'],i['Speed']]) for i in self.data2[self.expectedRaces[race]] if i['Speed']!='None' and i['Speed']!=None],key=lambda x: x[1],reverse=True) if race.lower() !='all' else sorted([tuple([j['Unit'],j['Speed']]) for i in self.data2 for j in i if j['Speed']!='None' and j['Speed']!=None],key=lambda x: x[1],reverse=True)
        numbers = [i[1] for i in speed]
        labels = [i[0] for i in speed]
        resultNumbers = [numbers[i] for i in range(maximum)] if 0<maximum<=len(numbers) else numbers
        resultLabels = [labels[i] for i in range(maximum)] if 0<maximum<=len(numbers) else labels
        finalNumbers = sorted(resultNumbers)
        resultLabels.reverse()
        mp.barh(resultLabels,finalNumbers)
        mp.title(f'Speed Per Unit - {race}')
        mp.savefig(filename+'.png' if '.png' not in filename else filename)
        mp.show()