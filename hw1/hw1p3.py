from func import f 
import sys

a = sys.argv[1]
b = sys.argv[2]

# Prerequisite check
try:
  float(a)
  float(b)
except:
  sys.stderr.write("Range error\n")
  # print('Range error', file=sys.stderr)
  sys.exit()
else:
  a = float(a)
  b = float(b)

if a >= b:
  sys.stderr.write("Range error\n")
  # print('Range error', file=sys.stderr)
  sys.exit()
if f(a)*f(b) >= 0:
  sys.stderr.write("Range error\n")
  # print('Range error', file=sys.stderr)
  sys.exit()
  
#Secant inplementation
CONV_CRIT = 1e-10

x0 = a
x1 = b
N = 0
while True:
  x2 = x1 - f(x1)*(x1-x0)/(f(x1) - f(x0))
  N += 1
  if(abs(x2 - x1) < CONV_CRIT):
    print(str(N), file=sys.stdout)
    print(str(x0), file=sys.stdout)
    print(str(x1), file=sys.stdout)
    print(str(x2), file=sys.stdout)
    sys.exit()
  x0 = x1
  x1 = x2



