import random


def get_numbers_ticket(min_value, max_value, quantity):
    
    if not  ( 1<= min_value <= max_value <= 1000): # Список унікальних випадкових чисел у межах від minimum до maximum.

        raise ValueError("Please enter values between 1 and 1000")  # Неправильно задані межі чисел
    
    if not isinstance(quantity, int):

        raise TypeError("Please enter a whole number for quantity") # Кількість чисел повинна бути цілим числом
    
    if quantity > max_value - min_value + 1:

        raise ValueError("The quantity of numbers requested exceeds the available range!!!") # Кількість чисел перевищує доступний діапазон
        
    return sorted(random.sample(range(min_value, max_value + 1), quantity))
    
min_num = 1     # задаємо параметри для квитка : 6 цифр від 1 до 49
max_num = 49
quantity = 6                                                            

lottery_numbers = get_numbers_ticket(min_num, max_num, quantity)

print("The winning ticket numbers are:", lottery_numbers)