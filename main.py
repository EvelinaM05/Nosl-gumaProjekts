


def add_prod(data)
def view_all(data)
def price_alert(data) 
def export_to_excel(data)
def import_from_excel(data)
def statistic_data(data)
def price_chart(data)
def delete_product(data)


#Main loop
def main_menu():
    data = load_data()
    reminder()

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