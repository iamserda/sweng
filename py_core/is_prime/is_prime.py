def is_prime(n):
  '''
  if n is a prime number, return True
  if n isn't a prime number, return False
  '''
  for i in range(2, n//2+1):
    if n % i == 0:
      return False
  return True

for i in range(2, 10):
    print(i,"is a `Prime` number:", "yes" if is_prime(i) else "no")
    
