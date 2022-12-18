print("Список покупок")
lista_zakupow = {
        "Пекарня" : ["хліб", "булочки", "пончик"],
        "Продуктовий" : ["морква", "селера", "рукола"]
}

number_of_goods = 0

for sklep in lista_zakupow:
        print("Заходжу в ", sklep, " купую ", lista_zakupow[sklep])
        number_of_goods = number_of_goods + len(lista_zakupow[sklep])

print("Разом купую ", number_of_goods, " товарів")
