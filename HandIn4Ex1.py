import sys
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt

#1.2

data = np.genfromtxt('C:\\Users\\Bruger\\Documents\\4semester\\Python\\dat4sem2020spring-python\\befkbhalderstatkode.csv', 
delimiter=',', dtype=np.uint, skip_header=1) #print

#1.3
neighb = {1: 'Indre By', 2: 'Oesterbro', 3: 'Noerrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanloese', 7: 'Broenshoej-Husum', 8: 'Bispebjerg', 9: 'Amager Oest', 
       10: 'Amager Vest', 99: 'Udenfor'}


lst2 = [1,2,3,4,5,6,7,8,9,10,99]
dict = {}
def create_dict_for_citizens():
    for x in lst2:
        citizens = np.sum(data[(data[:,0] == 2015) & (data[:,1] == x)][:,4])
    #print("Bydel {} - {}".format(x, neighb[x]), citizens )
    #looper gennem vha. mask 
        dict[neighb[x]] = citizens
    #print(dict)
    return dict

print(create_dict_for_citizens())


mask = (data[:,0] == 2015) & (data[:,1] == 9)
masktotal = (data[:,0] == 2015)
#print(data[mask])
print("total", np.sum(data[masktotal][:,4])) # printer total

#1.4
#%%
dictfor4 = create_dict_for_citizens()

xakse = list(dictfor4.keys())
xaksetrue = xakse.sort()
yakse = list(dictfor4.values())
yaksetrue = yakse.sort()


plt.bar(xakse,yakse)
plt.xlabel("Names", fontsize=13)
plt.ylabel("Ages", fontsize=13)
plt.title("People & Age", fontsize=17)
