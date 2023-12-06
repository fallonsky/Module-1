import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data2.csv")
df = df.drop(df.columns[[1,2]], axis=1)
print(df)



# Get current axis 
ax = plt.gca() 
  
# line plot for math marks 
df.plot(kind='line', 
        x='date', 
        y='delta', 
        color='green', ax=ax) 
  
# set the title 
plt.title('LinePlots') 
  
# show the plot 
plt.show() 
