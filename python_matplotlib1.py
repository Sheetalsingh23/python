# Name: Sheetal Singh
# Roll No: TECOA166


# Method 1: Scatter Plot

import matplotlib.pyplot as plt


with open("D:\Sheetal\scatter_data.csv",'r') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = [r for r in reader]
    Unemployment_Rate = [float(i[0]) for i in data]
    Stock_Index_Price = [int(float(i[1])) for i in data]
plt.scatter(Unemployment_Rate, Stock_Index_Price, color='green')
plt.title('Unemployment Rate Vs Stock Index Price', fontsize=18)
plt.xlabel('Unemployment Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.grid(True)
plt.show()


# In[22]:


# Method 2: Line Plot

df1 = pd.read_csv(r'D:\Sheetal\line_data.csv')
plt.plot(df1.Year, df1.Unemployment_Rate, color='red', marker='o')
plt.title('Unemployment Rate Vs Year', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Unemployment Rate', fontsize=14)
plt.show()


# In[55]:


# Method 3: Bar Plot
df2 = pd.read_csv(r'D:\Sheetal\bar_data.csv')
xAxis = [i + 0.5 for i, _ in enumerate(df2.Country)]
plt.bar(xAxis, df2.GDP_Per_Capita, color='teal')
plt.title('Country Vs GDP Per Capita', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('GDP Per Capita', fontsize=14)
plt.xticks([i + 0.5 for i, _ in enumerate(df2.Country)], df2.Country)
plt.show()

