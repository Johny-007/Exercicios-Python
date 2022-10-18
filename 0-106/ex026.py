frase = str(input("\n   -digite uma frase motivacional:\n   - ")).lower().strip()
print (f"""   - a lera 'A' aparece {frase.count("a")} vezes na frase
   - a posicao da primeira letra 'A' foi {frase.find("a")+1}
   - a posicao da ultima letra 'A' foi {frase.rfind("a")+1}""")
