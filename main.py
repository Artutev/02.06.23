#1
def authenticate(login, password):
    correct_login = "user"
    correct_password = "qwerty"

    if login == correct_login and password == correct_password:
        return "Authentication completed"
    else:
        return "Invalid login or password"

input_login = input("Введите логин: ")
input_password = input("Введите пароль: ")

result = authenticate(input_login, input_password)

print(result)

#2
def exchange_currency(amount, target_currency):
    usd_rate = 420
    eur_rate = 510
    rub_rate = 5.8

    if target_currency == "USD":
        converted_amount = amount / usd_rate
        return f"{amount} KZT равны {converted_amount:.2f} USD"
    elif target_currency == "EUR":
        converted_amount = amount / eur_rate
        return f"{amount} KZT равны {converted_amount:.2f} EUR"
    elif target_currency == "RUB":
        converted_amount = amount / rub_rate
        return f"{amount} KZT равны {converted_amount:.2f} RUB"
    else:
        return "Неверно выбрана целевая валюта"

input_amount = float(input("Введите сумму в тенге: "))
target_currency = input("Выберите валюту для обмена (USD, EUR, RUB): ")

result = exchange_currency(input_amount, target_currency)
print(result)
