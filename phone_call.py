class Phone:
    
    def __init__(self, number, model= None, weight= None):

        self.number = number
        self.model = model
        self.weight = weight
        
    def __str__(self):
        return f'Телефон {self.model} (номер: {self.number}), вес: {self.weight} грамм.'
    
    def receive_call(self, name):
        print(f"Звонит {name} на {self.number}")
    
    def get_number(self):
        return self.number

phone1 = Phone('+7 967 475 8237', "Samsung", 150) # Создание трёх экземпляров класса Phone
phone2 = Phone('+7 955 234 1122', "iPhone")
phone3 = Phone('7 990 234 5678')

print(phone1) # Вывод информации о каждом телефоне
print(phone2)
print(phone3)

print('Номер телефона 1:', phone1.get_number()) # Вызываем метод get_number() для каждого телефона
print('Номер телефона 2:', phone2.get_number())
print('Номер телефона 3:', phone3.get_number())

phone1.receive_call('Артем') # Вызываем метод receive_call() для каждого телефона
phone2.receive_call('Даша')
phone3.receive_call('Служба доставки')