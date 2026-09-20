import re

padrao_email = r"^[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"


def explicar_motivo(email):
    """Retorna o motivo da rejeição de um e-mail inválido."""
    if "@" not in email:
        return "não possui o símbolo @"
    usuario, _, resto = email.partition("@")
    if not usuario:
        return "não possui usuário"
    if not resto:
        return "não possui domínio"
    if "." not in resto:
        return "não possui extensão (faltou o ponto)"
    dominio, _, extensao = resto.rpartition(".")
    if not dominio:
        return "não possui domínio"
    if len(extensao) < 2 or not extensao.isalpha():
        return "a extensão precisa ter pelo menos duas letras"
    if " " in email:
        return "contém espaço em branco"
    return "não segue o formato esperado de e-mail"


def main():
    validos = []
    invalidos = []

    print("Digite 5 endereços de e-mail para validar:\n")
    for i in range(1, 6):
        email = input(f"E-mail {i}: ").strip()
        if re.fullmatch(padrao_email, email):
            validos.append(email)
        else:
            invalidos.append((email, explicar_motivo(email)))

    print("\n--- Resultado ---")

    print(f"\nE-mails válidos ({len(validos)}):")
    if validos:
        for email in validos:
            print(f"  - {email}")
    else:
        print("  Nenhum")

    print(f"\nE-mails inválidos ({len(invalidos)}):")
    if invalidos:
        for email, motivo in invalidos:
            print(f"  - {email}  →  {motivo}")
    else:
        print("  Nenhum")


if __name__ == "__main__":
    main()