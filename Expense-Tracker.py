def main():
    expenses = []
    while True:
        print("\n1 - Добавить Расход")
        print("2 - Показать Расходы")
        print("3 - Показать Общую Сумму")
        print("0 - Выход")
        choice = input()

        if choice == "1":
            a,b = map(str,input("Имя и количество:\n").split())
            b = int(b)
            add_expense(expenses,a,b)
        elif choice == "2":
            show_expenses(expenses)
            pass
        elif choice == "3":
            show_total(expenses)
        elif choice == "0":
            break
        else:
            print("Нет такого пункта. Попробуйте еще раз")

def add_expense(expenses,name,amount):
    expenses.append({"name": name, "amount": amount})

def show_expenses(expenses):
    if not expenses:
        print("Расходов нет")
    else:
        for i in expenses:
            print(f"{i["name"]} - {i["amount"]}.")
            
def show_total(expenses) -> int:
    a = 0
    if expenses:
        for i in expenses:
            a += i["amount"]
        print(f"Всего потрачено: {a}")
    else:
        print(f"Рассходы отсуствуют")
main()