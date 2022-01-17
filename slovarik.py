from module1 import *
rus=[]
eng=[]
variant=""
print("Привет!")
variant=int(input("Ты зашел в словарь. Напиши что ты хочешь сделать: \n1-перевести слово с русского на английский из предоставленных \n2-добавить свое слово и свой перевод \n3-перевести слово с английского на русский из предоставленных \n4-выйти \nВводи: "))
def choice():
    if variant==1:
        RuEng()
    elif variant==2:
        AddWordTranslate()
    elif variant==3:
        EngRu()
    elif variant==4:
        quit
def RuEng():
    fail=open(russkiy.txt,"r")
    fail=open(english.txt,"r")
    slovo=input("Выбери слово, которое хочешь перевести: ")
    if slovo=="арбуз":