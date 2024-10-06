# import csv
#
#
# class UserLog:
#     def __init__(self, first_name: str, last_name: str, age: int, email: str, money: int, password: str):
#         self.email = email
#         self.age = age
#         self.last_name = last_name
#         self.first_name = first_name
#         self._money = int(money)
#         self._password = password
#
#     @property
#     def money(self):
#         return self._money
#
#     @money.setter
#     def money(self, value):
#         new_money = self._money + value
#         self._money = new_money
#
#     def to_dict(self):
#         log_info = {
#             'id': UserLog.get_next_id(log_in_path),
#             'first_name': self.first_name,
#             'last_name': self.last_name,
#             'age': self.age,
#             'email': self.email,
#             'money': self._money,
#             'password': self._password
#         }
#         return log_info
#
#     @classmethod
#     def get_next_id(cls, path_to_db):
#         next_id = 1
#         with open(path_to_db, 'r') as csv_db:
#             reader = csv.DictReader(csv_db)
#             for _ in reader:
#                 next_id += 1
#
#         return next_id
#
#
# user = UserLog('test', 'test', 21, 'test@t.com', 1000, 123)
# print(user.money)
# print(user.age)
# print(user.id)

import pendulum

# date = pendulum.now('Europe/Sofia')
# date2 = pendulum.now('Europe/Sofia')
# dt = pendulum.parse(str(date))
# dt2 = pendulum.parse(str(date2))
# print(dt.year)
# print(dt2.timestamp())
# print(dt.timestamp() - dt2.timestamp())
# print(date)
# date_to_check = input('Date to check(YYYY-MM-DD): ')
# date = '-'.join(date_to_check)


def display_by_period():
    period_expenses = []
    starting_date = input('Starting from(YYYY-MM-DD): ')
    finish_date = input('Ending on(YYYY-MM-DD): ')
    try:
        starting_date = pendulum.from_format(starting_date, 'YYYY-MM-DD').date()
        finish_date = pendulum.from_format(finish_date, 'YYYY-MM-DD').date()
    except ValueError:
        print('The dates should be in the correct format: YYYY-MM-DD.')
        return

    starting_date = pendulum.parse(str(starting_date))
    finish_date = pendulum.parse(str(finish_date))
    print(starting_date.timestamp())
    print(finish_date.timestamp())
    print(starting_date.timestamp() - finish_date.timestamp())


display_by_period()