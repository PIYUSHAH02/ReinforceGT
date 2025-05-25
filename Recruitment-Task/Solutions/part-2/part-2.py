count = {i: 1 for i in range(1,221)}

infile = open('input.txt').read().strip()
lines = infile.split('\n')
card_number = 0

count

for line in lines:
	card_number+=1
	print("Card number: ", card_number, end = " ")
	temp1=line[10:39]
	temp2=line[42:]
	start = [int(x) for x in temp1.split()]
	end = [int(x) for x in temp2.split()]

	matches = 0
	for i in start:
		for j in end:
			curr = int(i)
			check = int(j)

			if curr == check:
				matches += 1

	count_current = count[card_number]
	print("Count: ", count_current, end = " ")
	print("Matches: ", matches)

	for i in range(card_number+1, card_number+matches+1):
		count[i] += count_current*matches
	
total_cards = 0
print()
for i in range(1, 221):
	total_cards += count[i]

print("Final Answer: ", total_cards)