class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):
    def get_full_name(self):
        return f'{self.name, self.surname}'  # Не уверен в надобности здесь position в связи с заданием.

    def get_total_income(self):
        return round(self._income_wage + self._income_bonus, 2)


pos = Position('Ivan', 'Petrov', 'engineer', {"wage": 150000, "bonus": 50000})
print(pos.get_full_name())
print(pos.get_total_income())

