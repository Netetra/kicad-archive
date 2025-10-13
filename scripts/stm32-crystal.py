import math

# G_MIN = 5 # STM32F4
G_MIN = 10 # STM32F3

def calc_cl12(cl, cs):
    return 2 * (cl - cs)

# ESR[Ohm] Freq[Hz] C0[F] CL[F]
def calc_margin(esr, freq, c0, cl):
  g_mcrit = 4 * esr * (2 * math.pi * freq) ** 2 * (c0 + cl) ** 2
  return G_MIN / (g_mcrit * 1000)

def main():
  esr = int(input("ESR[Ω] > "))
  freq = int(input("Freq[MHz] > ")) * 10 ** 6
  c0 = int(input("C0[pF] > ")) * 10 ** -12
  cl = int(input("CL[pF] > ")) * 10 ** -12
  cs = 5 * 10 ** -12
  
  cl12 = calc_cl12(cl, cs) * 10 ** 12
  g_margin = calc_margin(esr, freq, c0, cl)
  print(f"CL1 = CL2 = {cl12}pF")
  print(f"gain margin: {g_margin}")

  if 5 <= cl12 and cl12 <= 25:
    print("定格内, ", end="")
  else:
    print("定格外, ", end="")

  if g_margin >= 5:
    print("発振: 可")
  else:
    print("発振: 不可")
  return

main()
