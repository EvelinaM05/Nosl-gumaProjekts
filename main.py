import json
import os
import datatime
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
    with open(DATA_FILE, "w", encoding"utf-8") as f:
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
        "date": datatime.datatime.now().strftime("%Y-%m-%d")
    }
    if product not in data:
        data[product] = []
    data[product].append(entry)
    save data(data)
    print("Produkta cena veiksmīgi pievienota!").

#Produktu izvade tabulas formātā
def view_all(data)

#Produkta cenu limita uzstādīšana, un cenas paaugstināšanās brīdinājums
def price_alert(data) 

#Eksportē datus uz Excel
def export_to_excel(data)

#Importē datus no Excel
def import_from_excel(data)

#Produktu statistikas
def statistic_data(data)

#Cenu tabula
def price_chart(data)


#Izdzēst produktu
def delete_product(data):
    product = input("Ievadiet produkta nosaukumu, lai to izdzēstu: ")
    if product in data:
        confirm = input(f"Vai tiešām vēlaties dzēst produktu '{product.title()}'") no uzskaites sistēmas? (jā/nē):.strip().lower()
        if confirm == "jā":
            del data[product]
            ssaving_data(data)
            print(f"Produkts '{product.title()}' tika izdzēsts.")
            else:
                print("Darbība tika atcelta. ")
        else:
            print("Produkts netika atrasts datu bāzē.")


#Atgādinājums par produktu reģistrēšanu sistēmā
##### uzrakstīt kodu

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
               price_alert(data) 
            elif choice == "4":
               export_to_excel(data)
            elif choice == "5":
               impport_from_excel(data)
            elif choice == "6":
                statistic_data(data)
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