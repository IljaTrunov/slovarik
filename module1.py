import os
from gtts import gTTS

def failist_lugemine(f:str,l:list):
	fail=open(f,"r",encoding="utf-8-sig") 
	for rida in fail:
		l.append(rida.strip())
	fail.close()
	return l
def failisse_salvestamine(f:str,l:list):
	fail=open(f,"w",encoding="utf-8-sig")
	for el in l:
		fail.write(el+"\n")
	fail.close()
def rida_salvestamine(f:str,rida:str):
	fail=open(f,"a",encoding="utf-8-sig")
	fail.write(rida+"\n")
	fail.close()
def uus_sona(f:str,rida:str)->list:
	l=[]
	with open(f,"a",encoding="utf-8-sig") as fail:
		fail.write(rida+"\n")
	l=failist_lugemine(f) 
	return l
def translate(l1:list,l2:list):
	sona=input("Что перевести?: ")
	if sona in l1:
		tolk=l2[l1.index(sona)]
		print(sona+"-"+tolk)
	elif sona in l2:
		tolk=l1[l2.index(sona)]
		print(sona+"-"+tolk)
	else:
		print("Этого слова не существует в словаре!")
def viga(l1:list,f1:str,l2:list,f2:str):
	word=input("В каком слова ошибка? ")
	if word not in l1 and word not in l2:
		print("Нету такого слова ")
	else:
		if word in l1:
			translate=l2[l1.index(word)]
			l1.remove(word)
			l2.remove(translate)
		elif word in l2:
			translate=l2[l1.index(word)]
			l2.remove(word)
			l1.remove(translate)
		l1.append(input("Введи слово: "))
		l2.append(input("Введи слово: "))
		failisse_salvestamine(f1,l1)
		failisse_salvestamine(f2,l2)
def correction(sona:str,l:list):
	for i in range(len(l)):
		if l[i]==sona:
			uus_sona=sona.replace(sona,input("Новое слово: "))
			l.insert(i,uus_sona)
			l.remove(sona)
	return l

def heli(text:str,keel:str):
	obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
	os.system("heli.mp3")

#import os
#from gtts import gTTS
#def heli(text:str,lang:str):
#	obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
#	os.system("heli.mp3")
