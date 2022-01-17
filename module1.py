def failist_lugemine(f:str,l:list):
    fail=open(russkiy.txt,"r")
    for line in fail:
        l.append(rida.strip())
    fail.close()
    return l
def failisse_salvestamine():
    """Loetelu salvestame failis
    """
    fail=open(f,'w')
    for el in l:
        fail.write(el+'\n')
    fail.close()
def rida_salvestamine(f:str,rida:str):
    """üks sõna või lause(rida) savestame failisse
    """
    fail=open(f,'a')
    fail.write(rida+'\n')
    fail.close()
def loe_failist(file:str)->list:
	"""loeme failist read ja lisame järjendisse
	:param str file: faili nimetus
	"""
	fail=open(file,'r',encoding="utf-8-sig"
	mas=[]
