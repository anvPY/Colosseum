# This a Book pages blind guessing without knowledge how many pages are in book.

# I have take some randomn guesses in this case 30 samples and use it a data which i have noted in excel.

#Also this is known as "Crowd Computing or Wisdom of crowds  hahaha..."

# I use list data structure to store my data from the sample survey.
from statistics import mean
from scipy import stats

Data_Feed=[200,200,210,225,230,234,
240,240,249,250,250,258,260,264,
270,272,275,275,277,280,280,286,290,
290,298,300,300,310,315,320]
# print(Data_Feed)
# for i in Data_Feed:
#     print(i)
# print("\n")
# print(len(Data_Feed))

# Data_Feed.sort()
x=0
# for i in Data_Feed:
#    x=i+x
#      print(x,i)
# average=x/len(Data_Feed)
# print(average)

#number of values to trim to get more accurate mean
# Here I choose to trim 10 percent from lower values and 10 percent from higher values

# so what is 10 percent from data feed lets find
m=stats.trim_mean(Data_Feed,0.3)
trim_lower_values= int(0.1*len(Data_Feed))
print(trim_lower_values)

Data_Feed=Data_Feed[trim_lower_values:len(Data_Feed)-trim_lower_values]
print(len(Data_Feed))
print(mean(Data_Feed))

for i in Data_Feed:
   x=i+x
   print(x,i)
average=x/len(Data_Feed)
print(average)

