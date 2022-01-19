from module1 import *
rus_list=[]
eng_list=[]
rus_list=failist_lugemine("russkiy.txt",rus_list)
eng_list=failist_lugemine("english.txt",eng_list)
while True:
    print("Привет, ты зашел в словарь русско-английского и английско-русского перевода! \nЧто ты хочешь сделать?")
    menu=input("\ntranslate - перевести слово \nadd - добавить слово \nall - все слова, которые есть \ncontrol - Произвести слово \nerror - исправить слово \nВводи: ")
    if menu=="t":
        translate()
    elif menu=="add":
        rus_list=uus_sona("russkiy.txt",input("Новое слово:"))
        eng_list=uus_sona("english.txt",input("Uus sõna:"))
    elif menu=="all":
        print(rus_list)
        print(eng_list)
    elif menu=="control":
         wordControl()
    elif menu=="error":
        viga()
