from datetime import datetime

def get_upcoming_birthdays(users):
    
    current_date = datetime.today().date()

    upcoming_birthdays = []

    for user in users:
        
        birthday_components = user["birthday"].split(".") # Розбиваємо рядок з датою народження на компоненти року, місяця і дня
        birthday_components = user["birthday"].split(".")
        birthday_year = int(birthday_components[0])
        birthday_month = int(birthday_components[1])
        birthday_day = int(birthday_components[2])

        user_birthday = datetime(current_date.year, birthday_month, birthday_day).date() # Створюємо об'єкт datetime для дня народження цього користувача у поточному році
        
        if user_birthday < current_date: 
            user_birthday = datetime(current_date.year + 1, birthday_month, birthday_day).date() # Перевіряємо, чи день народження користувача вже пройшов у цьому році, якщо так, то додаємо його до списку
        
        days_until_birthday = (user_birthday - current_date).days # Обчислюємо різницю між поточною датою і днем народження користувача

        if 0 <= days_until_birthday <= 7:  # Якщо різниця менша або дорівнює 7, то додаємо користувача до списку наближених днів народження
            upcoming_birthdays.append({"name": user["name"], "days_until_birthday": days_until_birthday})
    
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.04.23"},
    {"name": "Jane Smith", "birthday": "1990.04.27"},
    {"name": "Oksana Kvitka", "birthday": "1989.05.05"},
    {"name": "Yuliya Glushka", "birthday": "1988.03.23"},
    
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
