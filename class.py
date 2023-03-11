class Total:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"姓名：{self.name}\n工号：{self.id}")


class FullTimeEmployee(Total):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary
    def calculate(self):
        return f"月薪：{self.monthly_salary}"

class PartTimeEmployee(Total):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days
    def calculate(self):
        return f"月薪：{self.daily_salary * self.work_days}"


sqj = FullTimeEmployee("sqj", 10001, 4000)
wldss = PartTimeEmployee("wldss", 10002, 356, 15)
sqj.print_info()
print(sqj.calculate())
wldss.print_info()
print(wldss.calculate())
open("text/Employee.txt", encoding="utf-8")