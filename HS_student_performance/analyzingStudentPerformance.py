#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 14:00:40 2018

@author: janicelove
"""

import pandas as pd 
from plotnine import *

df = pd.read_csv('StudentsPerformance.csv')
info = df.describe()

#group by gender and describe
dfgender = df.groupby(['gender'])
dfgender.describe() #males had better math scores, females had better writiing and reading

dfParental = df.groupby(['parental level of education'])
dfParental.describe() #in general, mean math scores were higher with college education (except some HS),
#mean reading score was higher, and  mean writing score was higher


dfTestPrep = df.groupby(['test preparation course'])
dfTestPrep.describe() #mean math score higher in completed, mean reading score 
#higher in completed, mean writing score higher in completed 

dfRace = df.groupby(['race/ethnicity'])
dfRace.describe() #mean math scores grp E>D>C>B>A
#mean reading scores grp E>D>C>B>A
#mean writing scores grp E>D>C>B>A

#EXPLORATORY DATA ANALYSIS
#What is the gender distribution of the dataset?
g = (ggplot(df) + aes(x='gender') + geom_histogram())
g.save(filename='genderHisto.png')

#Is there any trend between gender and test scores?
#math scores
'''
p = (ggplot(df) +
     aes(x='gender', y = 'math score', fill = 'parental level of education')+
        geom_jitter())
p.save(filename = 'gendervsMathScoreparental education.png')

#reading scores
q = (ggplot(df) +
     aes(x='gender', y = 'reading score', fill = 'parental level of education')+
        geom_jitter())
q.save(filename = 'gendervsReadingScoreparental education.png')

#writing score
r = (ggplot(df) +
     aes(x='gender', y = 'writing score', fill = 'parental level of education')+
        geom_jitter())
r.save(filename = 'gendervsWritingScoreparental education.png')

#Does taking a test preparation course result in higher scores?
#math scores
p = (ggplot(df) +
     aes(x='test preparation course', y = 'math score', fill = 'gender')+
        geom_jitter())
p.save(filename = 'testprepvsMathScore.png')
#Writing scores
r = (ggplot(df) +
     aes(x='test preparation course', y = 'writing score', fill = 'gender')+
        geom_jitter())
r.save(filename = 'testprepVsWritingScore.png')
'''
'''a = (ggplot(df)+
     aes(x='math score', fill='lunch')+ theme_classic() +
     geom_density(alpha=0.5))
a.save('mathscoreLunchDensity.png')
'''
b  = (ggplot(df)+
     aes(x='math score', fill='gender')+ theme_classic() +
     geom_density(alpha=0.5))
print b

c = (ggplot(df)+
     aes(x='math score', y = 'reading score', fill='gender')+ theme_classic() +
     geom_point())
c.save('mathvsreadingscoreGender.png')

d = (ggplot(df)+
     aes(x='parental level of education', fill = 'lunch')+ theme_classic() +
     geom_bar(position='dodge'))
print d

