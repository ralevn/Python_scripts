def is_in_dict(items, item):
	return True if item in items else False

force_book = {}

while True:
	text = input()
	
	if text== 'Lumpawaroo':
		break
	
	side = ''
	user = ''
	
	if " | " in text:
		args = text.split(' | ')
		side = args[0]
		user = args[1]
		
		all_users = [item for current_list in force_book.values() for item in current_list]
	
		if user in all_users:
			continue
	
		if side not in force_book:
			force_book[side] = []
			force_book[side].append(user)
	else:
		args = text.split(' -> ')
		user= args[0]
		side = args[1]
		
		old_side = ''
		for k,v in force_book.items():
			if user in v:
				old_side = k
				break
	
		if old_side != '':
		force_book[old_side].remove(user)
		
		if side not in force_book:
		force_book[side] = []
		force_book[side].append(user)
		print (f'{user} joins the {side} side!')
	
force_book = dict(sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0])))

for k,v in force_book.items():
	if len(v) == 0:
		continue
	
	print(f'Side: {k}, Members: {len(v)}')
	
	for s in sorted(v):
		print(f'! {s}')