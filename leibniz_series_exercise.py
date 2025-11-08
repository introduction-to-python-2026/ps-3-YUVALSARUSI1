def approximate_pi(n_terms):
  result2 = 0
  for n in range(n_terms):
   result1 = ((-1)**n)/(2*n+1)
   result2 += result1

  return 4*result2
