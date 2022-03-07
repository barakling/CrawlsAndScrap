from bs4 import BeautifulSoup
import requests
import re
import random
import csv

#Python class for declaring movie attribtues.
class ExtractMovies(object):
    def __init__(self, position ,title, year,  star, ratings ):
        self.position = position
        self.title = title
        self.year = year
        self.star = star
        self.ratings = ratings
            
def first2(s):
    return s[:4]


url = 'https://www.imdb.com/chart/top/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

movies = soup.select('td.titleColumn')

links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
years = soup.select('span.secondaryInfo')


_temp_ = []

#loop to get and assign class instances
for index in range(0, len(movies)):
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7].replace('"', '')
    year = years[index].get_text() 
    position = index+1
    movie_instances = ExtractMovies(
        movie_title, year, position, crew[index], first2(ratings[index])
        )
    _temp_.append(movie_instances)

#shuffling array to randomize movies
#random.shuffle(_temp_)

filename = 'movies.csv'
f = open(filename,'w',encoding='UTF8',newline='')


music = csv.writer(f,delimiter=';')

i=1    
for obj in _temp_:
        data = ({i,  obj.title, obj.year,  obj.star, obj.ratings} )
        i=i+1        
        if(i==10):
            break
     
        music.writerow(data)
#music.writerow(_temp_) #Writing to CSV