ukoly = []

def hlavni_menu():
    while True:
        print("\n===== SPRÁVCE ÚKOLŮ =====")
        print("1. Přidat úkol")
        print("2. Zobrazit úkoly")
        print("3. Odstranit úkol")
        print("4. Konec")
        volba = input("Zadejte číslo volby: ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Program byl ukončen.")
            break
        else:
            print("Neplatná volba, zkuste to prosím znovu.")

def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        popis = input("Zadejte popis úkolu: ").strip()
        if nazev and popis:
            ukoly.append({"nazev": nazev, "popis": popis})
            print(f"Úkol '{nazev}' byl přidán.")
            break
        else:
            print("Název i popis úkolu nesmí být prázdný, zkuste to prosím znovu.")

def zobrazit_ukoly():
    if not ukoly:
        print("Žádné úkoly nejsou uloženy.")
    else:
        print("\n===== SEZNAM ÚKOLŮ =====")
        for idx, u in enumerate(ukoly, start=1):
            print(f"{idx}. {u['nazev']} - {u['popis']}")

def odstranit_ukol():
    if not ukoly:
        print("Není co odstraňovat, seznam je prázdný.")
        return
    zobrazit_ukoly()
    while True:
        try:
            cislo = int(input("Zadejte číslo úkolu k odstranění: "))
            if 1 <= cislo <= len(ukoly):
                smazany = ukoly.pop(cislo - 1)
                print(f"Úkol '{smazany['nazev']}' byl odstraněn.")
                break
            else:
                print("Tento úkol neexistuje, zkuste to znovu.")
        except ValueError:
            print("Zadejte prosím platné číslo.")

# Spuštění programu
hlavni_menu()