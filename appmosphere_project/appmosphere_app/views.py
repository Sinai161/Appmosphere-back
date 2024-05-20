from django.shortcuts import render
from pymongo import MongoClient
client = MongoClient('mongodb+srv:QiSATtCQFlwN58VU//ashleygalvan161:@cluster161.sjfxrgd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster161')
db = client['appmosphere-db']


