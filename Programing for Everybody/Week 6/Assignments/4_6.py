def computepay(hours, tax):
    if(hours > 40): 
      total = 40 * tax
      hours -= 40
      total += hours * (tax * 1.5)
    else:
      total = hours * tax
    return total

hrs = float(input("Enter Hours:"))
tax = float(input('Tax: '))
p = computepay(hrs, tax)
print("Pay", p)