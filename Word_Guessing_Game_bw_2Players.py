# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 14:29:36 2021

@author: anves

"""
count=0
Word_list=["nice","ajax","leverkusen","juventus","barcelona",
          "real madrid","atletico madrid","atletico bilbao",
          "inter milan", "ac milan", "lazio","tottenham",
          "man united","man city","leeds united","watford"
          ,"chelsea","porto","benfica","dinamo zagreb",
          "rb leipzig","bayern munich","napoli","as roma",
          "nantes","lille","marseille","psv",
          "shaktar donetsk","besiktas", "sevilla",
          "villareal","wolfsburg","arsenal","olympiakos",
          "slavia prague","redstar belgrade","atalanta",
          "basel","zenit","celtic","rangers","valencia",
          "Frankfurt","Mönchengladbach","liverpool",
          "southampton","Fiorentina","schalke","lyon","wolves","westham united","everton"]
for i in Word_list:
    x=Word_list.count(i)
    count=count+1
    print(count,')',x,i)
print("\n")
print(count)