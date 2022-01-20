from module1 import *
rus_list=[]
eng_list=[]
rus_list=failist_lugemine("russkiy.txt",rus_list)
eng_list=failist_lugemine("english.txt",eng_list)
while True:
    print("Привет, ты зашел в словарь русско-английского и английско-русского перевода! \nЧто ты хочешь сделать?")
    menu=input("\ntranslate - перевести слово \nadd - добавить слово \nall - все слова, которые есть \ncontrol - Произвести слово \nerror - ошибка \ncorrection - исправить \nВводи: ")
    if menu=="t":
        translate(rus_list,eng_list)
    elif menu=="add":
        rus_list=uus_sona("russkiy.txt",input("Русский: "))
        eng_list=uus_sona("english.txt",input("Английский: "))
    elif menu=="all":
        print(rus_list)
        print(eng_list)
    elif menu=="error":
        viga()
    elif menu=="correction"
        correction()

