from Module import *
rus_list=loe_failist("rus.txt")
est_list=loe_failist("est.txt")
print(rus_list)
print(est_list)
sonad=""
for sona in rus_list:
    sonad=sonad+sona
heli(sonad,'ru')

while True:
    menu=input("Tõlgida-T,\nUus sõna-U\n,Viga-V,\nKontroll-K;\nLõpp-L")
    if menu.upper()=="T":
        pass
    elif menu.upper()=="U":
        rus_list=uus_sona("rus.txt",input("Новое слово:"))
        est_list=uus_sona("est.txt",input("Uus sõna:"))
        pass
    elif menu.upper()=="V":
        pass
    elif menu.upper()=="K":
        pass
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