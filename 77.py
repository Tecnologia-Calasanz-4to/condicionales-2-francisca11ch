Año=int(input("Decime un año"))
división=Año%4
if (Año%4==0 and Año%100!=0)or(Año%400==0):
  print("BISIESTO")
else :
  print("NO BISIESTO")
