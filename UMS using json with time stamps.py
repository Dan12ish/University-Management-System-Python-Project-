from json import dumps, loads
import time

def registration():
	def chk_reg():
		if (rno.isdigit() and len(rno)==6):
			print('  ',rno,"'Confirmed'")
			print('')		
		else:
			print('  **Invalid entry! Pleasr try again!**')
			reg()			
			
	def reg():
		global rno
		rno=input(' • Enter your 6 digit registration number: ')
		chk_reg()
	
	def chk_fname():
		for i in f1:
			if ((ord(i)>64 and ord(i)<91) or (ord(i)>96 and ord(i)<123)):
				continue
			else:
				print('  **Invalid entry. Please try again!**')
				fname()
				break
	
	def fname():
		global f1
		n=input(' • Enter your first name: ')
		f1=n.capitalize()
		chk_fname()
		
	def chk_lname():
		for i in l1:
			if ((ord(i)>64 and ord(i)<91) or (ord(i)>96 and ord(i)<123)):
				continue
			else:
				print('  **Invalid entry. Please try again!**')
				fname()
				break
	
	def lname():
		global l1
		n=input(' • Enter your last name: ')
		l1=n.capitalize()
		chk_lname()
	
	def chk_mobile():
		if (m.isdigit() and len(m)==10):
			print('  ',m,"'confirmed'")
			print('')
		else:
			print('  **Invalid entry! Pleasr try again!**')
			mobile()			

	def mobile():
		global m
		m=input(' • Enter your mobile no: ')
		chk_mobile()
	
	def chk_email():
		lst=em.split('@')
		if (lst[-1]=='gmail.com'):
			print('  ',em,"'confirmed'")
			print('*'*54)
		else:
			print('  **Invalid entry! Pleasr try again!**')
			email()
	
	def email():
		global em
		e=input(' • Enter your Google email: ')
		em=e.lower()
		chk_email()

	reg()
	fname()
	print('  ',f1, "'Confirmed'")
	print('')
	lname()
	print('  ',l1, "'Confirmed'")
	print('')
	mobile()
	email()
	
	txt=''
	student_data={}
	fd=open('Student_Data.json','r')
	txt=fd.read()
	student_data=loads(txt)
	dct={}
	dct['Name']=f1+' '+l1
	dct['Mobile']=m
	dct['Email']=em
	dct['Registered on']=time.ctime()
	student_data[rno]=dct
	txt=dumps(student_data)
	fd=open('Student_Data.json','w')
	fd.write(txt)
	fd.close()
	txts=''
	history={}
	fd=open('UMS_History.json','r')
	txts=fd.read()
	history=loads(txts)
	h={}
	h['frequency']=0
	h['time']=time.ctime()
	history[rno]=h
	txts=dumps(history)
	fd=open('UMS_History.json','w')
	fd.write(txts)
	fd.close()

def details():
	def chk_enreg():
		txt=''
		student_data={}
		fd=open('Student_Data.json', 'r')
		txt=fd.read()
		fd.close()
		student_data=loads(txt)
		if (rno in student_data.keys()):
			print('_'*54)
			print(' Registration Number : ',rno)
			print(' Name of the student : ', student_data[rno]['Name'])
			print(' Mobile Number          : ', student_data[rno]['Mobile'])
			print(' Email ID                       : ', student_data[rno]['Email'])
			print('_'*54)
			print(' Registered on             : ', student_data[rno]['Registered on'])
			fd=open('UMS_History.json','r')
			txts=fd.read()
			fd.close()
			history={}
			history=loads(txts)
			print(' No. of Times Viewed  : ',history[rno]['frequency'])
			print(' Last viewed on            : ',history[rno]['time'])
			print('_'*54)
			print('')
			print('*'*54)
			if (rno in history.keys()):
				history[rno]['frequency'] += 1
				history[rno]['time'] = time.ctime()
			else:
				log={}
				log['frequency']=1
				log['time']=time.ctime()
				history[rno]=log
			txts=''
			txts=dumps(history)
			fd=open('UMS_History.json','w')
			fd.write(txts)
			fd.close()
			
		else:
			print('  **Invalid entry! Pleasr try again!**')
			enreg()
	
	def enreg():
		global rno
		rno=input(' • Enter your 6 digit registered no: ')
		chk_enreg()
	
	enreg()

def start():
	st=input(' Enter option no: ')
	if (st==str(1)):
		print(" 1 'Confirmed'")
		print('-'*54)
		print('-'*54)
		registration()
	
	elif (st==str(2)):
		print(" 2 'Confirmed'")
		print('-'*54)
		print('-'*54)
		details()
		
	else:
		print(' **Invalid entry! Please try again!**')
		start()

print('*'*54)
print('Hello!\nPlease choose one option from below.\n 1. Registration\n 2. Check your details')
print('-'*54)
start()
