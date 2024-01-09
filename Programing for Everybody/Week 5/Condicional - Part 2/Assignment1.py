hours = float(input('Hours: '))
tax = float(input('Tax: '))
total = 0

if(hours > 40): 
  total = 40 * tax
  hours -= 40
  total += hours * (tax * 1.5)
else:
  total = hours * tax

print(total)