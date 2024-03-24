def solution(n,choco):
  decision = 0
  for i in range(n):
    if choco[i] % 2 != 0:
      decision = 1
  if decision == 1:
      return "Ooty"
  else:
      return "Kodaikkanal"
