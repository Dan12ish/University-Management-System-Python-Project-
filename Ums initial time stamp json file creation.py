from json import loads, dumps
import time
rno='120401'
f1='Danish'
l1='Deepak'
m='1234567890'
em='danish@gmail.com'
student_data={}
dct={}
dct['Name']=f1+' '+l1
dct['Mobile']=m
dct['Email']=em
dct['Registered on']=time.ctime()
student_data[rno]=dct
txt=''
txt=dumps(student_data)
fd=open('Student_Data.json','w')
fd.write(txt)
fd.close()
history={}
h={}
history['frequency']=0
history['time']=time.ctime()
h[rno]=history
txts=''
txts=dumps(h)
fd=open('UMS_History.json','w')
fd.write(txts)
fd.close()
