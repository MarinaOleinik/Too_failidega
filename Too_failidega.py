from Module import *
rus_list=loe_failist("rus.txt")
est_list=loe_failist("est.txt")

while True:
    menu=input("Rääkida -R,\nKõik sõnad -S,\nTõlgida-T,\nUus sõna-U,\nViga-V,\nKontroll-K;\nLõpp-L")
    if menu.upper()=="T":
        pass
    elif menu.upper()=="U":
        rus_list=uus_sona("rus.txt",input("Новое слово:"))
        est_list=uus_sona("est.txt",input("Uus sõna:"))
        
    elif menu.upper()=="V":
        keel=input("Mis keel?")
        if keel=="rus":
            rus_list=correction(input("Слово "),rus_list)
            failisse(rus_list,"rus.txt")
        else:
            est_list=correction(input("Sõna "),est_list)
            failisse(est_list,"est.txt")
    elif menu.upper()=="S":
        print(rus_list)
        print(est_list)
    elif menu.upper()=="R":
        keel=input("Mis keeles rääkida?")
        sonad=""
        if keel=="rus":
            mas=rus_list
            lang='ru'
        else:
            mas=est_list
            lang='fi'
        for sona in mas:
            sonad=sonad+" "+sona
        heli(sonad,lang)
    else:
        break














#file_read=open("TextFile.txt",'r',encoding="utf-8-sig")
#text=file_read.read()
#print(text)
#file_read.close()
#file_write=open("TextFile.txt",'a',encoding="utf-8-sig")
#text=input("Mis tekst on vaja lisada: ")
#file_write.write("\n"+text)
#file_write.close()
#with open("TextFile.txt",'r',encoding="utf-8-sig") as reader:
#    print(reader.read())
#with open("NewFile1.txt",'x') as f:
#    for i in range(5):
#        text=input("Mis tekst on vaja lisada: ")
#        f.write("\n"+text)
#with open("NewFile1.txt",'r') as f:
#    print(f.read())