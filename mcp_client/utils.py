def select_language() -> str:
    print("\n🌐 Selecione seu idioma / Select your language:")
    print("1 - Português (Brasil)")
    print("2 - English")

    while True:
        option = input("👤 Digite o número da opção / Enter option number: ").strip()
        if option == "1":
            print("\nIdioma selecionado: Português do Brasil")
            return "Portuguese (Brazil)"
        elif option == "2":
            print("\nSelected language: English")
            return "English"
        else:
            print("Opção inválida / Invalid option\n")