#!/usr/bin/env python
# coding: utf-8

# # Abrar Ali
# # Reg no:210201068

# In[ ]:


#question no 1


# In[ ]:


product_num = eval(input("Enter Number of products: "))
my_dict ={}
for x in range(product_num):
    productName = input("Enter Product Name: ")
    productPrice = int(input("Enter Product Price"))
    my_dict[productName] = productPrice


while True:
    productName = input("Enter Product name to get Price")
    if productName in my_dict:
        print("The price for your product is ", my_dict[productName])

    else:
        print("This product is not found in dictionary")


print(my_dict)


# In[ ]:


#Question no 2


# In[ ]:


my_dict ={'Mercedez': '100','Ferrari':'200','Bugatti':'300'}
print(my_dict)

amt =eval(input("Enter Amount: $$"))
for key ,values in my_dict.items():
    if  int(values) < amt:
        print (key ,"->",values)


# In[ ]:


#Question No 3


# In[ ]:


import operator

year ={"January":"31","Febuary":"28","March":"30","April":"30","May":"31","June":"30"}

user_input= input("Enter Name of a month: ")
for key, values in year.items():
     if user_input == key: 
        print( values)
        


sorted_year ={key:year[key] for key in sorted(year)}
print(sorted_year.keys())

for keys,values in year.items():
    if int(values) == 31:

      print(keys)

sorted_bymonthdays = dict(sorted(year.items(),key= operator.itemgetter(1)))
print(sorted_bymonthdays)


# In[ ]:


#Question No 4


# In[ ]:


user_dict ={"Henry":"1234","Thomas":"Larissa","Monique":"Gaga"}
def CheckUser_Pass(x,y):
    for keys ,values in user_dict.items():
        if keys == x  and y == user_dict[keys]:
            return ("you are succesfully logged in",keys,user_dict[keys])
        else:
            return  ("Please do check your login details")



x = input("Enter Username: ")    
y = input("Enter Your Password ")
print(CheckUser_Pass(x,y))


# In[ ]:


#Question No 5


# In[ ]:


def teamWIn():
    numberofTeams = int(input("Enter Number of Teams: "))
    team_dict={}
    score_list =[]
    winning_record =[]
    percentage_score = 0
    for team in range(numberofTeams):
        team_name = input("Enter Team Name: ")
        team_winning_score = int(input("Team Winning game: "))
        team_dict.update({team_name:team_winning_score})
        score_list.append(team_winning_score)
        winning_record.append(team_name)

    userinput = input("Enter team to check % of wins: ")
    for  keys,values in team_dict.items():

         if userinput == keys:
            score = team_dict[keys]
            percentage_score = (score/100)* 100

    return "Your teams list is {},Percentage win of team {}%, All team with winning record  {}".format(team_dict,percentage_score,winning_record)






print(teamWIn())


# In[ ]:


#Question No 6


# In[ ]:


def teamInfo():
   num_team =int(input("Enter Number Of Teams: "))
   team_dict={}
   for team in range(num_team):
       key = input("Enter Team name: ")
       value =[]
       wins = int(input("Enter Win: "))
       losses = int(input("Enter Losses: "))
       value.extend((wins,losses))
       team_dict.update({key:value})
       
   return team_dict

print(teamInfo())


# In[ ]:


#Question No 7


# In[ ]:


def creatList():
    matrix_dict={}
    for num in range(len(matrix_5)):
        key = matrix_5[num]
        value = matrix_5.count(key)
        matrix_dict.update({key:value})
    return matrix_dict



print(creatList())


# In[ ]:


#Qusetion No 8


# In[ ]:


import random

all_card ={"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10}
cards = 3
player1Card =[]
player2Card =[]
for card in range(cards):
    c1 =random.choice(list(all_card.values()))
    c2= random.choice(list(all_card.values()))
    player1Card.append(c1)
    player2Card.append(c2)
print(player1Card,player2Card)

if sum(player1Card) > sum(player2Card):
    print("Player 1 wins with ",sum(player1Card)," Against Player 2 with",sum(player2Card))
elif sum(player2Card) > sum(player1Card):
    print("Player 2 wins with ",sum(player2Card)," Against Player 1 with",sum(player1Card))


# In[ ]:


#Question No 9


# In[ ]:


from enum import Enum
from random import sample

class Cards(Enum):
    DECK = [{'value':i, 'suit':c} 
            for c in ['spades', 'clubs', 'hearts', 'diamonds'] 
            for i in range(2,15)]

def get_cards():
    rand_cards = sample(Cards.DECK.value, 3)
    return rand_cards

def flush(hand):
    if hand[0]['suit'] == hand[1]['suit'] == hand[2]['suit']:
        print('\nYou have a flush.')
    else:
        print('\nYou don\'t have a flush.')

def three_of_a_kind(hand):
    if hand[0]['value'] == hand[1]['value'] == hand[2]['value']:
        print('\nYou have a three-of-a-kind.')
    else:
        print('\nYou don\'t have a three-of-a-kind.')

def pair(hand):
    try:
        for i in range(3):
            if hand[i]['value'] == hand[i+1]['value']:
                print('\nYou have a pair.')
                break
            else:
                pass
    except IndexError:
        print('\nYou don\'t have a pair.')

def straight(hand):
    face_val = []
    for i in range(3):
        face_val.append(hand[i]['value'])
    face_val.sort(reverse = True)
    try:
        for i in range(3):
            if (face_val[i] - face_val[i+1] == 1) and (face_val[i+1] - face_val[i+2] == 1):
                print('\nYou have a straight.')
                break
            else:
                pass
    except IndexError:
        print('\nYou don\'t have a straight.')

def main():
    hand = get_cards()
    print('The following below is your hand.\n')
    print(hand)
    flush(hand)
    three_of_a_kind(hand)
    pair(hand)
    straight(hand)
    
if __name__ == '__main__':

