answer = 0
infile = open('input.txt').read().strip()
lines = infile.split('\n')
card_number = 0
for line in lines:
	card_number+=1
	temp1=line[10:39]
	temp2=line[42:]
	start = [int(x) for x in temp1.split()]
	end = [int(x) for x in temp2.split()]
	
	match_list = []
	for i in start:
		for j in end:
			curr = int(i)
			check = int(j)

			if curr == check: 
				match_list.append(curr)
	if(len(match_list) > 0):
		print(len(match_list), " MATCHING NUMBER(s): ", end = "")
		for c in match_list:
			print(c, end = " ")
		print("CARD_NUMBER: ", card_number, end = " ")
		print("POINTS: ", (2**(len(match_list)-1)),end = " ")
		to_add = card_number*(2**(len(match_list)-1))
		print("TOTAL POINTS: ", to_add)
		answer += to_add

print()
print("FINAL ANSWER: ", end = "")
print(answer)
