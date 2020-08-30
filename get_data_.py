import os
import json
import time
import mysql.connector as sql

def get_database(db='movie_track_rec_sys'):
	db=sql.connect(host="localhost",
	user="root",
	password="",
	database=db)
	return db
	
def get_cursor(db):
	c=db.cursor()
	return c
	
	
def insert(table,cols,values,url=""):

	db=get_database()
	c=get_cursor(db)
	sql="insert into %s %s values %s"%(table,str(cols).replace("'",""),str(values))
	try:
		c.execute(sql)
		db.commit()
		db.close()
		return 1
	except Exception as e:
		db.close()
		print("________________________________________________________________________")
		print(sql)
		print(url)
		print(str(e))
		print("________________________________________________________________________")
		return 0
		
#print("insert", "success" if insert("movie",('id','title'),(121214,"rab ne bana di jodi"))==1 else "fail")

import urllib.request

import requests
import threading
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}





urls=[
'https://api.themoviedb.org/3/movie/upcoming?api_key=c1371addc23fee06162831af28edc760&region=IN&language=hi-IN',
'https://api.themoviedb.org/3/movie/latest?api_key=c1371addc23fee06162831af28edc760&region=IN&language=hi-IN',
'https://api.themoviedb.org/3/movie/popular?api_key=c1371addc23fee06162831af28edc760&region=IN&language=hi-IN'
]

urls=['https://api.themoviedb.org/3/movie/latest?api_key=c1371addc23fee06162831af28edc760&region=IN&language=hi-IN']

def fetch(url,page_):
	
	url=url+'&page='+str(page_)
	page = requests.get(url, headers=headers)
	page_data=page.content.decode()
	x=json.loads(page_data)
	if(url.split("/")[5].split("?")[0]=="latest"):
		total_pages=500
		cols=tuple(x.keys())
		values=tuple(str(x) for x in x.values())
		insert("movie",cols,values,url)
		#print("insert", "success" if insert("movie",cols,values,url)==1 else "fail")
	else:
		total_pages=x['total_pages']
	

		for movie in x['results']:
			cols=tuple(movie.keys())
			values=tuple(str(x) for x in movie.values())
			insert("movie",cols,values,url)
			#print("insert", "success" if insert("movie",cols,values,url)==1 else "fail")	
	
	if(page_==1):
		return total_pages
	else :
		return 1
		
#itrate for each page
for base in urls:
	total_pages=fetch(base,1)
	print(base.split("/")[5].split("?")[0]," pages ",total_pages)
	if(total_pages>1):
		for page in range(51,total_pages):
			t1 = threading.Thread(target=fetch,args=(base,page)) 
			t1.start()
			time.sleep(1)