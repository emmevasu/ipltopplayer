# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from django.core.management.base import BaseCommand
from urllib.request import urlopen
from bs4 import BeautifulSoup



def IplTopScorer(requests, num):

    page=urlopen('https://www.iplt20.com/stats/2020/most-runs')

    soup=BeautifulSoup(page,'html.parser')

    lead=soup.findAll('div' ,attrs={'class':'stats-table'})
    player=lead[0].findAll('span',attrs={'class':'top-players__last-name'})
    score=lead[0].findAll('td',attrs={'class':'top-players__r is-active'})
        # player[:i].text.strip()
    player_names=[]

    player_scores=[]

    Top_Players=zip(player_names,player_scores)

    for i in range(0,num):

            # player=lead[0].findAll('span',attrs={'class':'top-players__last-name'})

        player_names.append(player[i].text.strip())

            # score=lead[0].findAll('td',attrs={'class':'top-players__r is-active'})

        player_scores.append(score[i].text.strip())

        # player_names.save()
        # player_scores.save()

    return render(requests,'details.html',{'data':Top_Players})

def Input(request):
    return render(request,'input.html')
