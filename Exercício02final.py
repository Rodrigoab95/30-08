def criar_curriculo():
    nome = input("Digite o seu nome: ")
    endereco = input("Digite o seu endereço: ")
    telefone = input("Digite o seu telefone: ")
    email = input("Digite o seu e-mail: ")
    escolaridade = input("Digite a sua escolaridade: ")
    experiencia_profissional = input("Digite a sua experiência profissional: ")

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Currículo</title>
    </head>
    <body>
        <h1>{nome}</h1>
        <p><strong>Endereço:</strong> {endereco}</p>
        <p><strong>Telefone:</strong> {telefone}</p>
        <p><strong>E-mail:</strong> {email}</p>
        <h2>Escolaridade</h2>
        <p>{escolaridade}</p>
        <h2>Experiência Profissional</h2>
        <p>{experiencia_profissional}</p>
    </body>
    </html>
    """

    with open("curriculo.html", "w") as file:
        file.write(html)

if __name__ == "__main__":
    criar_curriculo()
