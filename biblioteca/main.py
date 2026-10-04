import os
from teclas import get_key

def draw_screen(matricula, selected):
    os.system("cls" if os.name == "nt" else "clear")
    print("+" + "-"*30 + "+")
    print("|{:^30}|".format("MATRÍCULA:"))
    print("|{:^30}|".format(matricula.ljust(7, "_")))
    print("|{:^30}|".format(""))
    entrar = "[ ENTRAR ]"
    if selected == "entrar":
        entrar = ">> ENTRAR <<"
    print("|{:^30}|".format(entrar))
    print("+" + "-"*30 + "+")

def main():
    matricula = ""
    selected = "matricula"

    while True:
        draw_screen(matricula, selected)
        key = get_key()

        if os.name == "nt":
            # Navegação com setas
            if key in [b'H', b'P', b'K', b'M']:
                selected = "entrar" if selected=="matricula" else "matricula"
            elif selected == "matricula":
                if key.isdigit() and len(matricula) < 7:
                    matricula += key.decode()
                elif key in [b'\x08']:  # backspace
                    matricula = matricula[:-1]
            elif selected == "entrar" and key in [b'\r']:
                if len(matricula)==7 and matricula.isdigit():
                    print("Matrícula aceita:", matricula)
                else:
                    print("Erro: digite 7 números")
                break
            elif key == b'q':
                break

        else:  # Linux/Mac
            if key in [b'\x1b[A', b'\x1b[B', b'\x1b[C', b'\x1b[D']:
                selected = "entrar" if selected=="matricula" else "matricula"
            elif selected == "matricula":
                if key.decode().isdigit() and len(matricula) < 7:
                    matricula += key.decode()
                elif key in [b'\x7f']:  # backspace
                    matricula = matricula[:-1]
            elif selected == "entrar" and key in [b'\n', b'\r']:
                if len(matricula)==7 and matricula.isdigit():
                    print("Matrícula aceita:", matricula)
                else:
                    print("Erro: digite 7 números")
                break
            elif key == b'q':
                break

if __name__ == "__main__":
    main()
