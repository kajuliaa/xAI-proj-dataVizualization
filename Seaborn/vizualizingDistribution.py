import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

athlete_data =  pd.read_csv('athletes.csv')
country_data = pd.read_csv('countries.csv')
tips_data = sns.load_dataset('tips')

##Vizualizing the distribution of Dataset##

##Distribution of one Variable##

#What does the total bill looks like in restaurant
sns.histplot(tips_data['total_bill'])
#plt.show()
plt.close()

#KDE Plot
sns.kdeplot(tips_data['total_bill'], fill = True)
#plt.show()
plt.close()

##Distribution of 2 Variable##
#Bivariate Plot - 2D#
sns.jointplot(x=tips_data['total_bill'], y=tips_data['tip'], kind = "kde")
#plt.show()
plt.close()
#Plot aestetic#
sns.set_style('darkgrid')#unbedingt bevor alle plot activities
plt.figure(figsize=(30,10)) #important before plot das reinzuschreiben
plt.xticks(rotation=-45) #rotation of axis labels
plt.title('Sport type and participation', fontsize=20)
sns.countplot(x=athlete_data['sport'], order= athlete_data['sport'].value_counts().index)
#plt.show()
plt.close()


sns.relplot(x= 'height', y='weight', hue='sport', height=7, aspect=2, data=athlete_data) #for high density, it is important to use this two attributes as height(extends vertically) and aspect (extends horizontally)
plt.show()