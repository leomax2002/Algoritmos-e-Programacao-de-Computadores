i = 1
j = 7
cont = 0
while True:
  cont+=1
  if i > 9:
    break
  print(f"I={i} J={j}")
  if cont == 1:
    j = 6
  if cont == 2:
    j = 5
  if cont == 3:
    j = 7
    i+=2 
    cont = 0