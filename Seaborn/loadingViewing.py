#importing required libraries
##IN PYCHARM I SHOULD ALL THINGS PRINT()##
from itertools import count

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#importing the dataset
athlete_data =  pd.read_csv('athletes.csv')
country_data = pd.read_csv('countries.csv')
tips_data = sns.load_dataset('tips')

#getting a peek at the athlete dataset
print(athlete_data.head(10))
#getting a peek at the countries dataset
print(country_data.head(10))
#getting a peek at the tips dataset
print(tips_data.head(10))

##VIZUALIZATION##
#What is relationship between population and GDP?
sns.relplot(x="population", y="gdp_per_capita", data = country_data)
#plt.show()
plt.close()

#What is the correlation between height and weight of athletes?
sns.relplot(x="height", y="weight", data = athlete_data)
#plt.show()
plt.close()

#Height and weight correlation based on sex
sns.relplot(x="height", y="weight", hue = "sex", data= athlete_data)
#plt.show()
plt.close()

#Height and weight correlation based on sport
sns.relplot(x="height", y="weight", hue="sport", data = athlete_data)
#plt.show()
plt.close()

##PLOTTING CATEGORICAL DATA##
#What is the connection between the tip amount and day of week
sns.catplot(x="day", y="tip", data = tips_data)
#plt.show()
plt.close()
#swarm prevents points from overlapping
sns.catplot(x="day", y="tip", kind="swarm", data = tips_data)
#plt.show()
plt.close()

#Who typically gets higher tips men or women?
sns.catplot(x="day", y="tip", hue="sex", data=tips_data)
#plt.show()
plt.close()
sns.catplot(x="day", y="tip", hue="sex", kind="swarm", data=tips_data)
#plt.show()
plt.close()

##Boxplot##
sns.catplot(x="day",y="tip",kind="box", data=tips_data)
#plt.show()
plt.close()
sns.boxplot(x="day",y="tip", data=tips_data)
#plt.show()
plt.close()
sns.catplot(x="day", y="tip", hue="sex", kind="box", data=tips_data)
#plt.show()
plt.close()

##Violin plots
sns.catplot(x="day", y="tip", kind="violin", data=tips_data)
#plt.show()
plt.close()

#What are the types of sports and what does their participation look like?
sns.countplot(x=athlete_data["sport"], order=athlete_data["sport"].value_counts().index)
plt.show()

#If you do not close plots, then it cause problems and can mix up two of them or even more