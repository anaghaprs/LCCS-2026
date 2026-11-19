import pandas
import matplotlib.pyplot as plt
import statistics as stat

"""
Title: Applied Learning Task 2
Author: Anagha Prasanth
Date: 17/12/2024 - 8/1/2025
"""

#Question: Does a high literacy rate correlate to high average IQ?
#Min, Max, Median, Mode, Mean, Range
#Visualisation
#Analysis

#Reading the CSV file
litRate = pandas.read_csv('litRate.csv')
#Using the desired labels to create a dataframe
litRateDF = litRate[['Country','Continent', 'Average IQ', 'Literacy Rate']]

#Europe
#Separating each data point by continent
eur = litRateDF[(litRateDF['Continent'] == 'Europe')]
print(eur)
#IQ
#Isolating IQ from data
eurIQ = eur['Average IQ']
print(eurIQ)
#Finding mean of data
avgEURIQ = round(eurIQ.mean(), 2)
print("Average IQ in Europe = ", avgEURIQ)
#Finding max value
print("Highest average IQ in Europe = ", eurIQ.max())
#Finding min value
print("Lowest average IQ in Europe = ", eurIQ.min())
#Finding median
print("Median average IQ in Europe = ", round(eurIQ.median(), 2))
#Finding modal value
print("Modal average IQ in Europe = ", eurIQ.mode())
#Literacy Rate
#Repeating the same from literacy rate
#Isolating literacy rate from data
eurLit = eur['Literacy Rate']
print(eurLit)
#Finding mean of data
avgEURLit = round(eurLit.mean(), 2)
print("Average literacy rate in Europe = ", avgEURLit)
#Finding max value
print("Highest literacy rate in Europe = ", eurLit.max())
#Finding min value
print("Lowest literacy rate in Europe = ", eurLit.min())
#Finding median
print("Median literacy rate in Europe = ", round(eurLit.median(), 2))
#Finding modal value
print("Modal literacy rate in Europe = ", eurLit.mode())

#Asia 
asia = litRateDF[(litRateDF['Continent'] == 'Asia')]
print(asia)
#Average IQ
asiaIQ = asia['Average IQ']
print(asiaIQ)
avgASIAIQ = round(asiaIQ.mean(), 2)
print("Average IQ in Asia = ", avgASIAIQ) 
print("Highest average IQ in Asia = ", asiaIQ.max())
print("Lowest average IQ in Asia = ", asiaIQ.min())
print("Median average IQ in Asia = ", round(asiaIQ.median(), 2))
print("Modal average IQ in Asia = ", asiaIQ.mode())
#Literacy Rate
asiaLit = asia['Literacy Rate']
print(asiaLit)
avgASIALit = round(asiaLit.mean(), 2)
print("Average literacy rate in Asia = ", avgASIALit)
print("Highest literacy rate in Asia = ", asiaLit.max())
print("Lowest literacy rate in Asia = ", asiaLit.min())
print("Median literacy rate in Asia = ", round(asiaLit.median(), 2))
print("Modal literacy rate in Asia = ", asiaLit.mode())

#North America
nAm = litRateDF[(litRateDF['Continent'] == 'North America')]
print(nAm)
#Average IQ
nAmIQ = nAm['Average IQ']
print(nAmIQ)
avgNAMIQ = round(nAmIQ.mean(), 2)
print("Average IQ in North America = ", avgNAMIQ) 
print("Highest average IQ in North America = ", nAmIQ.max())
print("Lowest average IQ in North America = ", nAmIQ.min())
print("Median average IQ in North America = ", round(nAmIQ.median(), 2))
print("Modal average IQ in North America = ", nAmIQ.mode())
#Literacy Rate
nAmLit = nAm['Literacy Rate']
print(asiaLit)
avgNAMLit = round(nAmLit.mean(), 2)
print("Average literacy rate in North America = ", avgNAMLit)
print("Highest literacy rate in North America = ", nAmLit.max())
print("Lowest literacy rate in North America = ", nAmLit.min())
print("Median literacy rate in North America = ", round(nAmLit.median(), 2))
print("Modal literacy rate in North America = ", nAmLit.mode())

#Central America
cAm = litRateDF[(litRateDF['Continent'] == 'Central America')]
print(cAm)
#Average IQ
cAmIQ = cAm['Average IQ']
print(cAmIQ)
avgCAMIQ = round(cAmIQ.mean(), 2)
print("Average IQ in Central America = ", avgCAMIQ) 
print("Highest average IQ in Central America = ", cAmIQ.max())
print("Lowest average IQ in Central America = ", cAmIQ.min())
print("Median average IQ in Central America = ", round(cAmIQ.median(), 2))
print("Modal average IQ in Central America = ", cAmIQ.mode())
#Literacy Rate
cAmLit = cAm['Literacy Rate']
print(cAmLit)
avgCAMLit = round(cAmLit.mean(), 2)
print("Average literacy rate in Central America = ", avgCAMLit)
print("Highest literacy rate in Central America = ", cAmLit.max())
print("Lowest literacy rate in Central America = ", cAmLit.min())
print("Median literacy rate in Central America = ", round(cAmLit.median(), 2))
print("Modal literacy rate in Central America = ", cAmLit.mode())

#South America
sAm = litRateDF[(litRateDF['Continent'] == 'South America')]
print(sAm)
#Average IQ
sAmIQ = sAm['Average IQ']
print(sAmIQ)
avgSAMIQ = round(sAmIQ.mean(), 2)
print("Average IQ in South America = ", avgSAMIQ) 
print("Highest average IQ in South America = ", sAmIQ.max())
print("Lowest average IQ in South America = ", sAmIQ.min())
print("Median average IQ in South America = ", round(sAmIQ.median(), 2))
print("Modal average IQ in South America = ", sAmIQ.mode())
#Literacy Rate
sAmLit = sAm['Literacy Rate']
print(cAmLit)
avgSAMLit = round(sAmLit.mean(), 2)
print("Average literacy rate in South America = ", avgSAMLit)
print("Highest literacy rate in South America = ", sAmLit.max())
print("Lowest literacy rate in South America = ", sAmLit.min())
print("Median literacy rate in South America = ", round(sAmLit.median(), 2))
print("Modal literacy rate in South America = ", sAmLit.mode())


#Oceania
ocea = litRateDF[(litRateDF['Continent'] == 'Oceania')]
print(ocea)
#Average IQ
oceaIQ = ocea['Average IQ']
print(oceaIQ)
avgOCEAIQ = round(oceaIQ.mean(), 2)
print("Average IQ in Oceania = ", avgOCEAIQ) 
print("Highest average IQ in Oceania = ", oceaIQ.max())
print("Lowest average IQ in Oceania = ",oceaIQ.min())
print("Median average IQ in Oceania = ", round(oceaIQ.median(), 2))
print("Modal average IQ in Oceania = ", oceaIQ.mode())
#Literacy Rate
oceaLit = ocea['Literacy Rate']
print(oceaLit)
avgOCEALit = round(oceaLit.mean(), 2)
print("Average literacy rate in Oceania = ", avgOCEALit)
print("Highest literacy rate in Oceania = ", oceaLit.max())
print("Lowest literacy rate in Oceania = ", oceaLit.min())
print("Median literacy rate in Oceania = ", round(oceaLit.median(), 2))
print("Modal literacy rate in Oceania = ", oceaLit.mode())

#Africa
afr = litRateDF[(litRateDF['Continent'] == 'Africa')]
print(afr)
#Average IQ
afrIQ = afr['Average IQ']
print(afrIQ)
avgAFRIQ = round(afrIQ.mean(), 2)
print("Average IQ in Africa = ", avgAFRIQ) 
print("Highest average IQ in Africa = ", afrIQ.max())
print("Lowest average IQ in Africa = ", afrIQ.min())
print("Median average IQ in Africa = ", round(afrIQ.median(), 2))
print("Modal average IQ in Africa = ", afrIQ.mode())
#Literacy Rate
afrLit = afr['Literacy Rate']
print(afrLit)
avgAFRLit = round(afrLit.mean(), 2)
print("Average literacy rate in Africa = ", avgAFRLit)
print("Highest literacy rate in Africa = ", afrLit.max())
print("Lowest literacy rate in Africa = ", afrLit.min())
print("Median literacy rate in Africa = ", round(afrLit.median(), 2))
print("Modal literacy rate in Africa = ", afrLit.mode())

#Printing all final values
print(avgEURIQ, avgASIAIQ, avgOCEAIQ, avgCAMIQ, avgSAMIQ, avgNAMIQ, avgAFRIQ)
print(avgEURLit, avgASIALit, avgOCEALit, avgCAMLit, avgSAMLit, avgNAMLit, avgAFRLit)

#grouping each piece of data
meanIQ = litRate.groupby('Continent')['Average IQ'].mean()
meanLit = litRate.groupby('Continent')['Literacy Rate'].mean()

maxIQ = litRate.groupby('Continent')['Average IQ'].max()
maxLit = litRate.groupby('Continent')['Literacy Rate'].max()

minIQ = litRate.groupby('Continent')['Average IQ'].min()
minLit = litRate.groupby('Continent')['Literacy Rate'].min()

medIQ = litRate.groupby('Continent')['Average IQ'].median()
medLit = litRate.groupby('Continent')['Literacy Rate'].median()

#Combine IQ data into a single dataframe
iq_data = pandas.DataFrame({
    'Mean': meanIQ,
    'Max': maxIQ,
    'Min': minIQ,
    'Median': medIQ,
})

#Combine Literacy Rate data into a single dataframe
lit_data = pandas.DataFrame({
    'Mean': meanLit,
    'Max': maxLit,
    'Min': minLit,
    'Median': medLit,
})

#Set up the figure and subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

#Define bar width and index
bar_width = 0.2
index = range(len(iq_data.index))

#Plot IQ data
axes[0].bar(index, iq_data['Mean'], bar_width, label='Mean')
axes[0].bar([i + bar_width for i in list(index)], iq_data['Max'], bar_width, label='Max')
axes[0].bar([i + 2 * bar_width for i in list(index)], iq_data['Min'], bar_width, label='Min')
axes[0].bar([i + 3 * bar_width for i in list(index)], iq_data['Median'], bar_width, label='Median')

axes[0].set_title('Average IQ by Continent')
axes[0].set_xlabel('Continent')
axes[0].set_ylabel('IQ')
axes[0].set_xticks([i + 1.5 * bar_width for i in list(index)]) 
axes[0].set_xticklabels(iq_data.index)
axes[0].legend()

#Plot literacy rate data
axes[1].bar(index, lit_data['Mean'], bar_width, label='Mean')
axes[1].bar([i + bar_width for i in index], lit_data['Max'], bar_width, label='Max') 
axes[1].bar([i + 2 * bar_width for i in index], lit_data['Min'], bar_width, label='Min')
axes[1].bar([i + 3 * bar_width for i in index], lit_data['Median'], bar_width, label='Median')

axes[1].set_title('Average Literacy Rate by Continent')
axes[1].set_xlabel('Continent')
axes[1].set_ylabel('Literacy Rate')
axes[1].set_xticks([i + 1.5 * bar_width for i in index])
axes[1].set_xticklabels(lit_data.index)
axes[1].legend()

#Adjust layout for better readability
plt.tight_layout()

#Display the plot
plt.show()

