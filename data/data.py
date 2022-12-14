#used Jupyter notebook from Anaconda
#Imported pandas, matplotlib.pyplot, csv, and seaborn
#Extras: 
    #1. Data visualization in Histogram and Scatter Plot
    #2. Used multiple aspects of a single data source in your analysis

import pandas as pd
import matplotlib.pyplot as plt
import csv
import seaborn as sns


reader = pd.read_csv('hero_info.csv')



#Average integer height of superheros?
#The average height of all superheros is 102 cm
AvgHeight = reader['Height'].mean()
print('The average height of all superheros--cm--is...')
print(int(AvgHeight))

#displays count, mean, standard deviation, min, max, and 25th, 50th, and 75th percentiles as floats
#Describe Height ---> count: 734.0 , mean: 102.25, std: 139.62, min: -99.0, 25%: -99.0, 50%: 175.00, 75%: 185.0, max: 975
df1 = pd.read_csv('hero_info.csv', usecols = ["Height"])

df1.describe()


#Height Distribution of supers --> Mostly falls between 150-200 cm
%matplotlib inline

plt.hist(df1['Height'], bins=range(-100, 1000, 100), color='purple', edgecolor='black')
plt.xlabel('Height in cm')
plt.ylabel('# of superheros')
plt.title('Height Distribution--Histogram')



#Average integer weight of superheos?
#The average weight of all supers is 43 lbs
AvgWeight = reader['Weight'].mean()
print('The average weight of all superheros--lbs--is...')
print(int(AvgWeight))



#displays count, mean, standard deviation, min, max, and 25th, 50th, and 75th percentiles
#Describe Weight --> count: 732.00, mean: 43.86, std: 130.82, min: 99.0, 25%: -99.00, 50%: 62.0, 75%: 90.0, max: 900.0
df2 = pd.read_csv('hero_info.csv', usecols = ["Weight"])

df2.describe()


#Distribution of Weight graph --> Most supers fall around 0 to 100
%matplotlib inline

plt.hist(df2['Weight'], color='yellow', edgecolor='black')
plt.xlabel('Weight in lbs')
plt.ylabel('# of superheros')
plt.title('Weight Distribution--Histogram')




#displays count, # of uniqe titles, top, and the frequency of top in all headers
df3 = pd.read_csv('hero_info.csv', usecols=["name","Gender", "Eye color", "Skin color", "Race", "Publisher", "Alignment"])

df3.describe()



#prints out only the columns of the names, gender, and races of superheros
name_gender_race = reader[['name', 'Gender', 'Race']]
print(name_gender_race)

#Only shows the columns of publisher and alignments of superheros 
publisher_alignment = reader[['Publisher', 'Alignment']]
print(publisher_alignment)




#Gender distribution graph --> 2x as many males than female supers
df4 = pd.read_csv('hero_info.csv', usecols = ["Gender"])

df4.describe()

%matplotlib inline
plt.hist(df4['Gender'], color='orange', edgecolor='black')
plt.xlabel('Gender')
plt.ylabel('Frequency of gender')
plt.title('Gender Distribution')






#Height and Weight correlation scatterplot using seaborn. Inspired from sfu website
df = pd.read_csv('hero_info.csv')
df1=sns.scatterplot(x="Height", y="Weight", data=df); #graphs scatterplot of height vs weight in seaborn
df2=sns.lmplot(x="Height", y="Weight", data=df); #graphs same scatterplot with the line of best fit --> positive correlation
df1.set_title("Height vs. Weight");


#Used another data source (hero_powers)

#describes the total count, unique answers, top result, and frequency of top result in hero_powers.csv --> 
df5 = pd.read_csv('hero_powers.csv', usecols=range(1,167))

df5.describe()



#Going to visualize the frequency of powers with a Bar chart of 'true' and 'false'. 
#shows top 5 rows of the data file 
Power = pd.read_csv('hero_powers.csv')

Power.head()

#storing the first 5 power columns and 5 rows of data into dataframe. #Inspired by website
df = pd.DataFrame({'Aligilty': ['True', 'False', 'True', 'False', 'False'],
                   'Accelerated Healing': ['False', 'True', 'True', 'False', 'True'],
                   'Lantern Power Ring': ['False', 'False', 'False', 'True', 'False'],
                   'Dimentional Awareness': ['False', 'False', 'False', 'False', 'False'], 
                   'Cold Resistance': ['False', 'False', 'True', 'False', 'False']})

#counts total frequency of true and false within the dataframe 'df'
#visualizes the total amount of true and false within the first 5 powers and 5 rows
#-->Accelerated healing for the first 5 heros seems to be the most frequent at 3 trues. 3 have it
#-->On the other hand, Dimentional Awareness is the most rare for the first 5 heros at 5 falses. All 5 do not have it
df1 = df.apply(pd.value_counts)

print(df1)


df1.plot.bar(figsize=(20,20))



#Using correlation matrix to illustrate heatmap of hero powers
Pow = pd.read_csv('hero_powers.csv')

corr = Pow.corr()

sns.heatmap(corr, cmap='Reds', linewidths=.00000000000000001);

#inspired from sfu website on correlation
#Heatmap displays the positive and negative correlations between items in the X and Y Axis. Not all powers are displayed
#The pixels in darker colors indicate that 2 superpowers have a high correlation coefficent 
#The higher the correlation coefficient, the darker the color displayed
#E.g) It seems heros who have Hyperkinesis are most likeley to have Toxin and Disease Resistence in the chart
