mao_obra = 150.0
print("Mao de obra: " + mao_obra)
#TypeError                                 Traceback (most recent call last)
#/tmp/ipykernel_2340/646303204.py in <cell line: 0>()
#      1 mao_obra = 150.0
#----> 2 print("Mao de obra: " + mao_obra)

#TypeError: can only concatenate str (not "float") to str

mao_obra = 150.0
print(f"Mao de obra: R$ {mao_obra:.2f}")