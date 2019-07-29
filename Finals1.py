import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from nltk.tokenize import RegexpTokenizer
import nltk
from nltk.corpus import sentiwordnet as swn
from wordcloud import WordCloud


#Reading the csv file into a dataframw
data = pd.read_csv('final dataset.csv')

#Extracting specific columns from a dataframe into another dataframe
df1 = data.loc[:,["STATNAME", "Total Literacy Rate"]] #Source: https://www.dataquest.io/blog/pandas-python-tutorial/

#Using the groupby fuction to group all the States by the total literacy rate given by each of them and then sorting them into descending order
df2 = df1.groupby('STATNAME').sum().sort_values('Total Literacy Rate', axis = 0, ascending = False).reset_index()

df3 = df2.head(15)
print ('\n\nThe Top 15 states with highest literacy rate are as follows:\n\n')
print (df3)

#Plotting the bar graph
ax = df3[['STATNAME', 'Total Literacy Rate']].plot(kind='bar', title ="Top States with their Literacy Rate", figsize=(15, 10), legend=True, fontsize=12, color = 'orange')
ax.set_xlabel("State Name", fontsize=12)
ax.set_ylabel("Total Literacy Rate", fontsize=12)
x_axis = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
list_customer = df3['STATNAME'].tolist() #Souce: https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
plt.xticks(x_axis, list_customer, rotation = 90)
plt.show()

#Q3: Category of products which have been ordered the most number of times

df14 = data['High or Low'].value_counts()
plt.figure(figsize=(16,8))
ax2 = plt.subplot(111, aspect='equal')

#Plotting the pie chart
df14.plot(kind='pie', autopct='%1.1f%%', startangle=45, shadow=False, legend = True, fontsize=14)
plt.show()


#Finding out total number of primary and upper primary with secondary schools
df4 = data.loc[:,["STATNAME", "Primary Schools"]]
df5 = df4.groupby("STATNAME").sum()
df6 = df5.reset_index()
df7 = df6.loc[df6['Primary Schools'] > 0] #Souce: https://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-pandas?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
df8 = df7.groupby('STATNAME').sum().sort_values('Primary Schools', axis = 0, ascending = False).reset_index()
print ('\n\n-----------------------------------------------------------------------------\n\n')

print ('\n\n\nThe states in which there are highest primary schools are as follows:\n\n')
print (df8)
print ("The top 15 states with highest number of Primary Schools are as follows:\n \n")
print (df8.head(15))

df9 = data.loc[:,["STATNAME", "Upper Primary with secondary"]]
df10 = df9.groupby("STATNAME").sum()
df11 = df10.reset_index()
df12 = df11.loc[df11['Upper Primary with secondary'] > 0] #Souce: https://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-pandas?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
df13 = df12.groupby('STATNAME').sum().sort_values('Upper Primary with secondary', axis = 0, ascending = False).reset_index()
print ('\n\n-----------------------------------------------------------------------------\n\n')

print ('\n\n\nThe states in which there are highest Upper primary with secondary schools are as follows:\n\n')
print (df13)
print ("The top 15 states with highest number of Upper Primary with Secondary Schools are as follows:\n \n")
print (df13.head(15))

x1_axis = []
    
list_state = df7['STATNAME'].tolist() #Source: https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
linecount = -1
for line in list_state:
    linecount = linecount + 1
    x1_axis.append(linecount)
ax1 = df7[['STATNAME', 'Primary Schools']].plot(kind='bar', title ="States in which there are higher number of primary schools", figsize=(15, 10), legend=True, fontsize=12, color = 'red')
ax1.set_xlabel("Statename", fontsize=12)
ax1.set_ylabel("Primary Schools", fontsize=12)
plt.xticks(x1_axis, list_state, rotation = 90)
plt.show()

y1_axis = []
list_state = df13['STATNAME'].tolist() #Source: https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
linecount = -1
for line in list_state:
    linecount = linecount + 1
    y1_axis.append(linecount)
ax1 = df13[['STATNAME', 'Upper Primary with secondary']].plot(kind='bar', title ="States in which there are higher number of Upper Primary with secondary", figsize=(15, 10), legend=True, fontsize=12, color = 'yellow')
ax1.set_xlabel("Statename", fontsize=12)
ax1.set_ylabel("Upper Primary with Secondary Schools", fontsize=12)
plt.xticks(y1_axis, list_state, rotation = 90)
plt.show()

#Q4: Finding out the profits given by each of the customer segments

df15 = data.loc[:,['STATNAME', 'Primary School(Government)']] #Source: https://www.dataquest.io/blog/pandas-python-tutorial/
df16 = df15.groupby('STATNAME').sum().reset_index()

print ('\n\n-----------------------------------------------------------------------------\n\n')

print ('\n\n\nThe states with number of government public schools are:\n\n')
print (df16)
df17 = df16.head(15)

x2_axis = []
    
list_segment = df17['STATNAME'].tolist() #Source: https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
linecount1 = -1
for line in list_segment:
    linecount1 = linecount1 + 1
    x2_axis.append(linecount1)
ax2 = df17[['STATNAME', 'Primary School(Government)']].plot(kind='bar', title ="Primary Government schools", figsize=(15, 10), legend=True, fontsize=12, color = 'g')
ax2.set_xlabel("States", fontsize=12)
ax2.set_ylabel("Schools", fontsize=12)
plt.xticks(x2_axis, list_segment, rotation = 90)
plt.show()


df18 = data.loc[:,['STATNAME', 'Upper Primary with Secondary(government)']] #Source: https://www.dataquest.io/blog/pandas-python-tutorial/
df19 = df18.groupby('STATNAME').sum().reset_index()

print ('\n\n-----------------------------------------------------------------------------\n\n')

print ('\n\n\nThe states with number of government upper primary with secondary schools are:\n\n')
print (df19)
df20 = df19.head(15)

x2_axis = []
    
list_segment = df20['STATNAME'].tolist() #Source: https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
linecount1 = -1
for line in list_segment:
    linecount1 = linecount1 + 1
    x2_axis.append(linecount1)
ax2 = df20[['STATNAME', 'Upper Primary with Secondary(government)']].plot(kind='bar', title ="Upper Primary with Secondary Government schools", figsize=(15, 10), legend=True, fontsize=12, color = 'pink')
ax2.set_xlabel("States", fontsize=12)
ax2.set_ylabel("Schools", fontsize=12)
plt.xticks(x2_axis, list_segment, rotation = 90)
plt.show()

df21 = data.loc[:,['STATNAME', 'Primary School(private)']] #Source: https://www.dataquest.io/blog/pandas-python-tutorial/
df22 = df21.groupby('STATNAME').sum().reset_index()

print ('\n\n-----------------------------------------------------------------------------\n\n')

print ('\n\n\nThe states with number of private primary schools are:\n\n')
print (df22)
df23 = df22.head(15)

x2_axis = []
    
list_segment = df23['STATNAME'].tolist() #Source: https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
linecount1 = -1
for line in list_segment:
    linecount1 = linecount1 + 1
    x2_axis.append(linecount1)
ax2 = df23[['STATNAME', 'Primary School(private)']].plot(kind='bar', title ="Private Primary schools", figsize=(15, 10), legend=True, fontsize=12, color = 'purple')
ax2.set_xlabel("States", fontsize=12)
ax2.set_ylabel("Schools", fontsize=12)
plt.xticks(x2_axis, list_segment, rotation = 90)
plt.show()

df24 = data.loc[:,['STATNAME', 'Upper primary with secondary(private)']] #Source: https://www.dataquest.io/blog/pandas-python-tutorial/
df25 = df24.groupby('STATNAME').sum().reset_index()

print ('\n\n-----------------------------------------------------------------------------\n\n')

print ('\n\n\nThe states with number of private upper primary with secondary schools are:\n\n')
print (df25)
df26 = df25.head(15)

x2_axis = []
    
list_segment = df26['STATNAME'].tolist() #Source: https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
linecount1 = -1
for line in list_segment:
    linecount1 = linecount1 + 1
    x2_axis.append(linecount1)
ax2 = df26[['STATNAME', 'Upper primary with secondary(private)']].plot(kind='bar', title ="Upper Primary with secondry private schools", figsize=(15, 10), legend=True, fontsize=12, color = 'brown')
ax2.set_xlabel("States", fontsize=12)
ax2.set_ylabel("Schools", fontsize=12)
plt.xticks(x2_axis, list_segment, rotation = 90)
plt.show()

df27 = data.loc[:,['STATNAME', 'Primary School(Schools approachabe by all weather road)']] #Source: https://www.dataquest.io/blog/pandas-python-tutorial/
df28 = df27.groupby('STATNAME').sum().reset_index()

print ('\n\n-----------------------------------------------------------------------------\n\n')

print ('\n\n\nThe states with number of primary schools that are approachable by all weather are:\n\n')
print (df28)
df29 = df28.head(15)

x2_axis = []
    
list_segment = df29['STATNAME'].tolist() #Source: https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
linecount1 = -1
for line in list_segment:
    linecount1 = linecount1 + 1
    x2_axis.append(linecount1)
ax2 = df29[['STATNAME', 'Primary School(Schools approachabe by all weather road)']].plot(kind='bar', title ="Primary schools approachable by all weather", figsize=(15, 10), legend=True, fontsize=12, color = 'turquoise')
ax2.set_xlabel("States", fontsize=12)
ax2.set_ylabel("Schools", fontsize=12)
plt.xticks(x2_axis, list_segment, rotation = 90)
plt.show()

df30 = data.loc[:,['STATNAME', 'Upper primary with secondary(Schools approachabe by all weather road)']] #Source: https://www.dataquest.io/blog/pandas-python-tutorial/
df31 = df30.groupby('STATNAME').sum().reset_index()

print ('\n\n-----------------------------------------------------------------------------\n\n')

print ('\n\n\nThe states with number of upper primary with secondary schools that are approachable in all weather are:\n\n')
print (df31)
df32 = df31.head(15)

x2_axis = []
    
list_segment = df32['STATNAME'].tolist() #Source: https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
linecount1 = -1
for line in list_segment:
    linecount1 = linecount1 + 1
    x2_axis.append(linecount1)
ax2 = df32[['STATNAME', 'Upper primary with secondary(Schools approachabe by all weather road)']].plot(kind='bar', title ="Upper Primary with secondary schools approachable by all weather", figsize=(15, 10), legend=True, fontsize=12, color = 'grey')
ax2.set_xlabel("States", fontsize=12)
ax2.set_ylabel("Schools", fontsize=12)
plt.xticks(x2_axis, list_segment, rotation = 90)
plt.show()

df33 = data.loc[:,['STATNAME', 'Primary Schools(with electricity)']] #Source: https://www.dataquest.io/blog/pandas-python-tutorial/
df34 = df33.groupby('STATNAME').sum().reset_index()

print ('\n\n-----------------------------------------------------------------------------\n\n')

print ('\n\n\nThe states with number of primary schools with electricity are:\n\n')
print (df34)
df35 = df34.head(15)

x2_axis = []
    
list_segment = df35['STATNAME'].tolist() #Source: https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
linecount1 = -1
for line in list_segment:
    linecount1 = linecount1 + 1
    x2_axis.append(linecount1)
ax2 = df35[['STATNAME', 'Primary Schools(with electricity)']].plot(kind='bar', title ="Primary schools with electricity", figsize=(15, 10), legend=True, fontsize=12, color = 'blue')
ax2.set_xlabel("States", fontsize=12)
ax2.set_ylabel("Schools", fontsize=12)
plt.xticks(x2_axis, list_segment, rotation = 90)
plt.show()

df36 = data.loc[:,['STATNAME', 'Upper primary with secondary(with electricity)']] #Source: https://www.dataquest.io/blog/pandas-python-tutorial/
df37 = df36.groupby('STATNAME').sum().reset_index()

print ('\n\n-----------------------------------------------------------------------------\n\n')

print ('\n\n\nThe states with number of upper primary with secondary schools with electricity are:\n\n')
print (df37)
df38 = df37.head(15)

x2_axis = []
    
list_segment = df38['STATNAME'].tolist() #Source: https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
linecount1 = -1
for line in list_segment:
    linecount1 = linecount1 + 1
    x2_axis.append(linecount1)
ax2 = df38[['STATNAME', 'Upper primary with secondary(with electricity)']].plot(kind='bar', title ="Upper Primary with secondary schools with electricity", figsize=(15, 10), legend=True, fontsize=12, color = 'teal')
ax2.set_xlabel("States", fontsize=12)
ax2.set_ylabel("Schools", fontsize=12)
plt.xticks(x2_axis, list_segment, rotation = 90)
plt.show()

df39 = data.loc[:,['STATNAME', 'Primary schools(need major repair)']] #Source: https://www.dataquest.io/blog/pandas-python-tutorial/
df40 = df39.groupby('STATNAME').sum().reset_index()

print ('\n\n-----------------------------------------------------------------------------\n\n')

print ('\n\n\nThe states with number of primary schools that needs major repair are:\n\n')
print (df40)
df41 = df40.head(15)

x2_axis = []
    
list_segment = df41['STATNAME'].tolist() #Source: https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
linecount1 = -1
for line in list_segment:
    linecount1 = linecount1 + 1
    x2_axis.append(linecount1)
ax2 = df41[['STATNAME', 'Primary schools(need major repair)']].plot(kind='bar', title ="Primary schools(need major repair)", figsize=(15, 10), legend=True, fontsize=12, color = 'orange')
ax2.set_xlabel("States", fontsize=12)
ax2.set_ylabel("Schools", fontsize=12)
plt.xticks(x2_axis, list_segment, rotation = 90)
plt.show()

df42 = data.loc[:,['STATNAME', 'Upper primary with secondary(need major repair)']] #Source: https://www.dataquest.io/blog/pandas-python-tutorial/
df43 = df42.groupby('STATNAME').sum().reset_index()

print ('\n\n-----------------------------------------------------------------------------\n\n')

print ('\n\n\nThe states with number of upper primary with secondary schools that needs major repair are:\n\n')
print (df43)
df44 = df43.head(15)

x2_axis = []
    
list_segment = df44['STATNAME'].tolist() #Source: https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
linecount1 = -1
for line in list_segment:
    linecount1 = linecount1 + 1
    x2_axis.append(linecount1)
ax2 = df44[['STATNAME', 'Upper primary with secondary(need major repair)']].plot(kind='bar', title ="Upper primary with secondary(need major repair)", figsize=(15, 10), legend=True, fontsize=12, color = 'violet')
ax2.set_xlabel("States", fontsize=12)
ax2.set_ylabel("Schools", fontsize=12)
plt.xticks(x2_axis, list_segment, rotation = 90)
plt.show()
#wordCloud and sentimental analysis
#Importing the sentimental comments and stopwords file.
file1 = open("senti.txt", "r")

cf = open("stopwords_en.txt", "r")

#Using regular expressions form nltk
tokenizer = RegexpTokenizer(r'\w+')

#Reading the input files and converting them to lower case

conslower = file1.read().lower()
read = cf.read().lower()

#Replacing the new line command with space ("\n" to " ")

consreplace = conslower.replace("\n", " ")
read = read.replace("\n", " ")

#Removing Punctuations and tokenizing

cons_read = tokenizer.tokenize(consreplace)
read = tokenizer.tokenize(read)


#Removing numerial data

numberscon = []

for j in cons_read:
	if j.isdigit() == False:
		numberscon.append(j)

#Removing stopwords
cleancon = []

for j in numberscon:
	if j not in read:
		cleancon.append(j)
 
#Creating bigrams       

bigrammed_cons = list(nltk.bigrams(cleancon))

#Creating a string of all the cleaned text

con_data = " ".join(cleancon)

#Plotting a WordCloud of all the Cleaned Cons text
plt.figure()
wc = WordCloud(background_color="white", max_words=100)
wc.generate(con_data)
wc.to_file('Pro.png')
plt.title("Comments - WordCloud")
plt.imshow(wc)
plt.axis('off')
plt.show()

#Sentiment Calculation

Negscore_Con = 0
PosScore_Con = 0



for j in cleancon:
    try:
        sentiment_pos = swn.senti_synset(j + '.n.01').pos_score()
        PosScore_Con += sentiment_pos
        sentiment_con = swn.senti_synset(j + '.n.01').neg_score()
        Negscore_Con += sentiment_con
    except:
        try:
            sentiment_pos = swn.senti_synset(j + '.v.01').pos_score()
            PosScore_Con += sentiment_pos
            sentiment_con = swn.senti_synset(j + '.v.01').neg_score()
            Negscore_Con += sentiment_con
        except:
            try:
                sentiment_pos = swn.senti_synset(j + '.a.02').pos_score()
                PosScore_Pro += sentiment_pos
                sentiment_con = swn.senti_synset(j + '.a.02').neg_score()
                Negscore_Con += sentiment_con
            except:
                try:
                    sentiment_pos = swn.senti_synset(j + '.s.02').pos_score()
                    PosScore_Con += sentiment_pos
                    sentiment_con = swn.senti_synset(j + '.s.02').neg_score()
                    Negscore_Con += sentiment_con
                except:
                    try:
                        sentiment_pos = swn.senti_synset(j + '.r.02').pos_score()
                        PosScore_Con += sentiment_pos
                        sentiment_con = swn.senti_synset(j + '.r.02').neg_score()
                        Negscore_Con += sentiment_con
                    except:
                        continue

print "---------------------------"
print "Total of Negative Score of all the comments are:", PosScore_Con
print "Total of Positive Score of all the comments are:", Negscore_Con
print "---------------------------"