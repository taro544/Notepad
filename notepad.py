#!/bin/python3 
dosya = input("dosya konumu : ")
with open (dosya,'r') as f :
	lines =f.readlines() 
	listlenght = len(lines)
	x = 0
	y = 0 
	print("lenght of list = " + str(listlenght))
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