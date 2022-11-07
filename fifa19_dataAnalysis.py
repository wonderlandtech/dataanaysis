#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from IPython.display import display


# In[71]:


data = pd.read_csv('fifa19.csv')
display(data)


# In[52]:


data.columns


# In[55]:


data.columns.shape


# In[ ]:





# In[ ]:





# In[9]:


data[['ID','Name','Age']].loc[18000:18207].to_json(r'C:\Users\WONDER BASSEY PAUL\Desktop\_\files\export_dataframe2.json', orient='split')


# In[14]:


import json as js


# In[28]:


with open("export_dataframe2.json") as df:
    df = pd.read_csv('export_dataframe2.json')
    df


# In[29]:


df.pop('Name')


# In[30]:





# In[ ]:





# In[ ]:





# In[6]:


shape = data.shape
shape


# In[10]:


total_columns = data.columns
display(total_columns)


# In[14]:


display(data.values)


# In[58]:


data.Nationality = 'Nigeria'
data


# In[33]:


data.pop('Name')


# In[43]:


df =data[['Potential','Overall']]
df


# In[44]:


df['Olu'] = data['Age'].astype(str) +" " + data['Nationality']
df


# In[7]:


csv_filename = 'fifa19.csv'

with open(csv_filename) as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        print(row)


# In[9]:


dicte = {'ï»¿': '0', 'ID': '158023', 'Name': 'L. Messi', 'Age': '31', 'Photo': 'https://cdn.sofifa.org/players/4/19/158023.png', 'Nationality': 'Argentina', 'Flag': 'https://cdn.sofifa.org/flags/52.png', 'Overall': '94', 'Potential': '94', 'Club': 'FC Barcelona', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/241.png', 'Value': 'â‚¬110.5M', 'Wage': 'â‚¬565K', 'Special': '2202', 'Preferred Foot': 'Left', 'International Reputation': '5', 'Weak Foot': '4', 'Skill Moves': '4', 'Work Rate': 'Medium/ Medium', 'Body Type': 'Messi', 'Real Face': 'Yes', 'Position': 'RF', 'Jersey Number': '10', 'Joined': 'Jul 1, 2004', 'Loaned From': '', 'Contract Valid Until': '2021', 'Height': "5'7", 'Weight': '159lbs', 'LS': '88+2', 'ST': '88+2', 'RS': '88+2', 'LW': '92+2', 'LF': '93+2', 'CF': '93+2', 'RF': '93+2', 'RW': '92+2', 'LAM': '93+2', 'CAM': '93+2', 'RAM': '93+2', 'LM': '91+2', 'LCM': '84+2', 'CM': '84+2', 'RCM': '84+2', 'RM': '91+2', 'LWB': '64+2', 'LDM': '61+2', 'CDM': '61+2', 'RDM': '61+2', 'RWB': '64+2', 'LB': '59+2', 'LCB': '47+2', 'CB': '47+2', 'RCB': '47+2', 'RB': '59+2', 'Crossing': '84', 'Finishing': '95', 'HeadingAccuracy': '70', 'ShortPassing': '90', 'Volleys': '86', 'Dribbling': '97', 'Curve': '93', 'FKAccuracy': '94', 'LongPassing': '87', 'BallControl': '96', 'Acceleration': '91', 'SprintSpeed': '86', 'Agility': '91', 'Reactions': '95', 'Balance': '95', 'ShotPower': '85', 'Jumping': '68', 'Stamina': '72', 'Strength': '59', 'LongShots': '94', 'Aggression': '48', 'Interceptions': '22', 'Positioning': '94', 'Vision': '94', 'Penalties': '75', 'Composure': '96', 'Marking': '33', 'StandingTackle': '28', 'SlidingTackle': '26', 'GKDiving': '6', 'GKHandling': '11', 'GKKicking': '15', 'GKPositioning': '14', 'GKReflexes': '8', 'Release Clause': 'â‚¬226.5M'}
{'ï»¿': '1', 'ID': '20801', 'Name': 'Cristiano Ronaldo', 'Age': '33', 'Photo': 'https://cdn.sofifa.org/players/4/19/20801.png', 'Nationality': 'Portugal', 'Flag': 'https://cdn.sofifa.org/flags/38.png', 'Overall': '94', 'Potential': '94', 'Club': 'Juventus', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/45.png', 'Value': 'â‚¬77M', 'Wage': 'â‚¬405K', 'Special': '2228', 'Preferred Foot': 'Right', 'International Reputation': '5', 'Weak Foot': '4', 'Skill Moves': '5', 'Work Rate': 'High/ Low', 'Body Type': 'C. Ronaldo', 'Real Face': 'Yes', 'Position': 'ST', 'Jersey Number': '7', 'Joined': 'Jul 10, 2018', 'Loaned From': '', 'Contract Valid Until': '2022', 'Height': "6'2", 'Weight': '183lbs', 'LS': '91+3', 'ST': '91+3', 'RS': '91+3', 'LW': '89+3', 'LF': '90+3', 'CF': '90+3', 'RF': '90+3', 'RW': '89+3', 'LAM': '88+3', 'CAM': '88+3', 'RAM': '88+3', 'LM': '88+3', 'LCM': '81+3', 'CM': '81+3', 'RCM': '81+3', 'RM': '88+3', 'LWB': '65+3', 'LDM': '61+3', 'CDM': '61+3', 'RDM': '61+3', 'RWB': '65+3', 'LB': '61+3', 'LCB': '53+3', 'CB': '53+3', 'RCB': '53+3', 'RB': '61+3', 'Crossing': '84', 'Finishing': '94', 'HeadingAccuracy': '89', 'ShortPassing': '81', 'Volleys': '87', 'Dribbling': '88', 'Curve': '81', 'FKAccuracy': '76', 'LongPassing': '77', 'BallControl': '94', 'Acceleration': '89', 'SprintSpeed': '91', 'Agility': '87', 'Reactions': '96', 'Balance': '70', 'ShotPower': '95', 'Jumping': '95', 'Stamina': '88', 'Strength': '79', 'LongShots': '93', 'Aggression': '63', 'Interceptions': '29', 'Positioning': '95', 'Vision': '82', 'Penalties': '85', 'Composure': '95', 'Marking': '28', 'StandingTackle': '31', 'SlidingTackle': '23', 'GKDiving': '7', 'GKHandling': '11', 'GKKicking': '15', 'GKPositioning': '14', 'GKReflexes': '11', 'Release Clause': 'â‚¬127.1M'}
{'ï»¿': '2', 'ID': '190871', 'Name': 'Neymar Jr', 'Age': '26', 'Photo': 'https://cdn.sofifa.org/players/4/19/190871.png', 'Nationality': 'Brazil', 'Flag': 'https://cdn.sofifa.org/flags/54.png', 'Overall': '92', 'Potential': '93', 'Club': 'Paris Saint-Germain', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/73.png', 'Value': 'â‚¬118.5M', 'Wage': 'â‚¬290K', 'Special': '2143', 'Preferred Foot': 'Right', 'International Reputation': '5', 'Weak Foot': '5', 'Skill Moves': '5', 'Work Rate': 'High/ Medium', 'Body Type': 'Neymar', 'Real Face': 'Yes', 'Position': 'LW', 'Jersey Number': '10', 'Joined': 'Aug 3, 2017', 'Loaned From': '', 'Contract Valid Until': '2022', 'Height': "5'9", 'Weight': '150lbs', 'LS': '84+3', 'ST': '84+3', 'RS': '84+3', 'LW': '89+3', 'LF': '89+3', 'CF': '89+3', 'RF': '89+3', 'RW': '89+3', 'LAM': '89+3', 'CAM': '89+3', 'RAM': '89+3', 'LM': '88+3', 'LCM': '81+3', 'CM': '81+3', 'RCM': '81+3', 'RM': '88+3', 'LWB': '65+3', 'LDM': '60+3', 'CDM': '60+3', 'RDM': '60+3', 'RWB': '65+3', 'LB': '60+3', 'LCB': '47+3', 'CB': '47+3', 'RCB': '47+3', 'RB': '60+3', 'Crossing': '79', 'Finishing': '87', 'HeadingAccuracy': '62', 'ShortPassing': '84', 'Volleys': '84', 'Dribbling': '96', 'Curve': '88', 'FKAccuracy': '87', 'LongPassing': '78', 'BallControl': '95', 'Acceleration': '94', 'SprintSpeed': '90', 'Agility': '96', 'Reactions': '94', 'Balance': '84', 'ShotPower': '80', 'Jumping': '61', 'Stamina': '81', 'Strength': '49', 'LongShots': '82', 'Aggression': '56', 'Interceptions': '36', 'Positioning': '89', 'Vision': '87', 'Penalties': '81', 'Composure': '94', 'Marking': '27', 'StandingTackle': '24', 'SlidingTackle': '33', 'GKDiving': '9', 'GKHandling': '9', 'GKKicking': '15', 'GKPositioning': '15', 'GKReflexes': '11', 'Release Clause': 'â‚¬228.1M'}
{'ï»¿': '3', 'ID': '193080', 'Name': 'De Gea', 'Age': '27', 'Photo': 'https://cdn.sofifa.org/players/4/19/193080.png', 'Nationality': 'Spain', 'Flag': 'https://cdn.sofifa.org/flags/45.png', 'Overall': '91', 'Potential': '93', 'Club': 'Manchester United', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/11.png', 'Value': 'â‚¬72M', 'Wage': 'â‚¬260K', 'Special': '1471', 'Preferred Foot': 'Right', 'International Reputation': '4', 'Weak Foot': '3', 'Skill Moves': '1', 'Work Rate': 'Medium/ Medium', 'Body Type': 'Lean', 'Real Face': 'Yes', 'Position': 'GK', 'Jersey Number': '1', 'Joined': 'Jul 1, 2011', 'Loaned From': '', 'Contract Valid Until': '2020', 'Height': "6'4", 'Weight': '168lbs', 'LS': '', 'ST': '', 'RS': '', 'LW': '', 'LF': '', 'CF': '', 'RF': '', 'RW': '', 'LAM': '', 'CAM': '', 'RAM': '', 'LM': '', 'LCM': '', 'CM': '', 'RCM': '', 'RM': '', 'LWB': '', 'LDM': '', 'CDM': '', 'RDM': '', 'RWB': '', 'LB': '', 'LCB': '', 'CB': '', 'RCB': '', 'RB': '', 'Crossing': '17', 'Finishing': '13', 'HeadingAccuracy': '21', 'ShortPassing': '50', 'Volleys': '13', 'Dribbling': '18', 'Curve': '21', 'FKAccuracy': '19', 'LongPassing': '51', 'BallControl': '42', 'Acceleration': '57', 'SprintSpeed': '58', 'Agility': '60', 'Reactions': '90', 'Balance': '43', 'ShotPower': '31', 'Jumping': '67', 'Stamina': '43', 'Strength': '64', 'LongShots': '12', 'Aggression': '38', 'Interceptions': '30', 'Positioning': '12', 'Vision': '68', 'Penalties': '40', 'Composure': '68', 'Marking': '15', 'StandingTackle': '21', 'SlidingTackle': '13', 'GKDiving': '90', 'GKHandling': '85', 'GKKicking': '87', 'GKPositioning': '88', 'GKReflexes': '94', 'Release Clause': 'â‚¬138.6M'}
{'ï»¿': '4', 'ID': '192985', 'Name': 'K. De Bruyne', 'Age': '27', 'Photo': 'https://cdn.sofifa.org/players/4/19/192985.png', 'Nationality': 'Belgium', 'Flag': 'https://cdn.sofifa.org/flags/7.png', 'Overall': '91', 'Potential': '92', 'Club': 'Manchester City', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/10.png', 'Value': 'â‚¬102M', 'Wage': 'â‚¬355K', 'Special': '2281', 'Preferred Foot': 'Right', 'International Reputation': '4', 'Weak Foot': '5', 'Skill Moves': '4', 'Work Rate': 'High/ High', 'Body Type': 'Normal', 'Real Face': 'Yes', 'Position': 'RCM', 'Jersey Number': '7', 'Joined': 'Aug 30, 2015', 'Loaned From': '', 'Contract Valid Until': '2023', 'Height': "5'11", 'Weight': '154lbs', 'LS': '82+3', 'ST': '82+3', 'RS': '82+3', 'LW': '87+3', 'LF': '87+3', 'CF': '87+3', 'RF': '87+3', 'RW': '87+3', 'LAM': '88+3', 'CAM': '88+3', 'RAM': '88+3', 'LM': '88+3', 'LCM': '87+3', 'CM': '87+3', 'RCM': '87+3', 'RM': '88+3', 'LWB': '77+3', 'LDM': '77+3', 'CDM': '77+3', 'RDM': '77+3', 'RWB': '77+3', 'LB': '73+3', 'LCB': '66+3', 'CB': '66+3', 'RCB': '66+3', 'RB': '73+3', 'Crossing': '93', 'Finishing': '82', 'HeadingAccuracy': '55', 'ShortPassing': '92', 'Volleys': '82', 'Dribbling': '86', 'Curve': '85', 'FKAccuracy': '83', 'LongPassing': '91', 'BallControl': '91', 'Acceleration': '78', 'SprintSpeed': '76', 'Agility': '79', 'Reactions': '91', 'Balance': '77', 'ShotPower': '91', 'Jumping': '63', 'Stamina': '90', 'Strength': '75', 'LongShots': '91', 'Aggression': '76', 'Interceptions': '61', 'Positioning': '87', 'Vision': '94', 'Penalties': '79', 'Composure': '88', 'Marking': '68', 'StandingTackle': '58', 'SlidingTackle': '51', 'GKDiving': '15', 'GKHandling': '13', 'GKKicking': '5', 'GKPositioning': '10', 'GKReflexes': '13', 'Release Clause': 'â‚¬196.4M'}
{'ï»¿': '5', 'ID': '183277', 'Name': 'E. Hazard', 'Age': '27', 'Photo': 'https://cdn.sofifa.org/players/4/19/183277.png', 'Nationality': 'Belgium', 'Flag': 'https://cdn.sofifa.org/flags/7.png', 'Overall': '91', 'Potential': '91', 'Club': 'Chelsea', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/5.png', 'Value': 'â‚¬93M', 'Wage': 'â‚¬340K', 'Special': '2142', 'Preferred Foot': 'Right', 'International Reputation': '4', 'Weak Foot': '4', 'Skill Moves': '4', 'Work Rate': 'High/ Medium', 'Body Type': 'Normal', 'Real Face': 'Yes', 'Position': 'LF', 'Jersey Number': '10', 'Joined': 'Jul 1, 2012', 'Loaned From': '', 'Contract Valid Until': '2020', 'Height': "5'8", 'Weight': '163lbs', 'LS': '83+3', 'ST': '83+3', 'RS': '83+3', 'LW': '89+3', 'LF': '88+3', 'CF': '88+3', 'RF': '88+3', 'RW': '89+3', 'LAM': '89+3', 'CAM': '89+3', 'RAM': '89+3', 'LM': '89+3', 'LCM': '82+3', 'CM': '82+3', 'RCM': '82+3', 'RM': '89+3', 'LWB': '66+3', 'LDM': '63+3', 'CDM': '63+3', 'RDM': '63+3', 'RWB': '66+3', 'LB': '60+3', 'LCB': '49+3', 'CB': '49+3', 'RCB': '49+3', 'RB': '60+3', 'Crossing': '81', 'Finishing': '84', 'HeadingAccuracy': '61', 'ShortPassing': '89', 'Volleys': '80', 'Dribbling': '95', 'Curve': '83', 'FKAccuracy': '79', 'LongPassing': '83', 'BallControl': '94', 'Acceleration': '94', 'SprintSpeed': '88', 'Agility': '95', 'Reactions': '90', 'Balance': '94', 'ShotPower': '82', 'Jumping': '56', 'Stamina': '83', 'Strength': '66', 'LongShots': '80', 'Aggression': '54', 'Interceptions': '41', 'Positioning': '87', 'Vision': '89', 'Penalties': '86', 'Composure': '91', 'Marking': '34', 'StandingTackle': '27', 'SlidingTackle': '22', 'GKDiving': '11', 'GKHandling': '12', 'GKKicking': '6', 'GKPositioning': '8', 'GKReflexes': '8', 'Release Clause': 'â‚¬172.1M'}
{'ï»¿': '6', 'ID': '177003', 'Name': 'L. ModriÄ‡', 'Age': '32', 'Photo': 'https://cdn.sofifa.org/players/4/19/177003.png', 'Nationality': 'Croatia', 'Flag': 'https://cdn.sofifa.org/flags/10.png', 'Overall': '91', 'Potential': '91', 'Club': 'Real Madrid', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/243.png', 'Value': 'â‚¬67M', 'Wage': 'â‚¬420K', 'Special': '2280', 'Preferred Foot': 'Right', 'International Reputation': '4', 'Weak Foot': '4', 'Skill Moves': '4', 'Work Rate': 'High/ High', 'Body Type': 'Lean', 'Real Face': 'Yes', 'Position': 'RCM', 'Jersey Number': '10', 'Joined': 'Aug 1, 2012', 'Loaned From': '', 'Contract Valid Until': '2020', 'Height': "5'8", 'Weight': '146lbs', 'LS': '77+3', 'ST': '77+3', 'RS': '77+3', 'LW': '85+3', 'LF': '84+3', 'CF': '84+3', 'RF': '84+3', 'RW': '85+3', 'LAM': '87+3', 'CAM': '87+3', 'RAM': '87+3', 'LM': '86+3', 'LCM': '88+3', 'CM': '88+3', 'RCM': '88+3', 'RM': '86+3', 'LWB': '82+3', 'LDM': '81+3', 'CDM': '81+3', 'RDM': '81+3', 'RWB': '82+3', 'LB': '79+3', 'LCB': '71+3', 'CB': '71+3', 'RCB': '71+3', 'RB': '79+3', 'Crossing': '86', 'Finishing': '72', 'HeadingAccuracy': '55', 'ShortPassing': '93', 'Volleys': '76', 'Dribbling': '90', 'Curve': '85', 'FKAccuracy': '78', 'LongPassing': '88', 'BallControl': '93', 'Acceleration': '80', 'SprintSpeed': '72', 'Agility': '93', 'Reactions': '90', 'Balance': '94', 'ShotPower': '79', 'Jumping': '68', 'Stamina': '89', 'Strength': '58', 'LongShots': '82', 'Aggression': '62', 'Interceptions': '83', 'Positioning': '79', 'Vision': '92', 'Penalties': '82', 'Composure': '84', 'Marking': '60', 'StandingTackle': '76', 'SlidingTackle': '73', 'GKDiving': '13', 'GKHandling': '9', 'GKKicking': '7', 'GKPositioning': '14', 'GKReflexes': '9', 'Release Clause': 'â‚¬137.4M'}
{'ï»¿': '7', 'ID': '176580', 'Name': 'L. SuÃ¡rez', 'Age': '31', 'Photo': 'https://cdn.sofifa.org/players/4/19/176580.png', 'Nationality': 'Uruguay', 'Flag': 'https://cdn.sofifa.org/flags/60.png', 'Overall': '91', 'Potential': '91', 'Club': 'FC Barcelona', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/241.png', 'Value': 'â‚¬80M', 'Wage': 'â‚¬455K', 'Special': '2346', 'Preferred Foot': 'Right', 'International Reputation': '5', 'Weak Foot': '4', 'Skill Moves': '3', 'Work Rate': 'High/ Medium', 'Body Type': 'Normal', 'Real Face': 'Yes', 'Position': 'RS', 'Jersey Number': '9', 'Joined': 'Jul 11, 2014', 'Loaned From': '', 'Contract Valid Until': '2021', 'Height': "6'0", 'Weight': '190lbs', 'LS': '87+5', 'ST': '87+5', 'RS': '87+5', 'LW': '86+5', 'LF': '87+5', 'CF': '87+5', 'RF': '87+5', 'RW': '86+5', 'LAM': '85+5', 'CAM': '85+5', 'RAM': '85+5', 'LM': '84+5', 'LCM': '79+5', 'CM': '79+5', 'RCM': '79+5', 'RM': '84+5', 'LWB': '69+5', 'LDM': '68+5', 'CDM': '68+5', 'RDM': '68+5', 'RWB': '69+5', 'LB': '66+5', 'LCB': '63+5', 'CB': '63+5', 'RCB': '63+5', 'RB': '66+5', 'Crossing': '77', 'Finishing': '93', 'HeadingAccuracy': '77', 'ShortPassing': '82', 'Volleys': '88', 'Dribbling': '87', 'Curve': '86', 'FKAccuracy': '84', 'LongPassing': '64', 'BallControl': '90', 'Acceleration': '86', 'SprintSpeed': '75', 'Agility': '82', 'Reactions': '92', 'Balance': '83', 'ShotPower': '86', 'Jumping': '69', 'Stamina': '90', 'Strength': '83', 'LongShots': '85', 'Aggression': '87', 'Interceptions': '41', 'Positioning': '92', 'Vision': '84', 'Penalties': '85', 'Composure': '85', 'Marking': '62', 'StandingTackle': '45', 'SlidingTackle': '38', 'GKDiving': '27', 'GKHandling': '25', 'GKKicking': '31', 'GKPositioning': '33', 'GKReflexes': '37', 'Release Clause': 'â‚¬164M'}
{'ï»¿': '8', 'ID': '155862', 'Name': 'Sergio Ramos', 'Age': '32', 'Photo': 'https://cdn.sofifa.org/players/4/19/155862.png', 'Nationality': 'Spain', 'Flag': 'https://cdn.sofifa.org/flags/45.png', 'Overall': '91', 'Potential': '91', 'Club': 'Real Madrid', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/243.png', 'Value': 'â‚¬51M', 'Wage': 'â‚¬380K', 'Special': '2201', 'Preferred Foot': 'Right', 'International Reputation': '4', 'Weak Foot': '3', 'Skill Moves': '3', 'Work Rate': 'High/ Medium', 'Body Type': 'Normal', 'Real Face': 'Yes', 'Position': 'RCB', 'Jersey Number': '15', 'Joined': 'Aug 1, 2005', 'Loaned From': '', 'Contract Valid Until': '2020', 'Height': "6'0", 'Weight': '181lbs', 'LS': '73+3', 'ST': '73+3', 'RS': '73+3', 'LW': '70+3', 'LF': '71+3', 'CF': '71+3', 'RF': '71+3', 'RW': '70+3', 'LAM': '71+3', 'CAM': '71+3', 'RAM': '71+3', 'LM': '72+3', 'LCM': '75+3', 'CM': '75+3', 'RCM': '75+3', 'RM': '72+3', 'LWB': '81+3', 'LDM': '84+3', 'CDM': '84+3', 'RDM': '84+3', 'RWB': '81+3', 'LB': '84+3', 'LCB': '87+3', 'CB': '87+3', 'RCB': '87+3', 'RB': '84+3', 'Crossing': '66', 'Finishing': '60', 'HeadingAccuracy': '91', 'ShortPassing': '78', 'Volleys': '66', 'Dribbling': '63', 'Curve': '74', 'FKAccuracy': '72', 'LongPassing': '77', 'BallControl': '84', 'Acceleration': '76', 'SprintSpeed': '75', 'Agility': '78', 'Reactions': '85', 'Balance': '66', 'ShotPower': '79', 'Jumping': '93', 'Stamina': '84', 'Strength': '83', 'LongShots': '59', 'Aggression': '88', 'Interceptions': '90', 'Positioning': '60', 'Vision': '63', 'Penalties': '75', 'Composure': '82', 'Marking': '87', 'StandingTackle': '92', 'SlidingTackle': '91', 'GKDiving': '11', 'GKHandling': '8', 'GKKicking': '9', 'GKPositioning': '7', 'GKReflexes': '11', 'Release Clause': 'â‚¬104.6M'}
{'ï»¿': '9', 'ID': '200389', 'Name': 'J. Oblak', 'Age': '25', 'Photo': 'https://cdn.sofifa.org/players/4/19/200389.png', 'Nationality': 'Slovenia', 'Flag': 'https://cdn.sofifa.org/flags/44.png', 'Overall': '90', 'Potential': '93', 'Club': 'AtlÃ©tico Madrid', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/240.png', 'Value': 'â‚¬68M', 'Wage': 'â‚¬94K', 'Special': '1331', 'Preferred Foot': 'Right', 'International Reputation': '3', 'Weak Foot': '3', 'Skill Moves': '1', 'Work Rate': 'Medium/ Medium', 'Body Type': 'Normal', 'Real Face': 'Yes', 'Position': 'GK', 'Jersey Number': '1', 'Joined': 'Jul 16, 2014', 'Loaned From': '', 'Contract Valid Until': '2021', 'Height': "6'2", 'Weight': '192lbs', 'LS': '', 'ST': '', 'RS': '', 'LW': '', 'LF': '', 'CF': '', 'RF': '', 'RW': '', 'LAM': '', 'CAM': '', 'RAM': '', 'LM': '', 'LCM': '', 'CM': '', 'RCM': '', 'RM': '', 'LWB': '', 'LDM': '', 'CDM': '', 'RDM': '', 'RWB': '', 'LB': '', 'LCB': '', 'CB': '', 'RCB': '', 'RB': '', 'Crossing': '13', 'Finishing': '11', 'HeadingAccuracy': '15', 'ShortPassing': '29', 'Volleys': '13', 'Dribbling': '12', 'Curve': '13', 'FKAccuracy': '14', 'LongPassing': '26', 'BallControl': '16', 'Acceleration': '43', 'SprintSpeed': '60', 'Agility': '67', 'Reactions': '86', 'Balance': '49', 'ShotPower': '22', 'Jumping': '76', 'Stamina': '41', 'Strength': '78', 'LongShots': '12', 'Aggression': '34', 'Interceptions': '19', 'Positioning': '11', 'Vision': '70', 'Penalties': '11', 'Composure': '70', 'Marking': '27', 'StandingTackle': '12', 'SlidingTackle': '18', 'GKDiving': '86', 'GKHandling': '92', 'GKKicking': '78', 'GKPositioning': '88', 'GKReflexes': '89', 'Release Clause': 'â‚¬144.5M'}
{'ï»¿': '10', 'ID': '188545', 'Name': 'R. Lewandowski', 'Age': '29', 'Photo': 'https://cdn.sofifa.org/players/4/19/188545.png', 'Nationality': 'Poland', 'Flag': 'https://cdn.sofifa.org/flags/37.png', 'Overall': '90', 'Potential': '90', 'Club': 'FC Bayern MÃ¼nchen', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/21.png', 'Value': 'â‚¬77M', 'Wage': 'â‚¬205K', 'Special': '2152', 'Preferred Foot': 'Right', 'International Reputation': '4', 'Weak Foot': '4', 'Skill Moves': '4', 'Work Rate': 'High/ Medium', 'Body Type': 'Normal', 'Real Face': 'Yes', 'Position': 'ST', 'Jersey Number': '9', 'Joined': 'Jul 1, 2014', 'Loaned From': '', 'Contract Valid Until': '2021', 'Height': "6'0", 'Weight': '176lbs', 'LS': '87+3', 'ST': '87+3', 'RS': '87+3', 'LW': '83+3', 'LF': '86+3', 'CF': '86+3', 'RF': '86+3', 'RW': '83+3', 'LAM': '83+3', 'CAM': '83+3', 'RAM': '83+3', 'LM': '81+3', 'LCM': '77+3', 'CM': '77+3', 'RCM': '77+3', 'RM': '81+3', 'LWB': '61+3', 'LDM': '62+3', 'CDM': '62+3', 'RDM': '62+3', 'RWB': '61+3', 'LB': '58+3', 'LCB': '57+3', 'CB': '57+3', 'RCB': '57+3', 'RB': '58+3', 'Crossing': '62', 'Finishing': '91', 'HeadingAccuracy': '85', 'ShortPassing': '83', 'Volleys': '89', 'Dribbling': '85', 'Curve': '77', 'FKAccuracy': '86', 'LongPassing': '65', 'BallControl': '89', 'Acceleration': '77', 'SprintSpeed': '78', 'Agility': '78', 'Reactions': '90', 'Balance': '78', 'ShotPower': '88', 'Jumping': '84', 'Stamina': '78', 'Strength': '84', 'LongShots': '84', 'Aggression': '80', 'Interceptions': '39', 'Positioning': '91', 'Vision': '77', 'Penalties': '88', 'Composure': '86', 'Marking': '34', 'StandingTackle': '42', 'SlidingTackle': '19', 'GKDiving': '15', 'GKHandling': '6', 'GKKicking': '12', 'GKPositioning': '8', 'GKReflexes': '10', 'Release Clause': 'â‚¬127.1M'}
{'ï»¿': '11', 'ID': '182521', 'Name': 'T. Kroos', 'Age': '28', 'Photo': 'https://cdn.sofifa.org/players/4/19/182521.png', 'Nationality': 'Germany', 'Flag': 'https://cdn.sofifa.org/flags/21.png', 'Overall': '90', 'Potential': '90', 'Club': 'Real Madrid', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/243.png', 'Value': 'â‚¬76.5M', 'Wage': 'â‚¬355K', 'Special': '2190', 'Preferred Foot': 'Right', 'International Reputation': '4', 'Weak Foot': '5', 'Skill Moves': '3', 'Work Rate': 'Medium/ Medium', 'Body Type': 'Normal', 'Real Face': 'Yes', 'Position': 'LCM', 'Jersey Number': '8', 'Joined': 'Jul 17, 2014', 'Loaned From': '', 'Contract Valid Until': '2022', 'Height': "6'0", 'Weight': '168lbs', 'LS': '78+3', 'ST': '78+3', 'RS': '78+3', 'LW': '81+3', 'LF': '82+3', 'CF': '82+3', 'RF': '82+3', 'RW': '81+3', 'LAM': '84+3', 'CAM': '84+3', 'RAM': '84+3', 'LM': '82+3', 'LCM': '86+3', 'CM': '86+3', 'RCM': '86+3', 'RM': '82+3', 'LWB': '79+3', 'LDM': '82+3', 'CDM': '82+3', 'RDM': '82+3', 'RWB': '79+3', 'LB': '77+3', 'LCB': '72+3', 'CB': '72+3', 'RCB': '72+3', 'RB': '77+3', 'Crossing': '88', 'Finishing': '76', 'HeadingAccuracy': '54', 'ShortPassing': '92', 'Volleys': '82', 'Dribbling': '81', 'Curve': '86', 'FKAccuracy': '84', 'LongPassing': '93', 'BallControl': '90', 'Acceleration': '64', 'SprintSpeed': '62', 'Agility': '70', 'Reactions': '89', 'Balance': '71', 'ShotPower': '87', 'Jumping': '30', 'Stamina': '75', 'Strength': '73', 'LongShots': '92', 'Aggression': '60', 'Interceptions': '82', 'Positioning': '79', 'Vision': '86', 'Penalties': '73', 'Composure': '85', 'Marking': '72', 'StandingTackle': '79', 'SlidingTackle': '69', 'GKDiving': '10', 'GKHandling': '11', 'GKKicking': '13', 'GKPositioning': '7', 'GKReflexes': '10', 'Release Clause': 'â‚¬156.8M'}
{'ï»¿': '12', 'ID': '182493', 'Name': 'D. GodÃ\xadn', 'Age': '32', 'Photo': 'https://cdn.sofifa.org/players/4/19/182493.png', 'Nationality': 'Uruguay', 'Flag': 'https://cdn.sofifa.org/flags/60.png', 'Overall': '90', 'Potential': '90', 'Club': 'AtlÃ©tico Madrid', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/240.png', 'Value': 'â‚¬44M', 'Wage': 'â‚¬125K', 'Special': '1946', 'Preferred Foot': 'Right', 'International Reputation': '3', 'Weak Foot': '3', 'Skill Moves': '2', 'Work Rate': 'Medium/ High', 'Body Type': 'Lean', 'Real Face': 'Yes', 'Position': 'CB', 'Jersey Number': '10', 'Joined': 'Aug 4, 2010', 'Loaned From': '', 'Contract Valid Until': '2019', 'Height': "6'2", 'Weight': '172lbs', 'LS': '64+3', 'ST': '64+3', 'RS': '64+3', 'LW': '61+3', 'LF': '62+3', 'CF': '62+3', 'RF': '62+3', 'RW': '61+3', 'LAM': '62+3', 'CAM': '62+3', 'RAM': '62+3', 'LM': '63+3', 'LCM': '68+3', 'CM': '68+3', 'RCM': '68+3', 'RM': '63+3', 'LWB': '76+3', 'LDM': '81+3', 'CDM': '81+3', 'RDM': '81+3', 'RWB': '76+3', 'LB': '79+3', 'LCB': '87+3', 'CB': '87+3', 'RCB': '87+3', 'RB': '79+3', 'Crossing': '55', 'Finishing': '42', 'HeadingAccuracy': '92', 'ShortPassing': '79', 'Volleys': '47', 'Dribbling': '53', 'Curve': '49', 'FKAccuracy': '51', 'LongPassing': '70', 'BallControl': '76', 'Acceleration': '68', 'SprintSpeed': '68', 'Agility': '58', 'Reactions': '85', 'Balance': '54', 'ShotPower': '67', 'Jumping': '91', 'Stamina': '66', 'Strength': '88', 'LongShots': '43', 'Aggression': '89', 'Interceptions': '88', 'Positioning': '48', 'Vision': '52', 'Penalties': '50', 'Composure': '82', 'Marking': '90', 'StandingTackle': '89', 'SlidingTackle': '89', 'GKDiving': '6', 'GKHandling': '8', 'GKKicking': '15', 'GKPositioning': '5', 'GKReflexes': '15', 'Release Clause': 'â‚¬90.2M'}
{'ï»¿': '13', 'ID': '168542', 'Name': 'David Silva', 'Age': '32', 'Photo': 'https://cdn.sofifa.org/players/4/19/168542.png', 'Nationality': 'Spain', 'Flag': 'https://cdn.sofifa.org/flags/45.png', 'Overall': '90', 'Potential': '90', 'Club': 'Manchester City', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/10.png', 'Value': 'â‚¬60M', 'Wage': 'â‚¬285K', 'Special': '2115', 'Preferred Foot': 'Left', 'International Reputation': '4', 'Weak Foot': '2', 'Skill Moves': '4', 'Work Rate': 'High/ Medium', 'Body Type': 'Normal', 'Real Face': 'Yes', 'Position': 'LCM', 'Jersey Number': '21', 'Joined': 'Jul 14, 2010', 'Loaned From': '', 'Contract Valid Until': '2020', 'Height': "5'8", 'Weight': '148lbs', 'LS': '77+3', 'ST': '77+3', 'RS': '77+3', 'LW': '85+3', 'LF': '84+3', 'CF': '84+3', 'RF': '84+3', 'RW': '85+3', 'LAM': '87+3', 'CAM': '87+3', 'RAM': '87+3', 'LM': '85+3', 'LCM': '85+3', 'CM': '85+3', 'RCM': '85+3', 'RM': '85+3', 'LWB': '69+3', 'LDM': '70+3', 'CDM': '70+3', 'RDM': '70+3', 'RWB': '69+3', 'LB': '64+3', 'LCB': '57+3', 'CB': '57+3', 'RCB': '57+3', 'RB': '64+3', 'Crossing': '84', 'Finishing': '76', 'HeadingAccuracy': '54', 'ShortPassing': '93', 'Volleys': '82', 'Dribbling': '89', 'Curve': '82', 'FKAccuracy': '77', 'LongPassing': '87', 'BallControl': '94', 'Acceleration': '70', 'SprintSpeed': '64', 'Agility': '92', 'Reactions': '90', 'Balance': '90', 'ShotPower': '72', 'Jumping': '64', 'Stamina': '78', 'Strength': '52', 'LongShots': '75', 'Aggression': '57', 'Interceptions': '50', 'Positioning': '89', 'Vision': '92', 'Penalties': '75', 'Composure': '93', 'Marking': '59', 'StandingTackle': '53', 'SlidingTackle': '29', 'GKDiving': '6', 'GKHandling': '15', 'GKKicking': '7', 'GKPositioning': '6', 'GKReflexes': '12', 'Release Clause': 'â‚¬111M'}
{'ï»¿': '14', 'ID': '215914', 'Name': 'N. KantÃ©', 'Age': '27', 'Photo': 'https://cdn.sofifa.org/players/4/19/215914.png', 'Nationality': 'France', 'Flag': 'https://cdn.sofifa.org/flags/18.png', 'Overall': '89', 'Potential': '90', 'Club': 'Chelsea', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/5.png', 'Value': 'â‚¬63M', 'Wage': 'â‚¬225K', 'Special': '2189', 'Preferred Foot': 'Right', 'International Reputation': '3', 'Weak Foot': '3', 'Skill Moves': '2', 'Work Rate': 'Medium/ High', 'Body Type': 'Lean', 'Real Face': 'Yes', 'Position': 'LDM', 'Jersey Number': '13', 'Joined': 'Jul 16, 2016', 'Loaned From': '', 'Contract Valid Until': '2023', 'Height': "5'6", 'Weight': '159lbs', 'LS': '72+3', 'ST': '72+3', 'RS': '72+3', 'LW': '77+3', 'LF': '77+3', 'CF': '77+3', 'RF': '77+3', 'RW': '77+3', 'LAM': '79+3', 'CAM': '79+3', 'RAM': '79+3', 'LM': '79+3', 'LCM': '82+3', 'CM': '82+3', 'RCM': '82+3', 'RM': '79+3', 'LWB': '85+3', 'LDM': '87+3', 'CDM': '87+3', 'RDM': '87+3', 'RWB': '85+3', 'LB': '84+3', 'LCB': '83+3', 'CB': '83+3', 'RCB': '83+3', 'RB': '84+3', 'Crossing': '68', 'Finishing': '65', 'HeadingAccuracy': '54', 'ShortPassing': '86', 'Volleys': '56', 'Dribbling': '79', 'Curve': '49', 'FKAccuracy': '49', 'LongPassing': '81', 'BallControl': '80', 'Acceleration': '82', 'SprintSpeed': '78', 'Agility': '82', 'Reactions': '93', 'Balance': '92', 'ShotPower': '71', 'Jumping': '77', 'Stamina': '96', 'Strength': '76', 'LongShots': '69', 'Aggression': '90', 'Interceptions': '92', 'Positioning': '71', 'Vision': '79', 'Penalties': '54', 'Composure': '85', 'Marking': '90', 'StandingTackle': '91', 'SlidingTackle': '85', 'GKDiving': '15', 'GKHandling': '12', 'GKKicking': '10', 'GKPositioning': '7', 'GKReflexes': '10', 'Release Clause': 'â‚¬121.3M'}
{'ï»¿': '15', 'ID': '211110', 'Name': 'P. Dybala', 'Age': '24', 'Photo': 'https://cdn.sofifa.org/players/4/19/211110.png', 'Nationality': 'Argentina', 'Flag': 'https://cdn.sofifa.org/flags/52.png', 'Overall': '89', 'Potential': '94', 'Club': 'Juventus', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/45.png', 'Value': 'â‚¬89M', 'Wage': 'â‚¬205K', 'Special': '2092', 'Preferred Foot': 'Left', 'International Reputation': '3', 'Weak Foot': '3', 'Skill Moves': '4', 'Work Rate': 'High/ Medium', 'Body Type': 'Normal', 'Real Face': 'Yes', 'Position': 'LF', 'Jersey Number': '21', 'Joined': 'Jul 1, 2015', 'Loaned From': '', 'Contract Valid Until': '2022', 'Height': "5'10", 'Weight': '165lbs', 'LS': '83+3', 'ST': '83+3', 'RS': '83+3', 'LW': '87+3', 'LF': '86+3', 'CF': '86+3', 'RF': '86+3', 'RW': '87+3', 'LAM': '87+3', 'CAM': '87+3', 'RAM': '87+3', 'LM': '86+3', 'LCM': '79+3', 'CM': '79+3', 'RCM': '79+3', 'RM': '86+3', 'LWB': '62+3', 'LDM': '58+3', 'CDM': '58+3', 'RDM': '58+3', 'RWB': '62+3', 'LB': '56+3', 'LCB': '45+3', 'CB': '45+3', 'RCB': '45+3', 'RB': '56+3', 'Crossing': '82', 'Finishing': '84', 'HeadingAccuracy': '68', 'ShortPassing': '87', 'Volleys': '88', 'Dribbling': '92', 'Curve': '88', 'FKAccuracy': '88', 'LongPassing': '75', 'BallControl': '92', 'Acceleration': '87', 'SprintSpeed': '83', 'Agility': '91', 'Reactions': '86', 'Balance': '85', 'ShotPower': '82', 'Jumping': '75', 'Stamina': '80', 'Strength': '65', 'LongShots': '88', 'Aggression': '48', 'Interceptions': '32', 'Positioning': '84', 'Vision': '87', 'Penalties': '86', 'Composure': '84', 'Marking': '23', 'StandingTackle': '20', 'SlidingTackle': '20', 'GKDiving': '5', 'GKHandling': '4', 'GKKicking': '4', 'GKPositioning': '5', 'GKReflexes': '8', 'Release Clause': 'â‚¬153.5M'}
{'ï»¿': '16', 'ID': '202126', 'Name': 'H. Kane', 'Age': '24', 'Photo': 'https://cdn.sofifa.org/players/4/19/202126.png', 'Nationality': 'England', 'Flag': 'https://cdn.sofifa.org/flags/14.png', 'Overall': '89', 'Potential': '91', 'Club': 'Tottenham Hotspur', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/18.png', 'Value': 'â‚¬83.5M', 'Wage': 'â‚¬205K', 'Special': '2165', 'Preferred Foot': 'Right', 'International Reputation': '3', 'Weak Foot': '4', 'Skill Moves': '3', 'Work Rate': 'High/ High', 'Body Type': 'Normal', 'Real Face': 'Yes', 'Position': 'ST', 'Jersey Number': '9', 'Joined': 'Jul 1, 2010', 'Loaned From': '', 'Contract Valid Until': '2024', 'Height': "6'2", 'Weight': '196lbs', 'LS': '86+3', 'ST': '86+3', 'RS': '86+3', 'LW': '82+3', 'LF': '84+3', 'CF': '84+3', 'RF': '84+3', 'RW': '82+3', 'LAM': '82+3', 'CAM': '82+3', 'RAM': '82+3', 'LM': '81+3', 'LCM': '79+3', 'CM': '79+3', 'RCM': '79+3', 'RM': '81+3', 'LWB': '65+3', 'LDM': '66+3', 'CDM': '66+3', 'RDM': '66+3', 'RWB': '65+3', 'LB': '62+3', 'LCB': '60+3', 'CB': '60+3', 'RCB': '60+3', 'RB': '62+3', 'Crossing': '75', 'Finishing': '94', 'HeadingAccuracy': '85', 'ShortPassing': '80', 'Volleys': '84', 'Dribbling': '80', 'Curve': '78', 'FKAccuracy': '68', 'LongPassing': '82', 'BallControl': '84', 'Acceleration': '68', 'SprintSpeed': '72', 'Agility': '71', 'Reactions': '91', 'Balance': '71', 'ShotPower': '88', 'Jumping': '78', 'Stamina': '89', 'Strength': '84', 'LongShots': '85', 'Aggression': '76', 'Interceptions': '35', 'Positioning': '93', 'Vision': '80', 'Penalties': '90', 'Composure': '89', 'Marking': '56', 'StandingTackle': '36', 'SlidingTackle': '38', 'GKDiving': '8', 'GKHandling': '10', 'GKKicking': '11', 'GKPositioning': '14', 'GKReflexes': '11', 'Release Clause': 'â‚¬160.7M'}
{'ï»¿': '17', 'ID': '194765', 'Name': 'A. Griezmann', 'Age': '27', 'Photo': 'https://cdn.sofifa.org/players/4/19/194765.png', 'Nationality': 'France', 'Flag': 'https://cdn.sofifa.org/flags/18.png', 'Overall': '89', 'Potential': '90', 'Club': 'AtlÃ©tico Madrid', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/240.png', 'Value': 'â‚¬78M', 'Wage': 'â‚¬145K', 'Special': '2246', 'Preferred Foot': 'Left', 'International Reputation': '4', 'Weak Foot': '3', 'Skill Moves': '4', 'Work Rate': 'High/ High', 'Body Type': 'Lean', 'Real Face': 'Yes', 'Position': 'CAM', 'Jersey Number': '7', 'Joined': 'Jul 28, 2014', 'Loaned From': '', 'Contract Valid Until': '2023', 'Height': "5'9", 'Weight': '161lbs', 'LS': '86+3', 'ST': '86+3', 'RS': '86+3', 'LW': '87+3', 'LF': '87+3', 'CF': '87+3', 'RF': '87+3', 'RW': '87+3', 'LAM': '86+3', 'CAM': '86+3', 'RAM': '86+3', 'LM': '86+3', 'LCM': '80+3', 'CM': '80+3', 'RCM': '80+3', 'RM': '86+3', 'LWB': '70+3', 'LDM': '67+3', 'CDM': '67+3', 'RDM': '67+3', 'RWB': '70+3', 'LB': '67+3', 'LCB': '61+3', 'CB': '61+3', 'RCB': '61+3', 'RB': '67+3', 'Crossing': '82', 'Finishing': '90', 'HeadingAccuracy': '84', 'ShortPassing': '83', 'Volleys': '87', 'Dribbling': '88', 'Curve': '84', 'FKAccuracy': '78', 'LongPassing': '76', 'BallControl': '90', 'Acceleration': '88', 'SprintSpeed': '85', 'Agility': '90', 'Reactions': '90', 'Balance': '80', 'ShotPower': '80', 'Jumping': '90', 'Stamina': '83', 'Strength': '62', 'LongShots': '82', 'Aggression': '69', 'Interceptions': '35', 'Positioning': '91', 'Vision': '83', 'Penalties': '79', 'Composure': '87', 'Marking': '59', 'StandingTackle': '47', 'SlidingTackle': '48', 'GKDiving': '14', 'GKHandling': '8', 'GKKicking': '14', 'GKPositioning': '13', 'GKReflexes': '14', 'Release Clause': 'â‚¬165.8M'}
{'ï»¿': '18', 'ID': '192448', 'Name': 'M. ter Stegen', 'Age': '26', 'Photo': 'https://cdn.sofifa.org/players/4/19/192448.png', 'Nationality': 'Germany', 'Flag': 'https://cdn.sofifa.org/flags/21.png', 'Overall': '89', 'Potential': '92', 'Club': 'FC Barcelona', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/241.png', 'Value': 'â‚¬58M', 'Wage': 'â‚¬240K', 'Special': '1328', 'Preferred Foot': 'Right', 'International Reputation': '3', 'Weak Foot': '4', 'Skill Moves': '1', 'Work Rate': 'Medium/ Medium', 'Body Type': 'Normal', 'Real Face': 'Yes', 'Position': 'GK', 'Jersey Number': '22', 'Joined': 'Jul 1, 2014', 'Loaned From': '', 'Contract Valid Until': '2022', 'Height': "6'2", 'Weight': '187lbs', 'LS': '', 'ST': '', 'RS': '', 'LW': '', 'LF': '', 'CF': '', 'RF': '', 'RW': '', 'LAM': '', 'CAM': '', 'RAM': '', 'LM': '', 'LCM': '', 'CM': '', 'RCM': '', 'RM': '', 'LWB': '', 'LDM': '', 'CDM': '', 'RDM': '', 'RWB': '', 'LB': '', 'LCB': '', 'CB': '', 'RCB': '', 'RB': '', 'Crossing': '15', 'Finishing': '14', 'HeadingAccuracy': '11', 'ShortPassing': '36', 'Volleys': '14', 'Dribbling': '17', 'Curve': '18', 'FKAccuracy': '12', 'LongPassing': '42', 'BallControl': '18', 'Acceleration': '38', 'SprintSpeed': '50', 'Agility': '37', 'Reactions': '85', 'Balance': '43', 'ShotPower': '22', 'Jumping': '79', 'Stamina': '35', 'Strength': '79', 'LongShots': '10', 'Aggression': '43', 'Interceptions': '22', 'Positioning': '11', 'Vision': '69', 'Penalties': '25', 'Composure': '69', 'Marking': '25', 'StandingTackle': '13', 'SlidingTackle': '10', 'GKDiving': '87', 'GKHandling': '85', 'GKKicking': '88', 'GKPositioning': '85', 'GKReflexes': '90', 'Release Clause': 'â‚¬123.3M'}
{'ï»¿': '19', 'ID': '192119', 'Name': 'T. Courtois', 'Age': '26', 'Photo': 'https://cdn.sofifa.org/players/4/19/192119.png', 'Nationality': 'Belgium', 'Flag': 'https://cdn.sofifa.org/flags/7.png', 'Overall': '89', 'Potential': '90', 'Club': 'Real Madrid', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/243.png', 'Value': 'â‚¬53.5M', 'Wage': 'â‚¬240K', 'Special': '1311', 'Preferred Foot': 'Left', 'International Reputation': '4', 'Weak Foot': '2', 'Skill Moves': '1', 'Work Rate': 'Medium/ Medium', 'Body Type': 'Courtois', 'Real Face': 'Yes', 'Position': 'GK', 'Jersey Number': '1', 'Joined': 'Aug 9, 2018', 'Loaned From': '', 'Contract Valid Until': '2024', 'Height': "6'6", 'Weight': '212lbs', 'LS': '', 'ST': '', 'RS': '', 'LW': '', 'LF': '', 'CF': '', 'RF': '', 'RW': '', 'LAM': '', 'CAM': '', 'RAM': '', 'LM': '', 'LCM': '', 'CM': '', 'RCM': '', 'RM': '', 'LWB': '', 'LDM': '', 'CDM': '', 'RDM': '', 'RWB': '', 'LB': '', 'LCB': '', 'CB': '', 'RCB': '', 'RB': '', 'Crossing': '14', 'Finishing': '14', 'HeadingAccuracy': '13', 'ShortPassing': '33', 'Volleys': '12', 'Dribbling': '13', 'Curve': '19', 'FKAccuracy': '20', 'LongPassing': '35', 'BallControl': '23', 'Acceleration': '46', 'SprintSpeed': '52', 'Agility': '61', 'Reactions': '84', 'Balance': '45', 'ShotPower': '36', 'Jumping': '68', 'Stamina': '38', 'Strength': '70', 'LongShots': '17', 'Aggression': '23', 'Interceptions': '15', 'Positioning': '13', 'Vision': '44', 'Penalties': '27', 'Composure': '66', 'Marking': '20', 'StandingTackle': '18', 'SlidingTackle': '16', 'GKDiving': '85', 'GKHandling': '91', 'GKKicking': '72', 'GKPositioning': '86', 'GKReflexes': '88', 'Release Clause': 'â‚¬113.7M'}
{'ï»¿': '20', 'ID': '189511', 'Name': 'Sergio Busquets', 'Age': '29', 'Photo': 'https://cdn.sofifa.org/players/4/19/189511.png', 'Nationality': 'Spain', 'Flag': 'https://cdn.sofifa.org/flags/45.png', 'Overall': '89', 'Potential': '89', 'Club': 'FC Barcelona', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/241.png', 'Value': 'â‚¬51.5M', 'Wage': 'â‚¬315K', 'Special': '2065', 'Preferred Foot': 'Right', 'International Reputation': '4', 'Weak Foot': '3', 'Skill Moves': '3', 'Work Rate': 'Medium/ Medium', 'Body Type': 'Lean', 'Real Face': 'Yes', 'Position': 'CDM', 'Jersey Number': '5', 'Joined': 'Sep 1, 2008', 'Loaned From': '', 'Contract Valid Until': '2023', 'Height': "6'2", 'Weight': '168lbs', 'LS': '71+3', 'ST': '71+3', 'RS': '71+3', 'LW': '74+3', 'LF': '76+3', 'CF': '76+3', 'RF': '76+3', 'RW': '74+3', 'LAM': '79+3', 'CAM': '79+3', 'RAM': '79+3', 'LM': '76+3', 'LCM': '83+3', 'CM': '83+3', 'RCM': '83+3', 'RM': '76+3', 'LWB': '79+3', 'LDM': '86+3', 'CDM': '86+3', 'RDM': '86+3', 'RWB': '79+3', 'LB': '78+3', 'LCB': '82+3', 'CB': '82+3', 'RCB': '82+3', 'RB': '78+3', 'Crossing': '62', 'Finishing': '67', 'HeadingAccuracy': '68', 'ShortPassing': '89', 'Volleys': '44', 'Dribbling': '80', 'Curve': '66', 'FKAccuracy': '68', 'LongPassing': '82', 'BallControl': '88', 'Acceleration': '50', 'SprintSpeed': '52', 'Agility': '66', 'Reactions': '87', 'Balance': '52', 'ShotPower': '61', 'Jumping': '66', 'Stamina': '86', 'Strength': '77', 'LongShots': '54', 'Aggression': '85', 'Interceptions': '87', 'Positioning': '77', 'Vision': '87', 'Penalties': '60', 'Composure': '90', 'Marking': '90', 'StandingTackle': '86', 'SlidingTackle': '80', 'GKDiving': '5', 'GKHandling': '8', 'GKKicking': '13', 'GKPositioning': '9', 'GKReflexes': '13', 'Release Clause': 'â‚¬105.6M'}
{'ï»¿': '21', 'ID': '179813', 'Name': 'E. Cavani', 'Age': '31', 'Photo': 'https://cdn.sofifa.org/players/4/19/179813.png', 'Nationality': 'Uruguay', 'Flag': 'https://cdn.sofifa.org/flags/60.png', 'Overall': '89', 'Potential': '89', 'Club': 'Paris Saint-Germain', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/73.png', 'Value': 'â‚¬60M', 'Wage': 'â‚¬200K', 'Special': '2161', 'Preferred Foot': 'Right', 'International Reputation': '4', 'Weak Foot': '4', 'Skill Moves': '3', 'Work Rate': 'High/ High', 'Body Type': 'Lean', 'Real Face': 'Yes', 'Position': 'LS', 'Jersey Number': '21', 'Joined': 'Jul 16, 2013', 'Loaned From': '', 'Contract Valid Until': '2020', 'Height': "6'1", 'Weight': '170lbs', 'LS': '85+3', 'ST': '85+3', 'RS': '85+3', 'LW': '81+3', 'LF': '83+3', 'CF': '83+3', 'RF': '83+3', 'RW': '81+3', 'LAM': '80+3', 'CAM': '80+3', 'RAM': '80+3', 'LM': '79+3', 'LCM': '75+3', 'CM': '75+3', 'RCM': '75+3', 'RM': '79+3', 'LWB': '67+3', 'LDM': '65+3', 'CDM': '65+3', 'RDM': '65+3', 'RWB': '67+3', 'LB': '65+3', 'LCB': '63+3', 'CB': '63+3', 'RCB': '63+3', 'RB': '65+3', 'Crossing': '70', 'Finishing': '89', 'HeadingAccuracy': '89', 'ShortPassing': '78', 'Volleys': '90', 'Dribbling': '80', 'Curve': '77', 'FKAccuracy': '76', 'LongPassing': '52', 'BallControl': '82', 'Acceleration': '75', 'SprintSpeed': '76', 'Agility': '77', 'Reactions': '91', 'Balance': '59', 'ShotPower': '87', 'Jumping': '88', 'Stamina': '92', 'Strength': '78', 'LongShots': '79', 'Aggression': '84', 'Interceptions': '48', 'Positioning': '93', 'Vision': '77', 'Penalties': '85', 'Composure': '82', 'Marking': '52', 'StandingTackle': '45', 'SlidingTackle': '39', 'GKDiving': '12', 'GKHandling': '5', 'GKKicking': '13', 'GKPositioning': '13', 'GKReflexes': '10', 'Release Clause': 'â‚¬111M'}
{'ï»¿': '22', 'ID': '167495', 'Name': 'M. Neuer', 'Age': '32', 'Photo': 'https://cdn.sofifa.org/players/4/19/167495.png', 'Nationality': 'Germany', 'Flag': 'https://cdn.sofifa.org/flags/21.png', 'Overall': '89', 'Potential': '89', 'Club': 'FC Bayern MÃ¼nchen', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/21.png', 'Value': 'â‚¬38M', 'Wage': 'â‚¬130K', 'Special': '1473', 'Preferred Foot': 'Right', 'International Reputation': '5', 'Weak Foot': '4', 'Skill Moves': '1', 'Work Rate': 'Medium/ Medium', 'Body Type': 'Normal', 'Real Face': 'Yes', 'Position': 'GK', 'Jersey Number': '1', 'Joined': 'Jul 1, 2011', 'Loaned From': '', 'Contract Valid Until': '2021', 'Height': "6'4", 'Weight': '203lbs', 'LS': '', 'ST': '', 'RS': '', 'LW': '', 'LF': '', 'CF': '', 'RF': '', 'RW': '', 'LAM': '', 'CAM': '', 'RAM': '', 'LM': '', 'LCM': '', 'CM': '', 'RCM': '', 'RM': '', 'LWB': '', 'LDM': '', 'CDM': '', 'RDM': '', 'RWB': '', 'LB': '', 'LCB': '', 'CB': '', 'RCB': '', 'RB': '', 'Crossing': '15', 'Finishing': '13', 'HeadingAccuracy': '25', 'ShortPassing': '55', 'Volleys': '11', 'Dribbling': '30', 'Curve': '14', 'FKAccuracy': '11', 'LongPassing': '59', 'BallControl': '48', 'Acceleration': '54', 'SprintSpeed': '60', 'Agility': '51', 'Reactions': '84', 'Balance': '35', 'ShotPower': '25', 'Jumping': '77', 'Stamina': '43', 'Strength': '80', 'LongShots': '16', 'Aggression': '29', 'Interceptions': '30', 'Positioning': '12', 'Vision': '70', 'Penalties': '47', 'Composure': '70', 'Marking': '17', 'StandingTackle': '10', 'SlidingTackle': '11', 'GKDiving': '90', 'GKHandling': '86', 'GKKicking': '91', 'GKPositioning': '87', 'GKReflexes': '87', 'Release Clause': 'â‚¬62.7M'}
{'ï»¿': '23', 'ID': '153079', 'Name': 'S. AgÃ¼ero', 'Age': '30', 'Photo': 'https://cdn.sofifa.org/players/4/19/153079.png', 'Nationality': 'Argentina', 'Flag': 'https://cdn.sofifa.org/flags/52.png', 'Overall': '89', 'Potential': '89', 'Club': 'Manchester City', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/10.png', 'Value': 'â‚¬64.5M', 'Wage': 'â‚¬300K', 'Special': '2107', 'Preferred Foot': 'Right', 'International Reputation': '4', 'Weak Foot': '4', 'Skill Moves': '4', 'Work Rate': 'High/ Medium', 'Body Type': 'Stocky', 'Real Face': 'Yes', 'Position': 'ST', 'Jersey Number': '10', 'Joined': 'Jul 28, 2011', 'Loaned From': '', 'Contract Valid Until': '2021', 'Height': "5'8", 'Weight': '154lbs', 'LS': '86+3', 'ST': '86+3', 'RS': '86+3', 'LW': '86+3', 'LF': '87+3', 'CF': '87+3', 'RF': '87+3', 'RW': '86+3', 'LAM': '85+3', 'CAM': '85+3', 'RAM': '85+3', 'LM': '83+3', 'LCM': '76+3', 'CM': '76+3', 'RCM': '76+3', 'RM': '83+3', 'LWB': '58+3', 'LDM': '56+3', 'CDM': '56+3', 'RDM': '56+3', 'RWB': '58+3', 'LB': '53+3', 'LCB': '47+3', 'CB': '47+3', 'RCB': '47+3', 'RB': '53+3', 'Crossing': '70', 'Finishing': '93', 'HeadingAccuracy': '77', 'ShortPassing': '81', 'Volleys': '85', 'Dribbling': '89', 'Curve': '82', 'FKAccuracy': '73', 'LongPassing': '64', 'BallControl': '89', 'Acceleration': '88', 'SprintSpeed': '80', 'Agility': '86', 'Reactions': '90', 'Balance': '91', 'ShotPower': '88', 'Jumping': '81', 'Stamina': '76', 'Strength': '73', 'LongShots': '83', 'Aggression': '65', 'Interceptions': '24', 'Positioning': '92', 'Vision': '83', 'Penalties': '83', 'Composure': '90', 'Marking': '30', 'StandingTackle': '20', 'SlidingTackle': '12', 'GKDiving': '13', 'GKHandling': '15', 'GKKicking': '6', 'GKPositioning': '11', 'GKReflexes': '14', 'Release Clause': 'â‚¬119.3M'}
{'ï»¿': '24', 'ID': '138956', 'Name': 'G. Chiellini', 'Age': '33', 'Photo': 'https://cdn.sofifa.org/players/4/19/138956.png', 'Nationality': 'Italy', 'Flag': 'https://cdn.sofifa.org/flags/27.png', 'Overall': '89', 'Potential': '89', 'Club': 'Juventus', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/45.png', 'Value': 'â‚¬27M', 'Wage': 'â‚¬215K', 'Special': '1841', 'Preferred Foot': 'Left', 'International Reputation': '4', 'Weak Foot': '3', 'Skill Moves': '2', 'Work Rate': 'Medium/ High', 'Body Type': 'Normal', 'Real Face': 'Yes', 'Position': 'LCB', 'Jersey Number': '3', 'Joined': 'Jul 1, 2005', 'Loaned From': '', 'Contract Valid Until': '2020', 'Height': "6'2", 'Weight': '187lbs', 'LS': '58+3', 'ST': '58+3', 'RS': '58+3', 'LW': '54+3', 'LF': '55+3', 'CF': '55+3', 'RF': '55+3', 'RW': '54+3', 'LAM': '54+3', 'CAM': '54+3', 'RAM': '54+3', 'LM': '56+3', 'LCM': '60+3', 'CM': '60+3', 'RCM': '60+3', 'RM': '56+3', 'LWB': '74+3', 'LDM': '76+3', 'CDM': '76+3', 'RDM': '76+3', 'RWB': '74+3', 'LB': '77+3', 'LCB': '86+3', 'CB': '86+3', 'RCB': '86+3', 'RB': '77+3', 'Crossing': '58', 'Finishing': '33', 'HeadingAccuracy': '83', 'ShortPassing': '59', 'Volleys': '45', 'Dribbling': '58', 'Curve': '60', 'FKAccuracy': '31', 'LongPassing': '59', 'BallControl': '57', 'Acceleration': '63', 'SprintSpeed': '75', 'Agility': '54', 'Reactions': '82', 'Balance': '55', 'ShotPower': '78', 'Jumping': '89', 'Stamina': '65', 'Strength': '89', 'LongShots': '49', 'Aggression': '92', 'Interceptions': '88', 'Positioning': '28', 'Vision': '50', 'Penalties': '50', 'Composure': '84', 'Marking': '93', 'StandingTackle': '93', 'SlidingTackle': '90', 'GKDiving': '3', 'GKHandling': '3', 'GKKicking': '2', 'GKPositioning': '4', 'GKReflexes': '3', 'Release Clause': 'â‚¬44.6M'}
{'ï»¿': '25', 'ID': '231747', 'Name': 'K. MbappÃ©', 'Age': '19', 'Photo': 'https://cdn.sofifa.org/players/4/19/231747.png', 'Nationality': 'France', 'Flag': 'https://cdn.sofifa.org/flags/18.png', 'Overall': '88', 'Potential': '95', 'Club': 'Paris Saint-Germain', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/73.png', 'Value': 'â‚¬81M', 'Wage': 'â‚¬100K', 'Special': '2118', 'Preferred Foot': 'Right', 'International Reputation': '3', 'Weak Foot': '4', 'Skill Moves': '5', 'Work Rate': 'High/ Medium', 'Body Type': 'Lean', 'Real Face': 'Yes', 'Position': 'RM', 'Jersey Number': '10', 'Joined': 'Jul 1, 2018', 'Loaned From': '', 'Contract Valid Until': '2022', 'Height': "5'10", 'Weight': '161lbs', 'LS': '85+3', 'ST': '85+3', 'RS': '85+3', 'LW': '87+3', 'LF': '87+3', 'CF': '87+3', 'RF': '87+3', 'RW': '87+3', 'LAM': '86+3', 'CAM': '86+3', 'RAM': '86+3', 'LM': '86+3', 'LCM': '78+3', 'CM': '78+3', 'RCM': '78+3', 'RM': '86+3', 'LWB': '66+3', 'LDM': '62+3', 'CDM': '62+3', 'RDM': '62+3', 'RWB': '66+3', 'LB': '62+3', 'LCB': '54+3', 'CB': '54+3', 'RCB': '54+3', 'RB': '62+3', 'Crossing': '77', 'Finishing': '88', 'HeadingAccuracy': '77', 'ShortPassing': '82', 'Volleys': '78', 'Dribbling': '90', 'Curve': '77', 'FKAccuracy': '63', 'LongPassing': '73', 'BallControl': '91', 'Acceleration': '96', 'SprintSpeed': '96', 'Agility': '92', 'Reactions': '87', 'Balance': '83', 'ShotPower': '79', 'Jumping': '75', 'Stamina': '83', 'Strength': '71', 'LongShots': '78', 'Aggression': '62', 'Interceptions': '38', 'Positioning': '88', 'Vision': '82', 'Penalties': '70', 'Composure': '86', 'Marking': '34', 'StandingTackle': '34', 'SlidingTackle': '32', 'GKDiving': '13', 'GKHandling': '5', 'GKKicking': '7', 'GKPositioning': '11', 'GKReflexes': '6', 'Release Clause': 'â‚¬166.1M'}
{'ï»¿': '26', 'ID': '209331', 'Name': 'M. Salah', 'Age': '26', 'Photo': 'https://cdn.sofifa.org/players/4/19/209331.png', 'Nationality': 'Egypt', 'Flag': 'https://cdn.sofifa.org/flags/111.png', 'Overall': '88', 'Potential': '89', 'Club': 'Liverpool', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/9.png', 'Value': 'â‚¬69.5M', 'Wage': 'â‚¬255K', 'Special': '2146', 'Preferred Foot': 'Left', 'International Reputation': '3', 'Weak Foot': '3', 'Skill Moves': '4', 'Work Rate': 'High/ Medium', 'Body Type': 'PLAYER_BODY_TYPE_25', 'Real Face': 'Yes', 'Position': 'RM', 'Jersey Number': '10', 'Joined': 'Jul 1, 2017', 'Loaned From': '', 'Contract Valid Until': '2023', 'Height': "5'9", 'Weight': '157lbs', 'LS': '83+3', 'ST': '83+3', 'RS': '83+3', 'LW': '87+3', 'LF': '86+3', 'CF': '86+3', 'RF': '86+3', 'RW': '87+3', 'LAM': '86+3', 'CAM': '86+3', 'RAM': '86+3', 'LM': '86+3', 'LCM': '80+3', 'CM': '80+3', 'RCM': '80+3', 'RM': '86+3', 'LWB': '70+3', 'LDM': '66+3', 'CDM': '66+3', 'RDM': '66+3', 'RWB': '70+3', 'LB': '66+3', 'LCB': '57+3', 'CB': '57+3', 'RCB': '57+3', 'RB': '66+3', 'Crossing': '78', 'Finishing': '90', 'HeadingAccuracy': '59', 'ShortPassing': '82', 'Volleys': '73', 'Dribbling': '89', 'Curve': '83', 'FKAccuracy': '60', 'LongPassing': '72', 'BallControl': '88', 'Acceleration': '94', 'SprintSpeed': '91', 'Agility': '91', 'Reactions': '91', 'Balance': '88', 'ShotPower': '77', 'Jumping': '68', 'Stamina': '84', 'Strength': '70', 'LongShots': '83', 'Aggression': '63', 'Interceptions': '55', 'Positioning': '90', 'Vision': '82', 'Penalties': '61', 'Composure': '91', 'Marking': '38', 'StandingTackle': '43', 'SlidingTackle': '41', 'GKDiving': '14', 'GKHandling': '14', 'GKKicking': '9', 'GKPositioning': '11', 'GKReflexes': '14', 'Release Clause': 'â‚¬137.3M'}
{'ï»¿': '27', 'ID': '200145', 'Name': 'Casemiro', 'Age': '26', 'Photo': 'https://cdn.sofifa.org/players/4/19/200145.png', 'Nationality': 'Brazil', 'Flag': 'https://cdn.sofifa.org/flags/54.png', 'Overall': '88', 'Potential': '90', 'Club': 'Real Madrid', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/243.png', 'Value': 'â‚¬59.5M', 'Wage': 'â‚¬285K', 'Special': '2170', 'Preferred Foot': 'Right', 'International Reputation': '3', 'Weak Foot': '3', 'Skill Moves': '2', 'Work Rate': 'Medium/ High', 'Body Type': 'Normal', 'Real Face': 'Yes', 'Position': 'CDM', 'Jersey Number': '14', 'Joined': 'Jul 11, 2013', 'Loaned From': '', 'Contract Valid Until': '2021', 'Height': "6'1", 'Weight': '185lbs', 'LS': '72+3', 'ST': '72+3', 'RS': '72+3', 'LW': '69+3', 'LF': '73+3', 'CF': '73+3', 'RF': '73+3', 'RW': '69+3', 'LAM': '74+3', 'CAM': '74+3', 'RAM': '74+3', 'LM': '71+3', 'LCM': '80+3', 'CM': '80+3', 'RCM': '80+3', 'RM': '71+3', 'LWB': '78+3', 'LDM': '85+3', 'CDM': '85+3', 'RDM': '85+3', 'RWB': '78+3', 'LB': '79+3', 'LCB': '85+3', 'CB': '85+3', 'RCB': '85+3', 'RB': '79+3', 'Crossing': '52', 'Finishing': '59', 'HeadingAccuracy': '76', 'ShortPassing': '85', 'Volleys': '53', 'Dribbling': '69', 'Curve': '59', 'FKAccuracy': '74', 'LongPassing': '82', 'BallControl': '78', 'Acceleration': '59', 'SprintSpeed': '65', 'Agility': '62', 'Reactions': '84', 'Balance': '66', 'ShotPower': '86', 'Jumping': '88', 'Stamina': '87', 'Strength': '89', 'LongShots': '79', 'Aggression': '87', 'Interceptions': '87', 'Positioning': '69', 'Vision': '77', 'Penalties': '66', 'Composure': '84', 'Marking': '88', 'StandingTackle': '90', 'SlidingTackle': '87', 'GKDiving': '13', 'GKHandling': '14', 'GKKicking': '16', 'GKPositioning': '12', 'GKReflexes': '12', 'Release Clause': 'â‚¬126.4M'}
{'ï»¿': '28', 'ID': '198710', 'Name': 'J. RodrÃ\xadguez', 'Age': '26', 'Photo': 'https://cdn.sofifa.org/players/4/19/198710.png', 'Nationality': 'Colombia', 'Flag': 'https://cdn.sofifa.org/flags/56.png', 'Overall': '88', 'Potential': '89', 'Club': 'FC Bayern MÃ¼nchen', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/21.png', 'Value': 'â‚¬69.5M', 'Wage': 'â‚¬315K', 'Special': '2171', 'Preferred Foot': 'Left', 'International Reputation': '4', 'Weak Foot': '3', 'Skill Moves': '4', 'Work Rate': 'Medium/ Medium', 'Body Type': 'Normal', 'Real Face': 'Yes', 'Position': 'LAM', 'Jersey Number': '10', 'Joined': '', 'Loaned From': 'Real Madrid', 'Contract Valid Until': 'Jun 30, 2019', 'Height': "5'11", 'Weight': '172lbs', 'LS': '80+3', 'ST': '80+3', 'RS': '80+3', 'LW': '84+3', 'LF': '83+3', 'CF': '83+3', 'RF': '83+3', 'RW': '84+3', 'LAM': '85+3', 'CAM': '85+3', 'RAM': '85+3', 'LM': '83+3', 'LCM': '81+3', 'CM': '81+3', 'RCM': '81+3', 'RM': '83+3', 'LWB': '69+3', 'LDM': '68+3', 'CDM': '68+3', 'RDM': '68+3', 'RWB': '69+3', 'LB': '65+3', 'LCB': '58+3', 'CB': '58+3', 'RCB': '58+3', 'RB': '65+3', 'Crossing': '90', 'Finishing': '83', 'HeadingAccuracy': '62', 'ShortPassing': '89', 'Volleys': '90', 'Dribbling': '85', 'Curve': '89', 'FKAccuracy': '86', 'LongPassing': '83', 'BallControl': '90', 'Acceleration': '73', 'SprintSpeed': '67', 'Agility': '83', 'Reactions': '85', 'Balance': '76', 'ShotPower': '86', 'Jumping': '54', 'Stamina': '70', 'Strength': '68', 'LongShots': '92', 'Aggression': '64', 'Interceptions': '55', 'Positioning': '80', 'Vision': '89', 'Penalties': '81', 'Composure': '87', 'Marking': '52', 'StandingTackle': '41', 'SlidingTackle': '44', 'GKDiving': '15', 'GKHandling': '15', 'GKKicking': '15', 'GKPositioning': '5', 'GKReflexes': '14', 'Release Clause': ''}
{'ï»¿': '29', 'ID': '198219', 'Name': 'L. Insigne', 'Age': '27', 'Photo': 'https://cdn.sofifa.org/players/4/19/198219.png', 'Nationality': 'Italy', 'Flag': 'https://cdn.sofifa.org/flags/27.png', 'Overall': '88', 'Potential': '88', 'Club': 'Napoli', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/48.png', 'Value': 'â‚¬62M', 'Wage': 'â‚¬165K', 'Special': '2017', 'Preferred Foot': 'Right', 'International Reputation': '3', 'Weak Foot': '3', 'Skill Moves': '4', 'Work Rate': 'High/ Medium', 'Body Type': 'Normal', 'Real Face': 'Yes', 'Position': 'LW', 'Jersey Number': '10', 'Joined': 'Jul 1, 2010', 'Loaned From': '', 'Contract Valid Until': '2022', 'Height': "5'4", 'Weight': '130lbs', 'LS': '78+3', 'ST': '78+3', 'RS': '78+3', 'LW': '86+3', 'LF': '85+3', 'CF': '85+3', 'RF': '85+3', 'RW': '86+3', 'LAM': '86+3', 'CAM': '86+3', 'RAM': '86+3', 'LM': '86+3', 'LCM': '78+3', 'CM': '78+3', 'RCM': '78+3', 'RM': '86+3', 'LWB': '63+3', 'LDM': '58+3', 'CDM': '58+3', 'RDM': '58+3', 'RWB': '63+3', 'LB': '58+3', 'LCB': '44+3', 'CB': '44+3', 'RCB': '44+3', 'RB': '58+3', 'Crossing': '86', 'Finishing': '77', 'HeadingAccuracy': '56', 'ShortPassing': '85', 'Volleys': '74', 'Dribbling': '90', 'Curve': '87', 'FKAccuracy': '77', 'LongPassing': '78', 'BallControl': '93', 'Acceleration': '94', 'SprintSpeed': '86', 'Agility': '94', 'Reactions': '83', 'Balance': '93', 'ShotPower': '75', 'Jumping': '53', 'Stamina': '75', 'Strength': '44', 'LongShots': '84', 'Aggression': '34', 'Interceptions': '26', 'Positioning': '83', 'Vision': '87', 'Penalties': '61', 'Composure': '83', 'Marking': '51', 'StandingTackle': '24', 'SlidingTackle': '22', 'GKDiving': '8', 'GKHandling': '4', 'GKKicking': '14', 'GKPositioning': '9', 'GKReflexes': '10', 'Release Clause': 'â‚¬105.4M'}
{'ï»¿': '30', 'ID': '197781', 'Name': 'Isco', 'Age': '26', 'Photo': 'https://cdn.sofifa.org/players/4/19/197781.png', 'Nationality': 'Spain', 'Flag': 'https://cdn.sofifa.org/flags/45.png', 'Overall': '88', 'Potential': '91', 'Club': 'Real Madrid', 'Club Logo': 'https://cdn.sofifa.org/teams/2/light/243.png', 'Value': 'â‚¬73.5M', 'Wage': 'â‚¬315K', 'Special': '2137', 'Preferred Foot': 'Right', 'International Reputation': '3', 'Weak Foot': '3', 'Skill Moves': '4', 'Work Rate': 'High/ Medium', 'Body Type': 'Normal', 'Real Face': 'Yes', 'Position': 'LW', 'Jersey Number': '22', 'Joined': 'Jul 3, 2013', 'Loaned From': '', 'Contract Valid Until': '2022', 'Height': "5'9", 'Weight': '174lbs', 'LS': '76+3', 'ST': '76+3', 'RS': '76+3', 'LW': '84+3', 'LF': '83+3', 'CF': '83+3', 'RF': '83+3', 'RW': '84+3', 'LAM': '86+3', 'CAM': '86+3', 'RAM': '86+3', 'LM': '83+3', 'LCM': '83+3', 'CM': '83+3', 'RCM': '83+3', 'RM': '83+3', 'LWB': '72+3', 'LDM': '73+3', 'CDM': '73+3', 'RDM': '73+3', 'RWB': '72+3', 'LB': '68+3', 'LCB': '63+3', 'CB': '63+3', 'RCB': '63+3', 'RB': '68+3', 'Crossing': '75', 'Finishing': '79', 'HeadingAccuracy': '55', 'ShortPassing': '89', 'Volleys': '65', 'Dribbling': '94', 'Curve': '88', 'FKAccuracy': '76', 'LongPassing': '83', 'BallControl': '95', 'Acceleration': '75', 'SprintSpeed': '69', 'Agility': '87', 'Reactions': '77', 'Balance': '90', 'ShotPower': '69', 'Jumping': '64', 'Stamina': '70', 'Strength': '59', 'LongShots': '87', 'Aggression': '58', 'Interceptions': '64', 'Positioning': '78', 'Vision': '89', 'Penalties': '76', 'Composure': '86', 'Marking': '60', 'StandingTackle': '64', 'SlidingTackle': '51', 'GKDiving': '10', 'GKHandling': '8', 'GKKicking': '12', 'GKPositioning': '15', 'GKReflexes': '6', 'Release Clause': 'â‚¬156.2M'}


# In[ ]:





# In[55]:


dicte


# In[26]:


col= data.columns


# In[53]:


d = data.values
dict(data = d)


# In[21]:


len(data.values)


# In[ ]:





# In[15]:


listed = ['Unnamed: 0', 'ID', 'Name', 'Age', 'Photo', 'Nationality', 'Flag',
       'Overall', 'Potential', 'Club', 'Club Logo', 'Value', 'Wage', 'Special',
       'Preferred Foot', 'International Reputation', 'Weak Foot',
       'Skill Moves', 'Work Rate', 'Body Type', 'Real Face', 'Position',
       'Jersey Number', 'Joined', 'Loaned From', 'Contract Valid Until',
       'Height', 'Weight', 'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
       'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
       'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB', 'Crossing',
       'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
       'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
       'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
       'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
       'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
       'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
       'GKKicking', 'GKPositioning', 'GKReflexes', 'Release Clause']


# In[39]:


df = pd.Series(listed)
df


# In[47]:


f  = {'student1': {'name': 'Ade', 'grade': 'best', 'age': '45'}, 
    'student2': {'name': 'Lola', 'grade': 'bad', 'age': '25'}, 'student3': {'name': 'Isaac', 'grade': 'good', 'age': '35'}, 'student4': {'name': 'luke', 'grade': 'avearage', 'age': '25'}, 
                'student5': {'name': 'kola', 'grade': 'best', 'age': '30'}}
f


# In[48]:


pd.DataFrame(f)


# In[60]:


get_ipython().system('pip install textblob')


# In[64]:


get_ipython().system('pip install pyspellchecker')


# In[61]:


from textblob import Word


# In[1]:


from spellchecker import SpellChecker


# In[67]:


spell = SpellChecker()
# find those words that may be misspelled
misspelled = spell.unknown(['let', 'us', 'wlak','on','the','groun'])

for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))


# In[57]:


data.columns


# In[74]:


some = data[['ID','Name','Age','Preferred Foot','Club','Nationality']]
some


# In[96]:


some['Players Hipe'] = some['Age'].astype(str) + ' '+ some['Club']
some


# In[ ]:




