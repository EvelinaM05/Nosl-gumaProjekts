import json
import os
import datetime
import time
import schedule
import pandas as pandas
import matplotlib.pyplot as plt
from tabulate import tabulate

DATA_FILE = "products_data.json"

#Lādējam datus no JSON faila
def load_data():
    if not os.path.exists(DATA_FILE):
        return{}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

#Saglabājam produkta datus json failā
def saving_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

#Pievienojam jaunu produktu
def add_prod(data):
    product = input("Produkta nosaukums: ").strip().lower()
    try:
        price = float(input("Cena (€): ").strip())
    except ValueError:
        print("Nepareiza cenas ievade(ievadiet kā 0.00)")
        return
    
    entry = {
        "price": price,
        "date": datetime.datatime.now().strftime("%Y-%m-%d")
    }
    if product not in data:
        data[product] = []
    data[product].append(entry)
    saving_data(data)
    print("Produkta cena veiksmīgi pievienota!")

#Produktu izvade tabulas formātā
def view_all(data):
    if not data:
        print("Dati netika atrasti.")
        return

    table = []
    
    for product, entries in data.items():
        latest = max(entries, key=lambda x: x["date"])
        table.append([product.title(), latest["price"], latest["date"]])
    print(tabulate(table, headers=["Produkts", "Cena(€), Datums"], tablefmt="grid"))


#Izdzēst produktu
def delete_product(data):
    product = input("Ievadiet produkta nosaukumu, lai to izdzēstu: ")
    if product in data:
        confirm = input(f"Vai tiešām vēlaties dzēst produktu '{product.title()})' no uzskaites sistēmas? (jā/nē): ").strip().lower()
        if confirm == "jā":
            del data[product]
            saving_data(data)
            print(f"Produkts '{product.title()}' tika izdzēsts.")
        else:
            print("Darbība tika atcelta. ")
    else:
        print("Produkts netika atrasts datu bāzē.")


#Atgādinājums par produktu reģistrēšanu sistēmā
def set_reminder():
    def reminder():
        print("Atgādinājums - Pievienojiet produktu cenas ")
    set.every().day.at("18:30").do(reminder)

#Produkta cenu limita uzstādīšana, un cenas paaugstināšanās brīdinājums
def set_alert(data):
    product = input("Produkta nosaukums: ").strip().lower()
    try:
        limit = float(input("Cenu limits (€): "))
    except ValueError:
        print("Nepareiza cena!")
        return

    if product in data and data[product]:
        latest_price = data[product][-1]["price"]
        if latest_price > limit:
            print(f"{product.title()} cena ({latest_price}€) pārsniedz {limit}€")
        else:
            print(f"{product.title()} cena ({latest_price}€) ir zem {limit}€")
    else:
        print("Produkts nav atrasts vai tam nav cenu ierakstu!")

#Eksportē datus uz Excel
def export_to_excel(data):
    entries = []
    for product, product_data in data.items():
        for record in product_data:
            entries.append({
                "Produkts": product.title(),
                "Cena (€)": record["price"],
                "Datums": record["date"]
            })

    if entries:
        df = pd.DataFrame(entries)
        df.to_excel("products.xlsx", index=False)
        print("Dati eksportēti uz 'products.xlsx'.")
    else:
        print("Nav datu, ko eksportēt.")

#Importē datus no Excel
def import_from_excel(data):
    try:
        df = pd.read_excel("products.xlsx")
        for _, row in df.iterrows():
            product = str(row["Produkts"]).strip().lower()
            price = float(row["Cena (€)"])
            date = str(row["Datums"])[:10]

            entry = {"price": price, "date": date}
            if product not in data:
                data[product] = []
            data[product].append(entry)
        save_data(data)
        print("Dati importēti no 'products.xlsx'.")
    except Exception as e:
        print(f"Importēšanas kļūda: {e}")

#Produktu statistika
def statistics(data):
    product = input("Produkta nosaukums: ").strip().lower()
    if product in data and data[product]:
        prices = [entry["price"] for entry in data[product]]
        print(f"\nStatistika par {product.title()}:")
        print(f"  Minimālā cena: {min(prices)}€")
        print(f"  Maksimālā cena: {max(prices)}€")
        print(f"  Vidējā cena: {sum(prices)/len(prices):.2f}€")
    else:
        print("Produkts nav atrasts vai nav ierakstu!")

#Cenu tabula
def price_chart(data):
    product = input("Produkta nosaukums: ").strip().lower()
    if product in data and data[product]:
        entries = sorted(data[product], key=lambda x: x["date"])
        dates = [e["date"] for e in entries]
        prices = [e["price"] for e in entries]

        plt.plot(dates, prices, marker='o')
        plt.title(f"{product.title()} cenu izmaiņas")
        plt.xlabel("Datums")
        plt.ylabel("Cena (€)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)
        plt.show()
    else:
        print("Produkts nav atrasts vai nav ierakstu!")

#Main loop
def main_menu():
    data = load_data()
    set_reminder()

    while True:
        print("\n---Pārtikas produktu cenu uzskaites sistēma ---")
        print("[1] Pievienot produktu")
        print("[2] Apskatīt visus produktus")
        print("[3] Cenu brīdinājums")
        print("[4] Eksportēt uz Excel")
        print("[5] Importēt no Excel")
        print("[6] Produkta statistika")
        print("[7] Parādīt cenu grafiku")
        print("[8] Iziet")
        print("[9] Dzēst produktu")

        choice = input("Izvēlies darbību(piem. 1): ").strip()
        if choice == "1":
            add_prod(data)
        elif choice == "2":
            view_all(data)
        elif choice == "3":
            set_alert(data)
        elif choice == "4":
            export_to_excel(data)
        elif choice == "5":
            import_from_excel(data)
        elif choice == "6":
            statistics(data)
        elif choice == "7":
            price_chart(data)
        elif choice == "8":
            print("Programma beidzas.")
            break
        elif choice == "9":
            delete_product(data)
        else:
            print("Nepareiza izvēle!")

        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main_menu
