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
def translate(rus:list,eng:list):
    word=input("Что переводить?")
    if word in l1:
        translate=l2[l1.index(word)]
        print(word+"-"+translate)
    elif word in l2:
        translate=l1[l2.index(word)]
        print(word+"-"+translate)
    else:
        print("Такого слова нету в словаре!")
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
def wordControl():
	while 1:
		print("Если хочешь выйти, напиши q")
		word=input("Введи слово и его перевод: ")
		if word in l1 and word in l2:
			print("Молодец")
		elif word=="q":
			quit
#import os
#from gtts import gTTS
#def heli(text:str,lang:str):
#	obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
#	os.system("heli.mp3")
