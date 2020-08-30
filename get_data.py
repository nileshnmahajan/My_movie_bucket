import requests
import os
import threading
import time
url='http://mahajan1.000webhostapp.com/add_post.php'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
def post(data,count):
	try:
		x = requests.post(url, data = myobj,headers=headers)
		print("finish",count)
	except:
		time.sleep(4)
		t1 = threading.Thread(target=post, args=(data,count)) 
		t1.start()
		
file_= os.walk("marathi")
count=0
for i in file_:
	files=i[2]
	for title in files:
		try:
			count+=1
			content=open("marathi/"+title,"r",encoding="UTF-8").read().replace("\n","</br>")
			myobj = {'content': content,'title':title}
			t1 = threading.Thread(target=post, args=(myobj,count)) 
			t1.start()
			print("send ",count)	
			time.sleep(1)
		except:
			print("error in ",count)
		
		
#before 2210


#after 		

#added from this