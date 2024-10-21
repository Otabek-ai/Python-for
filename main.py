# FUNKSIYALAR
from os.path import split

# def salom_dunyo ():
#     """Salom beruvchi funksiya :) """
#     print("Salom dunyo :")
# print(salom_dunyo())

# def agent_malumot(ism,familiya,sharif = " "):
#     if sharif :
#         axa = (f"{ism} {familiya} {sharif}")
#     else:
#         axa = (f"{ism} {familiya}")
#     return axa.title()
#
# asd = agent_malumot("shahram" , "olimov","saliev")
# print(asd)


# def yosh_hisobla(ism, tugulgan_yil):
#     print(f"{ism} {2024 - tugulgan_yil} yoshda")
#
# yosh_hisobla(ism = "olim " , tugulgan_yil = 1990)


# def toliq_ism_yasa(ism, familiya):
#     """Toliq ism yasash uchun"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
#
# asd = toliq_ism_yasa("ali" ,"botirov")
# print(asd)

#     LUG'AT ROYHAT KO'RINISHIDA

# def  avto_info(Komp,model,rangi,karobka,narhi=None):
#     avto = { "Kompaniya" : Komp,
#              "Model" : model,
#              "Rangi" : rangi,
#              "Karobka" : karobka,
#              "Narhi" : narhi}
#     return avto

# avto1 = avto_info("Ford","Ford_GTR","Kumush","Avtomat",)
# avto2 = avto_info("Ferrari","Ferrari_gtx_6F","Qizil","Avtomat",27_000)

# avtolar = [avto1,avto2]
# for avto in avtolar:
#     if avto["Narhi"]:
#         narh = avto["Narhi"]
#     else:
#         narh = "Narh belgilanmagan"
#     print(f"{avto["Rangi"]} {avto['Kompaniya']} Narhi : {narh}")



# 1 chi masala

# def salom_dunyo():
#     return "Hello world"
#
# print(salom_dunyo())

# 2 chi masala


# def Salom_beruvchi(ism):
#     """BU dastur ismga salom beradi"""
#     return "Hello " + ism.title()
#
# a = input("Isminggizni kiriting :")
# salom = Salom_beruvchi(a)
# print(salom)


# 3 chi masala

# def ikkita_sonni_qosh(a,b):
#     """BU funksiya ikkita sonni qoshadi"""
#     return a+b
#
# a = int(input("A sonini kiriting :"))
# b = int(input("B sonini kiriting :"))
# print(ikkita_sonni_qosh(a,b))

# 4 ci masala

# def salom_dostim(name="Guest"):
#     return f"Hello {name.title()}"
#
# ism = input("ISminggizni kiriting :")
# print(salom_dostim(ism if ism else "Guest"))

# 5 chi masala


# def son_KV(a):
#     """BU funksiya son kvadrstini qaytaradi"""
#     return a ** 2
#
# son = int(input("Son kiriting : "))
# print(son_KV(son))


# 6 chi masala

# son_kv = lambda x: x ** 2
#
# qiymat = int(input("Son kiriting : "))
# print(son_kv(qiymat))

# 7 chi masala

# sonlarni_qosh = lambda a,b: a + b
#
# a = int(input('A sonini kiriting : '))
# b = int(input('B sonini kiriting : '))
# print(sonlarni_qosh(a,b))

# 8 chi masala

# def faktorial(w):
#     if w == 1:
#         return 1
#     else:
#         return w * faktorial(w - 1)
# qiymat = int(input("Son kiriting : "))
# print(faktorial(qiymat))

# 9 chi masala  # MASALA ISHLANMADI

# def fun():
#     return 1, 2
#
# print(fun())


# 10 chi masala

# def juftmi(a):
#     if a % 2 == 0:
#         return "JUFT SON"
#     else:
#         return "TOQ SON"
#
#
# a = int(input("Enter a number: "))
# print(juftmi(a))


# 11 chi masala  # MASALA ISHLANMADI







# 12 chi masala # MASALA ISHLANMADI





# 13 chi masala # MASALA ISHLANMADI






# 14 chi masala

# def juft_sonlar(sanoq):
#     return [son for son in sanoq if son % 2 == 0]
#
# royhat = [2,5,6,5,7,8,56,35,678]
# print(juft_sonlar(royhat))

# 15 chi masala

# def royhatda_kv(sonlar):
#     return [son ** 2 for son in sonlar ]
#
# royhat = [2,4,68,23,9,12]
# print(royhatda_kv(royhat))

# 16 chi masala

""""""































