import subprocess
import os

# C-koodin tiedostonimi
source_file = "main.c"
# Käännetyn ohjelman nimi
executable_file = "ohjelma.exe"
# Testitulosten tallennustiedosto
output_file = "testit.txt"

# Testitapaukset: syötteet ja kuvaus
test_cases = [
    ("12345\n1122\n4\n", "Testitapaus 1: Toimintovalikko avautuu, saldo näkyy"),
    ("12345\n0000\n", "Testitapaus 2: Virheellinen PIN-koodi"),
    ("54321\n", "Testitapaus 3: Tilitiedostoa ei löydy"),
    ("12345\n1122\n2\n50\n4\n", "Testitapaus 4: Nostetaan 50 euroa, saldo vähenee"),
    ("12345\n1122\n2\n15\n4\n", "Testitapaus 5: Nostetaan virheellinen summa (15 euroa)"),
    ("12345\n1122\n2\n5000\n4\n", "Testitapaus 6: Nostetaan liian suuri summa (5000 euroa)"),
    ("12345\n1122\n3\n200\n4\n", "Testitapaus 7: Talletetaan 200 euroa"),
    ("12345\n1122\n4\n", "Testitapaus 8: Lopetus, saldo tallentuu"),
    ("12345\nABC\n", "Testitapaus 9: Virheellinen PIN-koodi (kirjaimia syötetty)"),
    ("12345\n1122\n2\nABC\n4\n", "Testitapaus 10: Nostetaan kirjaimia syötteeksi"),
    ("\n1122\n", "Testitapaus 11: Tyhjä tilinumero"),
    ("12345\n\n", "Testitapaus 12: Tyhjä PIN-koodi"),
    ("abcde\nxyz\n", "Testitapaus 13: Virheellinen tilinumero ja PIN-koodi"),
    ("12345\n1122\n2\nabc\n4\n", "Testitapaus 14: Nostetaan virheellinen syöte (kirjaimia)"),
    ("12345\n1122\n3\n-200\n4\n", "Testitapaus 15: Negatiivinen talletus ei ole sallittu"),
]

# Poista vanha tulostiedosto, jos sellainen on
if os.path.exists(output_file):
    os.remove(output_file)

# 1. Käännä C-koodi ja kirjoita käännöksen tulos tiedostoon
try:
    # Käännä C-koodi
    subprocess.run(["gcc", source_file, "-o", executable_file], check=True)
    # Avaa tiedosto ja kirjoita käännöksen tulos
    with open(output_file, "w") as f:
        f.write("Automatisoidut testit:\n\n")
        f.write(f"Käännetään {source_file}...\n")
        f.write("Kääntäminen onnistui.\n\n")
except subprocess.CalledProcessError:
    # Kirjoita käännöksen virhe tiedostoon ja keskeytä testit
    with open(output_file, "w") as f:
        f.write("Kääntäminen epäonnistui. Testit keskeytetään.\n")
    print("Kääntäminen epäonnistui. Tarkista C-koodisi.")
    exit(1)

# 2. Suorita testit ja kirjoita niiden tulokset tiedostoon
with open(output_file, "a") as f:
    for input_data, description in test_cases:
        f.write(f"{description}\n")
        try:
            # Suorita ohjelma ja anna sille syötteet
            result = subprocess.run(
                [f"./{executable_file}"],  # Suoritettavan ohjelman nimi
                input=input_data,          # Syötteet ohjelmalle
                text=True,                 # Käytä tekstitilaa
                capture_output=True        # Tallenna ohjelman tulosteet
            )
            # Kirjoita ohjelman tuloste tiedostoon
            f.write(result.stdout)
        except FileNotFoundError:
            f.write(f"{executable_file} ei löytynyt. Testi keskeytyi.\n")

        f.write("\n---\n")

print("Testit suoritettu. Tulokset löytyvät tiedostosta testit.txt.")
