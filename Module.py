def loe_failist(file:str)->list:
    """Loeme failist read ja lisame järjendisse
    :param str file: Faili nimetus
    """
    fail=open(file,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
def uus_sona(file:str,x:str)->list:
    """Lisame uus sõna failisse ja listisse
    :param str file: Faili nimetus
    :param str x: lisatav sõna
    """
    mas=[] 
    with open(file,"a",encoding="utf-8-sig") as f:
        f.write(x+"\n")
    mas=loe_failist(file)
    return mas
def correction(sona,mas):
    for i in range(len(mas)):
        if mas[i]==sona:
            uus_sona=sona.raplace(sona,input("UUs sõna"))
            mas.insert(i,sona)
            mas.remove(sona)
    return mas
def failisse(mas:list,file:str):
    f=open(file,'w',encoding="utf-8-sig")
    for sona in mas:
        f.write(sona+'\n')
    f.close()


import os
from gtts import gTTS
from playsound import playsound
def heli(text:str,keel:str):
    obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
    os.system("heli.mp3")
    #playsound("heli.mp3")
