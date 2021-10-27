do = str(input("decrypt(de)(де) or encrypt(en)(код): "))

rofl = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
21,22,23,24,25,26,27,28,29,30,31,32]

lang = str(input("en(ан) or ru(ру): "))

en = [' ','a','b','c','d','e','f','g','h','i','j',
'k','l','m','n','o','p','q','r','s','t',
'u','v','w','x','y','z']

ru = [' ','а','б','в','г','д','е','ё','ж','з','и','й','к','л',
'м','н','о','п','р','с','т','у','ф','х','ц',
'ч','ш','щ','ъ','ы','ь','э','ю','я']

key = int(input('key(ключ): '))

if do == 'en' or do == 'код':
	if lang == 'en' or lang == 'ан':
		text = list(input('text: ').lower())
		for i in text:
			if i == ' ':
				c = ' '
				print(c,end='',sep='')
			else:
				g = en.index(i)
				c = en[(g+key)%26]
				if (g+key)%26 == 0:
					print(en[26],end='',sep='')
				else:
					print(c,end='',sep='')
	elif lang == 'ru' or lang == 'ру':
		text = list(input('текст: ').lower())
		for i in text:
			if i == ' ':
				c = ' '
				print(c,end='',sep=' ')
			else:
				g = ru.index(i)
				c = ru[(g+key)%33]
				if (g+key)%33 == 0:
					print(ru[33],end='',sep='')
				else:
					print(c,end='',sep='')
	else:
		print('wrong language(неверный язык)')
elif do == 'de' or do == 'де':
	if lang == 'en' or lang == 'ан':
		text = list(input('chipertext: ').lower())
		for i in text:
			if i == ' ':
				c = ' '
				print(c,end='',sep=' ')
			else:
				g = en.index(i)
				c = en[(g-key)%26]
				if (g-key)%26 == 0:
					print(en[26],end='',sep='')
				else:
					print(c,end='',sep='')
	elif lang == 'ru' or lang == 'ру':
		text = list(input('шифро-текст: ').lower())
		for i in text:
			if i == ' ':
				c = ' '
				print(c,end='',sep=' ')
			else:
				g = ru.index(i)
				c = ru[(g-key)%33]
				if (g-key)%33 == 0:
					print(ru[33],end='',sep='')
				else:
					print(c,end='',sep='')
	else:
		print('wrong language(неверный язык)')
elif do == '3':
	text = list(input('шифро-текст: ').lower())
	for y in rofl:
		for i in text:
			if i == ' ':
				c = ' '
				print(c,end='',sep=' ')
			else:
				g = ru.index(i)
				c = ru[(g-y)%33]
				if (g-y)%33 == 0:
					print(ru[33],end='',sep='')
				else:
					print(c,end='',sep='')
else:
	print('wrong operation(неверная операция)')
	
#Для покупки ПО свяжитесь с автором по почте.
