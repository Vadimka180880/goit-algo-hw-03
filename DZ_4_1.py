from datetime import datetime

def get_days_from_today(date):

     try:
        date_object = datetime.strptime(date, '%Y-%m-%d')

        current_date = datetime.today()       # Отримуємо поточну дату та час

        delta = current_date - date_object    # Розраховуємо різницю між поточною датою та заданою датою                                                

        return delta.days                     # Повертаємо кількість днів (від'ємну, якщо задана дата пізніша за поточну)
     
     except ValueError:                       # Обробка помилки, якщо рядок дати має неправильний формат
         print("ERROR: no accepted formats date.\n Please enter date formats YYYY-MM_DD")
         return None

date_str = "2022-02-22"                       # Як приклад введемо дату коли москаль вторгся без запрошення в Україну

date_difference = get_days_from_today(date_str)
if date_difference is not None:

    print("Different days from", date_str, "and date today>>>", date_difference) 

