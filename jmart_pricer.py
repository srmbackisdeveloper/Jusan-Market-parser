import requests
from bs4 import BeautifulSoup as bs

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('JMart Pricer')
root.geometry('500x300')
root.resizable(width=False, height=False)




# url = input('URL = ')

url = ''
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
           'accept': '*/*'}

# functions

def get_html(url, params=None):
  my_request = requests.get(url_taker(), headers=headers, params=params)
  return my_request

def get_name(html):
  soup = bs(html, 'html.parser')
  price = soup.find_all('h1', class_=['sc-kDTinF', 'cUbUIS'])
  ##########
  if len(price) == 0:
  	price.append('empty')

  # full name
  print(price[0].get_text())

  result = price[0].get_text()
  return (result.split()[:4]) # 4 words only output

def get_price(html):
  soup = bs(html, 'html.parser')
  price = soup.find_all('div', class_=['geGYKT'])

  ##########
  if len(price) == 0:
  	price.append('empty')
  	# CONTINUE HEREEEEEEEEEEEEEEEEEEEE
  	return price[0]

  print(price[0].get_text())
  return (price[0].get_text())

def parse_name():
	html = get_html(url_taker())

	if html.status_code == 200:
	    name_view = get_name(html.text)
	    return name_view
	else:
		print('Error')

def parse_price():
	html = get_html(url_taker())

	if html.status_code == 200:
	    price_view = get_price(html.text)
	    return price_view
	else:
		print('Error')



def run():
	messagebox.askyesnocancel(parse_name(), parse_price())

def url_taker():
	############################################################################################
	if data.get():
		url_taken = 'https://jmart.kz/products/' + data.get() + '/P'
		label_success_url.config(text='URL:\n' + url_taken + '\nhas been set up.')
	else:
		messagebox.showinfo('Error!', 'None entered')
	
	print(url_taken)
	return url_taken



l1 = Label(root, text = "JMart Pricer by srmback", font=("Arial", 12))
l1.pack()

print()

data = StringVar()

entry = Entry(root, textvariable=data)
entry.pack()

btn1 = Button(root, text = "Take URL", font=("Arial", 9), command = url_taker)
btn1.pack()

label_success_url = Label(root, font=("Arial", 9))
label_success_url.pack()


btn2 = Button(root, text = "Run", command = run)
btn2.pack()


root.mainloop()