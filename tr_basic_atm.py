a = 0

while True:	

	b = int(input(("Lütfen bir işlem seçiniz\n\n1-Bakiye sorgulama\n2-Para yatırma\n3-Para çekme\n4-Çıkış\n")))

	if b == 1:
		print(f"Anlık bakiyeniz: {a}")

	elif b == 2:
		c = int(input("Yatırmak istediğiniz para miktarını giriniz: "))
		a = a+c 
		print(f"Anlık bakiyeniz: {a}")

	elif b == 3:
		d = int(input("Çekmek istediğiniz para miktarını giriniz: "))

		if d<=a:
			a = a-d
			print(f"Anlık bakiyeniz: {a}")
		else:
			print("Hesabınızda yeterli miktarda para yok.")

	elif b == 4:
		print("Görüşürüz...")
		break
		
