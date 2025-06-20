import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        """Геттер для получения списка названий товаров."""
        return self.__name_items

    @property
    def number_items(self):
        """Геттер для получения количества товаров."""
        return self.__number_items

    def add_item_to_cheque(self, name):
        """Добавляет товар в чек с проверками."""
        if not isinstance(name, str) or len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        
        self.__name_items.append(name)
        self.__number_items += 1

    def delete_item_from_check(self, name):
        """Удаляет товар из чека."""
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        
        self.__name_items.remove(name)
        self.__number_items -= 1

    def check_amount(self):
        """Считает общую сумму покупки со скидкой, если применимо."""
        total = sum(self.__item_price[item] for item in self.__name_items)
        if self.number_items > 10:
            total *= 0.9
        return total

    def twenty_percent_tax_calculation(self):
        """Рассчитывает НДС 20% с учётом скидки."""
        items_with_20_tax = [item for item in self.__name_items if self.__tax_rate.get(item) == 20]
        total_for_tax = sum(self.__item_price[item] for item in items_with_20_tax)
        
        if self.number_items > 10:
            total_for_tax *= 0.9
            
        return total_for_tax * 0.2

    def ten_percent_tax_calculation(self):
        """Рассчитывает НДС 10% с учётом скидки."""
        items_with_10_tax = [item for item in self.__name_items if self.__tax_rate.get(item) == 10]
        total_for_tax = sum(self.__item_price[item] for item in items_with_10_tax)

        if self.number_items > 10:
            total_for_tax *= 0.9

        return total_for_tax * 0.1

    def total_tax(self):
        """Возвращает общую сумму НДС по чеку."""
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

    @staticmethod
    def get_telephone_number(telephone_number):
        """Проверяет и возвращает номер телефона покупателя."""
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        if len(str(telephone_number)) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{telephone_number}'

    @staticmethod
    def get_date_and_time():
        """Возвращает текущую дату и время в заданном формате."""
        date_and_time = []
        now = datetime.datetime.now()
        date = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year]
        ]
        for item in date:
            date_and_time.append(f'{item[0]}: {item[1](now)}')
        return date_and_time
