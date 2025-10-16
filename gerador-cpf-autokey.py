import random
import time

PASTE_FIRST = True          # True: tenta colar primeiro; False: digita direto
TYPE_DELAY = 0.02           # atraso entre teclas (segundos)

def gen_cpf():
    digits = [random.randint(0, 9) for _ in range(9)]
    sum1 = sum((10 - i) * digits[i] for i in range(9))
    rem1 = (sum1 * 10) % 11
    c1 = 0 if rem1 >= 10 else rem1

    sum2 = sum((11 - i) * digits[i] for i in range(9)) + c1 * 2
    rem2 = (sum2 * 10) % 11
    c2 = 0 if rem2 >= 10 else rem2

    cpf = "".join(str(d) for d in digits) + str(c1) + str(c2)
    return cpf

def paste_via_clipboard(text):
    try:
        # AutoKey v2: usa set_clipboard / set_primary
        clipboard.set_clipboard(text)
        time.sleep(0.05)
        keyboard.send_keys("<ctrl>v>")
        return True
    except Exception:
        pass
    # alternativa clássica do X11
    try:
        clipboard.set_primary(text)
        time.sleep(0.05)
        keyboard.send_keys("<shift><insert>")
        return True
    except Exception:
        return False

def type_slowly(text):
    for ch in text:
        keyboard.send_keys(ch)
        time.sleep(TYPE_DELAY)

cpf = gen_cpf()

if PASTE_FIRST:
    ok = paste_via_clipboard(cpf)
    if not ok:
        type_slowly(cpf)
else:
    type_slowly(cpf)
