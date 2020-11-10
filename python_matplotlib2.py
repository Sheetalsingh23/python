# Name: Sheetal Singh
# Roll No: TECOA166

import matplotlib.pyplot as plt
import numpy as np
import csv

with open(r"Game_medal.csv",'r') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = [r for r in reader]
    Country_Names = [i[0] for i in data]
    gold_medals= [int(i[1]) for i in data]
    silver_medals= [int(i[2]) for i in data]
    bronze_medals= [int(i[3]) for i in data]
    
xpos = np.arange(len(Country_Names))

plt.bar(xpos-0.2, gold_medals, width = 0.2, label="GOLD MEDALS")
plt.bar(xpos, silver_medals,color='orange', width = 0.2, label="SILVER MEDALS")
plt.bar(xpos+0.2, bronze_medals,color='green', width = 0.2, label="BRONZE MEDALS")
plt.title('Olympics 2018', fontsize=14,  color='#0000FF')
plt.xlabel('Nations', fontsize=14, color='#842DCE')
plt.ylabel('Medals', fontsize=14, color='#842DCE')

plt.xticks([i for i, _ in enumerate(Country_Names)],Country_Names)
plt.legend()
plt.show()

