L = """ Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those! """

gmail = 'ilya.trusovv@gmail.com'
L += gmail

#len

lensym = len(L)
print(lensym)


#voules
counter = 0
for i in range(lensym):
	if L[i] in 'aweyuio':
		counter += 1

print(counter)


#each 18th symbol of the string
count = 0
for i in range(lensym):
	if i % 18 == 0:
		count += 18
		if L[i] == L[i].lower():
			print(count, L[i].upper(), sep = '')
		elif L[i] == L[i].upper():
			print(count, L[i].lower(), sep = '')
		else:
			continue
