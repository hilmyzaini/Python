#Modules

#print(help('modules'))
#print(help('math'))
#import math
#print(math.pi)
#import math as m
#print(m.pi)
from math import pi
print(pi)

print('-------------------------------')

#Exception & Error handling: kudune gwo try, except
try:
  a=10
  b=0
  c=a/b
except ZeroDivisionError:
  print('Ora iso dibagi 0')
else:
  print(c)
finally:
  print('End')