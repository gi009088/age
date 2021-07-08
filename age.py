print('請問您是否曾經駕駛過汽車?(Y/N)')
driving = input()
if driving != 'Y' and driving != 'N':
	print('請請重新執行程式，並入正確文字(含大小寫)')
	raise SystemExit

age =input('請問您的年齡為?')
age = int(age)
if driving == 'Y':
	if age >= 18:
		print('您通過測驗!')
	else:
		print('未成年禁止駕車!')
elif driving == 'N':
	if age >= 18:
		print('請學習考取駕照')
	elif age < 18:
		print('您將可於', 18 - age, '年後，可考取駕照')
	