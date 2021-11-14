#!/bin/python3
print("Lutfen txt dosyasinin tam konumunu yazin")
dosya = input("dosya konumu : ")
with open (dosya,'r') as f :
	lines =f.readlines()
	listlenght = len(lines)
	x = 0 #Toplam liste sayisi icin
	y = 0 #Bos olmayan satirlar icin 
	print("")
	while listlenght:
		if x == listlenght:
			break
		elif len(lines[x]) == 1:
			x += 1
			pass
		else:
			print(str(y+1) + ".",lines[x])
			x += 1
			y += 1
	print("Toplam satir sayisi = " + str(y))
