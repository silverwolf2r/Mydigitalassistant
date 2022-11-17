#basically want to have a list of websites and we will google search for a book on these websites.
#The search would be title site:onlinereadfreenovel.com
#We then copy the text from the book, turn it into a pdf and email it to oursleves.
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
import isbnlib
import fpdf
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import random
import speech_recognition as sr
import win32com.client as wincl
import winsound

def speak(text):
    #speak the text
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(text)

def listen():
    ad = None
    frequency = 2500  # Set Frequency To 2500 Hertz

    duration = 100  # Set Duration To 1000 ms == 1 second

    while ad == None:
        try:
            # obtain audio from the microphone
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening")
                winsound.Beep(frequency, duration)
                audio = r.listen(source)
            
            #recognize audio and assign it to a variable   
            x = (r.recognize_google(audio))
            text = str(r.recognize_google(audio))
            print("You said " + text)
            return text
        except:
            ad = None

#----------------------------------------------------
#Finding the book title
#----------------------------------------------------
speak("What book do you want emailed to you")
gtitle = listen()
book = isbnlib.goom(gtitle + ' ' ) 
isbn1 = book[0]
isbn = str(isbn1)
# I want the first 28 characters of str isbn
isbn = isbn[13:26]
book = isbnlib.meta(isbn)
title = book['Title']
author = book['Authors']
print('\n')	
print('\n')	
print('Title: ' + str(title) + '\n' + 'Author: ' + str(author))
print('\n ISBN: ' + isbn)

#----------------------------------------------------
#Formulate the google query and results
#----------------------------------------------------
resultinglinks = []
searching = str(title) + ' "Page 1" site:'
x = 0
links = ["onlinereadfreenovel.com", "readonlinefreenovel.com", "novel80.com", "thefreeonlinenovel.com", "readonlinefreebook.com", "lovefreenovels.com", "novel122.com", "www.topbooks2019.com", "allnovel.net", "www.superbook4u.net", "www.go2reads.com" ]
for link in links:
	randnum = random.randint(1, 4)
	time.sleep(randnum)
	query = searching + link
	result = search(query , num_results=0)
	resultinglinks.append(result)


for results in resultinglinks:
	x = x + 1
	linkresults = str(x) + " " + str(results)
	print(linkresults)
	
#---------------------------------------------------
#Use the chosen link to download
#---------------------------------------------------	

speak("Which link would you like to download?")
chosenlink = listen()
chosenlink = int(chosenlink) - 1
link = (resultinglinks[chosenlink])
link = str(link).replace("'","")
link = str(link).replace("[","")
link = str(link).replace("]","")
#for each link I need to format a way to download it from that link no matter how odd the link is




try:
	#DOWNLOAD INFORMATION FOR EACH LINK RIGHT NOW
	#link1 onlinereadfreenovel.com
	#-------------------------------------------------textid, Page_next
	if chosenlink == 0:

		textid = "textToRead"
		Nextpage = "→"
		
		#prep a document for the book to be written too
		tity = ''.join(filter(str.isalpha, title))
		f = open( str(tity) + ".txt", "w") 
		f.write("HERE IS YOUR BOOK:   ")
		f.close()

		#set for how many iterations this will run for
		tfoncode = int(275)
		x = 0
		linksy = (link[:31])
		while x < tfoncode + 1:
			x = x + 1
			#Get the html from the webpage 
			res = requests.get(link)
			text = res.text
			
			# Take the text and parses the html out so that it is easy to read
			soup = BeautifulSoup(text, 'html.parser')
			title = soup.title.string
			akt = soup.find(id=textid)
			text = akt.text 
			
			#Write the page to the document
			startpage = int(x)
			final_product = (str(title) + str(text) )
			fp = final_product # tfontext requires parsing everytime
			f = open( str(tity) + ".txt", "a") # write page to the document
			f.write(fp)
			f.close()
			print(startpage ,"/",tfoncode )
			startpage = startpage + 1
			
			#get the next url rinse and repeat
			#get the next url rinse and repeat
			for links in soup.find_all('a',href=True, text=Nextpage):
				links = links.get('href')
			link = str(linksy) + str(links)
			


	#link2 readonlinefreenovel.com
	#-------------------------------------------------search by class=content, class "active"
	elif chosenlink == 1:

		textid = "p"
		Nextpage = "active"
		
		#prep a document for the book to be written too
		tity = ''.join(filter(str.isalpha, title))
		f = open( str(tity) + ".txt", "w") 
		f.write("HERE IS YOUR BOOK:   ")
		f.close()

		#set for how many iterations this will run for
		tfoncode = int(275)
		x = -1
		linksy = (link[:31])
		while x < tfoncode + 1:
			x = x + 1
			#Get the html from the webpage 
			res = requests.get(link)
			text = res.text
			
			# Take the text and parses the html out so that it is easy to read
			soup = BeautifulSoup(text, 'html.parser')
			title = soup.title.string
			akt = soup.find("div", class_="content")
			text = akt.text
			
			#Write the page to the document
			startpage = int(x)
			final_product = (str(title) + str(text) )
			fp = final_product # tfontext requires parsing everytime
			f = open( str(tity) + ".txt", "a") # write page to the document
			f.write(fp)
			f.close()
			print(startpage ,"/",tfoncode )
			startpage = startpage + 1
			
			#get the next url rinse and repeat
			for links in soup.find_all('a',href=True,class_="active"):
				links = links.get('href')
			link = str(linksy) + str(links)
			
			

	#link3 novel80.com 
	#-------------------------------------------------search by chapter-content, search for Next page		
	elif chosenlink == 2:

		textid = "p"
		Nextpage = "Next page"
		
		#prep a document for the book to be written too
		tity = ''.join(filter(str.isalpha, title))
		f = open( str(tity) + ".txt", "w") 
		f.write("HERE IS YOUR BOOK:   ")
		f.close()

		#set for how many iterations this will run for
		tfoncode = int(275)
		x = 0
		linksy = (link[:19])
		while x < tfoncode + 1:
			x = x + 1
			#Get the html from the webpage 
			res = requests.get(link)
			text = res.text
			
			# Take the text and parses the html out so that it is easy to read
			soup = BeautifulSoup(text, 'html.parser')
			title = soup.title.string
			akt = soup.find("div", class_="chapter-content")
			text = akt.text
			
			#Write the page to the document
			startpage = int(x)
			final_product = (str(title) + str(text) )
			fp = final_product # tfontext requires parsing everytime
			f = open( str(tity) + ".txt", "a") # write page to the document
			f.write(fp)
			f.close()
			print(startpage ,"/",tfoncode )
			startpage = startpage + 1
			
			#get the next url rinse and repeat
			for links in soup.find_all('a',href=True, text=Nextpage):
				links = links.get('href')
				link = str(linksy) + str(links)
			
			
	#link4 thefreeonlinenovel.com	
	#Needs Revision
	#-------------------------------------------------textid <td>, linksy
	elif chosenlink == 3:

		textid = "td"
		Nextpage = "Next Page"
		print('This link needs revision and will most likely break. Feel free to try but eh...')
		#prep a document for the book to be written too
		tity = ''.join(filter(str.isalpha, title))
		f = open( str(tity) + ".txt", "w") 
		f.write("HERE IS YOUR BOOK:   ")
		f.close()

		#set for how many iterations this will run for
		tfoncode = int(275)
		x = 0
		linksyl = link
		linksy = (linksyl[-1])
		linksy = linksyl.replace(linksy, "")
		while x < tfoncode + 1:
			x = x + 1
			#Get the html from the webpage 
			res = requests.get(link)
			text = res.text
			
			# Take the text and parses the html out so that it is easy to read
			soup = BeautifulSoup(text, 'html.parser')
			title = soup.title.string
			akt = soup.find(textid)
			text = akt.text
			
			#Write the page to the document
			startpage = int(x)
			final_product = (str(title) + str(text) )
			fp = final_product # tfontext requires parsing everytime
			f = open( str(tity) + ".txt", "a") # write page to the document
			f.write(fp)
			f.close()
			print(startpage ,"/",tfoncode )
			startpage = startpage + 1
			
			#get the next url rinse and repeat
			
			link = str(linksy) + str(x)
			
	#link5 readonlinefreebook.com
	#-------------------------------------------------search for class content_novel, search for class of nextpage
	elif chosenlink == 4:

		textid = "p"
		res = requests.get(link)
		text = res.text
		soup = BeautifulSoup(text, 'html.parser')
		Nextpage = soup.find_all("div", class_="fa fa-angle-right")
		
		#prep a document for the book to be written too
		tity = ''.join(filter(str.isalpha, title))
		f = open( str(tity) + ".txt", "w") 
		f.write("HERE IS YOUR BOOK:   ")
		f.close()

		#set for how many iterations this will run for
		tfoncode = int(275)
		x = 0
		while x < tfoncode + 1:
			x = x + 1
			#Get the html from the webpage 
			res = requests.get(link)
			text = res.text
			
			# Take the text and parses the html out so that it is easy to read
			soup = BeautifulSoup(text, 'html.parser')
			title = soup.title.string
			akt = soup.find("div", class_="content_novel")
			text = akt.text
			
			#Write the page to the document
			startpage = int(x)
			final_product = (str(title) + str(text) )
			fp = final_product # tfontext requires parsing everytime
			f = open( str(tity) + ".txt", "a") # write page to the document
			f.write(fp)
			f.close()
			print(startpage ,"/",tfoncode )
			startpage = startpage + 1
			
			#get the next url rinse and repeat
			for links in Nextpage:
				print(links)
				link = links

	#link6 lovefreenovels.com
	#-------------------------------------------------search for text class, search for text
	elif chosenlink == 5:

		textid = "text"
		Nextpage = "Next"
		
		#prep a document for the book to be written too
		tity = ''.join(filter(str.isalpha, title))
		f = open( str(tity) + ".txt", "w") 
		f.write("HERE IS YOUR BOOK:   ")
		f.close()

		#set for how many iterations this will run for
		tfoncode = int(275)
		x = 0
		linksy = (link[:-9])
		while x < tfoncode + 1:
			x = x + 1
			#Get the html from the webpage 
			res = requests.get(link)
			text = res.text
			
			# Take the text and parses the html out so that it is easy to read
			soup = BeautifulSoup(text, 'html.parser')
			title = soup.title.string
			akt = soup.find("div", class_="text")
			text = akt.text 

			
			#Write the page to the document
			startpage = int(x)
			final_product = (str(title) + str(text) )
			fp = final_product # tfontext requires parsing everytime
			f = open( str(tity) + ".txt", "a") # write page to the document
			f.write(fp)
			f.close()
			print(startpage ,"/",tfoncode )
			startpage = startpage + 1
			
			#get the next url rinse and repeat
			for links in soup.find_all('a',href=True, text=Nextpage):
				links = links.get('href')
				link = str(linksy) + str(links)
		
	#link7 novel122.com
	#-------------------------------------------------search by classs=chapter-content-p, search by class btn-blue
	elif chosenlink == 6:

		textid = "btn-blue"
		res = requests.get(link)
		text = res.text
		soup = BeautifulSoup(text, 'html.parser')
		Nextpage = soup.find_all("div", class_="next-page")
		
		#prep a document for the book to be written too
		tity = ''.join(filter(str.isalpha, title))
		f = open( str(tity) + ".txt", "w") 
		f.write("HERE IS YOUR BOOK:   ")
		f.close()

		#set for how many iterations this will run for
		tfoncode = int(275)
		x = 0
		while x < tfoncode + 1:
			x = x + 1
			#Get the html from the webpage 
			res = requests.get(link)
			text = res.text
			
			# Take the text and parses the html out so that it is easy to read
			soup = BeautifulSoup(text, 'html.parser')
			title = soup.title.string
			akt = soup.find("div", class_="chapter-content-p")
			text = akt.text
			
			#Write the page to the document
			startpage = int(x)
			final_product = (str(title) + str(text) )
			fp = final_product # tfontext requires parsing everytime
			f = open( str(tity) + ".txt", "a") # write page to the document
			f.write(fp)
			f.close()
			print(startpage ,"/",tfoncode )
			startpage = startpage + 1
			
			#get the next url rinse and repeat
			for links in Nextpage:
				print(links)
				link = links
			
			


	#link8 www.topbooks2019.com
	#-------------------------------------------------textid <p>, linksy
	elif chosenlink == 7:

		textid = "p"
		Nextpage = "Next"
		
		#prep a document for the book to be written too
		tity = ''.join(filter(str.isalpha, title))
		f = open( str(tity) + ".txt", "w") 
		f.write("HERE IS YOUR BOOK:   ")
		f.close()

		#set for how many iterations this will run for
		tfoncode = int(275)
		x = 0
		linksy = link
		while x < tfoncode + 1:
			x = x + 1
			#Get the html from the webpage 
			res = requests.get(link)
			text = res.text
			
			# Take the text and parses the html out so that it is easy to read
			soup = BeautifulSoup(text, 'html.parser')
			title = soup.title.string
			akt = soup.find("div", class_="main")
			text = akt.text 
			
			#Write the page to the document
			startpage = int(x)
			final_product = (str(title) + str(text) )
			fp = final_product # tfontext requires parsing everytime
			f = open( str(tity) + ".txt", "a") # write page to the document
			f.write(fp)
			f.close()
			print(startpage ,"/",tfoncode )
			startpage = startpage + 1
			
			#get the next url rinse and repeat
			link = str(linksy) +  "index_" + str(startpage) + ".html"





	#link9 allnovel.net
	#-------------------------------------------------textid <p>, linksy
	if chosenlink == 8:
	
		textid = "p"
		Nextpage = "❯"
			
			
	#prep a document for the book to be written too
		tity = ''.join(filter(str.isalpha, title))
		f = open( str(tity) + ".txt", "w") 
		f.write("HERE IS YOUR BOOK:   ")
		f.close()
		#set for how many iterations this will run for
		tfoncode = int(275)
		x = 0
		linksy = (link[:-5])
		link = str(linksy)+ "/page-" + str(x) + ".html"
		while x < tfoncode + 1:
			x = x + 1
			#Get the html from the webpage 
			res = requests.get(link)
			text = res.text
		
			# Take the text and parses the html out so that it is easy to ead
			soup = BeautifulSoup(text, 'html.parser')
			#title = soup.title.string
			akt = soup.find("div", class_="col-md-9 col-xs-12")
			text = akt.text 
		
			#Write the page to the document
			startpage = int(x)
			final_product = (str(title) + str(text) )
			fp = final_product # tfontext requires parsing everytime
			f = open( str(tity) + ".txt", "a") # write page to the document
			f.write(fp)
			f.close()
			print(startpage ,"/",tfoncode )
			startpage = startpage + 1
		
			#get the next url rinse and repeat
			link = str(linksy)+ "/page-" + str(x) + ".html"





	#link10 www.superbook4u.net
	#-------------------------------------------------textid <p>, linksy
	elif chosenlink == 9:

		textid = "p"
		Nextpage = "Next"
		
		#prep a document for the book to be written too
		tity = ''.join(filter(str.isalpha, title))
		f = open( str(tity) + ".txt", "w") 
		f.write("HERE IS YOUR BOOK:   ")
		f.close()

		#set for how many iterations this will run for
		tfoncode = int(275)
		x = 0
		linksy = (link[:-5])
		while x < tfoncode + 1:
			x = x + 1
			#Get the html from the webpage 
			res = requests.get(link)
			text = res.text
			
			# Take the text and parses the html out so that it is easy to read
			soup = BeautifulSoup(text, 'html.parser')
			title = soup.title.string
			akt = soup.find("div", class_="text")
			text = akt.text 
			
			#Write the page to the document
			startpage = int(x)
			final_product = (str(title) + str(text) )
			fp = final_product # tfontext requires parsing everytime
			f = open( str(tity) + ".txt", "a") # write page to the document
			f.write(fp)
			f.close()
			print(startpage ,"/",tfoncode )
			startpage = startpage + 1
			
			#get the next url rinse and repeat
			link = str(linksy) +  "_" + str(startpage) + ".html"






	#link11 wwww.go2reads.com
	#-------------------------------------------------textid <p>, linksy
	elif chosenlink == 10:

		textid = "p"
		Nextpage = "Next Page"
		
		#prep a document for the book to be written too
		tity = ''.join(filter(str.isalpha, title))
		f = open( str(tity) + ".txt", "w") 
		f.write("HERE IS YOUR BOOK:   ")
		f.close()

		#set for how many iterations this will run for
		tfoncode = int(275)
		x = 0
		linksy = (link[:24])
		while x < tfoncode + 1:
			x = x + 1
			#Get the html from the webpage 
			res = requests.get(link)
			text = res.text
			
			# Take the text and parses the html out so that it is easy to read
			soup = BeautifulSoup(text, 'html.parser')
			title = soup.title.string
			akt = soup.find("div", class_="content")
			text = akt.text 
			
			#Write the page to the document
			startpage = int(x)
			final_product = (str(title) + str(text) )
			fp = final_product # tfontext requires parsing everytime
			f = open( str(tity) + ".txt", "a") # write page to the document
			f.write(fp)
			f.close()
			print(startpage ,"/",tfoncode )
			startpage = startpage + 1
			
			#get the next url rinse and repeat
			for links in soup.find_all('a',href=True,class_="active"):
				links = links.get('href')
			link = str(linksy) + str(links)













except:
	pass

		
		
		
		
		
		
		
pdf = fpdf.FPDF(format='letter')

# Read text file
name = (str(tity) + ".txt")
with open(name, 'r') as f:
	txt = f.read()




pdf.add_page()
pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
pdf.set_font('DejaVu', '', 12)
pdf.multi_cell(0, 5, txt,0,'R')
pdf.ln()
pdf.cell(0, 5, 'End')
pdf.output(str(tity) + ".pdf")
		




name = (str(tity) + ".pdf")		
#Send the pdf as an email to myself

mail_content = '''Hello,
Here is your book in pdf form.
'''

#The mail addresses and password
sender_address = 'tok6burg@gmail.com'
sender_pass = 'ufekkxiswdrgovkk'
receiver_address = 'tok6burg@gmail.com'

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = name


#Attach the body
message.attach(MIMEText(mail_content, 'plain'))

# open the file in bynary
binary_pdf = open(name, 'rb')
 
payload = MIMEBase('application', 'octate-stream', Name=name)
payload.set_payload((binary_pdf).read())
 
# enconding the binary into base64
encoders.encode_base64(payload)
 
# add header with pdf name
payload.add_header('Content-Decomposition', 'attachment', filename=name)
message.attach(payload)




#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()


print('Mail Sent')

				
		
		
		
		
		
		
