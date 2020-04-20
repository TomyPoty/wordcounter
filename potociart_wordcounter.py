import argparse
import sys

def main():

    parser = argparse.ArgumentParser(description='Wordcounter by Tomáš Potočiar')
    parser.add_argument("nazev", help = "Název souboru pro čtení")
    parser.add_argument("--znaky", help = "Spočítá znaky", action= "store_true")
    parser.add_argument("--slova", help = "Spočítá slova", action= "store_true")
    parser.add_argument("--radky", help = "Spočítá řádky", action= "store_true")

    args = parser.parse_args()

    try:
        file = open(args.nazev)
        text = file.read()
            
        if args.slova and args.znaky and args.radky:
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\n\nPočet znaků: {znaky} | Počet slov: {slova} | Počet řádků: {radky} \n")
            file.close()
        elif args.slova and args.znaky:
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\n\nPočet znaků: {znaky} | Počet slov: {slova}\n")
            file.close()
        elif args.radky and args.slova:
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\n\nPočet slov: {slova} | Počet řádků: {radky} \n")
            file.close()
        elif args.radky and args.znaky:
            znaky = len(text)
            radky = len(text.split("\n"))
            print(f"\n{text}\n\nPočet znaků: {znaky} | Počet řádků: {radky} \n")
            file.close()
        elif args.znaky:
            znaky = len(text)
            print(f"\n{text}\n\nPočet znaků: {znaky}\n")
            file.close()
        elif args.radky:
            radky = len(text.split("\n"))
            print(f"\n{text}\n\nPočet řádků: {radky} \n")
            file.close()
        elif args.slova:
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\n\nPočet slov: {slova} \n")
            file.close()
        else:
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\n\nPočet znaků: {znaky} | Počet slov: {slova} | Počet řádků: {radky} \n")
            file.close()
            
    except PermissionError:
        print("Nemáte oprávnění k přístupu do složky")
        sys.exit()
    except:
        print("Špatný název souboru nebo chybný soubor")
        sys.exit()
if __name__ == "__main__":
    main()





