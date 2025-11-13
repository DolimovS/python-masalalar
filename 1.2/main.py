# text=input("Matnni kiriting:")
# print("Kititilgan matn:",text)  


# son=input("Sonni kitriting:")
# print("Siz kiritgan son:",son)  


# a=int(input("a="))
# b=int(input("b="))

# s=a+b
# d=a-b
# k=a*b

# print("Yig'indi:",s ,"\nAyirma:",d ,"\nKo'paytma:",k)

# x=float(input("x="))
# y=float(input("y="))

# s=(abs(x)-abs(y))/(1+abs(x*y))
# print(s)


# a=int(input("Kubni qirrasini kiriting:"))

# s=a*a
# v=s*6

# print("Yon sirti yuzasi :",s , "\nTo'la sirti yuzasi:",v)

# import math

# a=int(input("a="))
# b=int(input("b="))

# s=(a+b)/2
# y=math.sqrt(a*b)

# print("O'rta arifmetigi:",s,"\nO'rta geometrigi",y)

# import math
# a=int(input("a="))
# b=int(input("b="))

# c=math.sqrt(pow(a,2)+pow(b,2))

# s=(a+b)/2
# print("Gipatenuza:", c ,"\nYuza",s)

# 9

# t1=int(input("t1:"))
# t2=int(input("t2:"))
# v1=int(input("v1:"))
# v2=int(input("v2:"))

# V=v1+v2
# T = (t1 * v1 + t2 * v2) / (v1 + v2)
# print("Hajmi:",V, "Tempratura:",T)

# ========================================================================
# 10
# Radiusi r bo‘lgan aylanaga tashqi chizilgan muntazam n-burchakning
# perimetrini toping.
# import math
# r=int(input("Aylana radiusi:"))
# n=int(input("Burchaklar soni:"))
# p=2*n*r*math.tan(math.pi/n)

# print(p)


# ========================================================================
# 11 h balandlikdan tashlangan tosh yerga qancha vaqtda tushadi

# import math
# h=int(input("Balantlikni kiriting"))

# t=math.sqrt((2*h)/9.81)
# print("H balantlikdan tashlangan toshning erkin tushish vaqti:",t)


# ========================================================================
# 14 Teng tomonli uchburchakning tomoni berilgan bo‘lsin. Uning yuzi va
# perimetrini toping.
# import math
# a=float(input("Uchburchak tomini="))

# p=3*a
# s=(a**2*math.sqrt(3)/4)

# print(f"Uchburchakning peremetri: {p:.2f}",f"Uchburchakning yuzasi: {s:.2f}")

# ========================================================================
# 15 Uzunligi l bo‘lgan mayatnikning tebranish davrini aniqlang.
# import math
# l=int(input("Uzunligini kiriting:"))

# t=2*math.pi*math.sqrt(l/9.81)

# print(t)

# ========================================================================
# 16. Og‘irliklari m1 va m2, orasidagi masofa r bo‘lgan ikki jism bir-birini
# qanday kuch bilan tortadi?

# m1=int(input("Birinchi jism massasi (kg):"))
# m2=int(input("Ikkinchi jism massasi (kg):"))
# r=int(input("Ular ortasidagi masofa (m):"))

# g=6.67e-11

# f=g*(m1*m2)/(r**2)

# print({f:.6})

# ========================================================================
# 17 To‘g‘ri burchakli uchburchakning gipotenuzasi hamda bitta kateti  berilgan bo‘lsin. Uning yuzi va ichki chizilgan aylanasining radiusini toping.
# import math

# c = float(input("Gipotenuzani kiriting (c): "))
# a = float(input("Bir katetni kiriting (a): "))
# b = math.sqrt(c**2 - a**2)       
# S = 0.5 * a * b                 
# r = (a + b - c) / 2              
# print(f"Ikkinchi katet: {b:.2f}")
# print(f"Uchburchakning yuzi: {S:.2f}")
# print(f"Ichki chizilgan aylananing radiusi: {r:.2f}")
