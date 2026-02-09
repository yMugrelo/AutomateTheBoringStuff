'''Function: isValidCPF(cpf)

Purpose:
    Validate whether a given CPF number is mathematically valid'''

def isAvaliableId(text):
    #input cleaning
    text = ''.join(filter(str.isdigit, text))
    if len(text) != 11 or text == text[0] * 11:
        return False 

    # Helper function to calculate a verification digit
    def calc(digs, pesos):
        s = sum(int(d) * p for d, p in zip(digs, pesos))
        r = (s * 10) % 11
        return 0 if r == 10 else r
    
    d1 = calc(text[:9], range(10, 1, -1))
    d2 = calc(text[:10], range(11, 1, -1))

    return text[-2:] == f"{d1}{d2}"
   

print(isAvaliableId("529.982.247-25"))
