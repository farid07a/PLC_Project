class salary:
    value = 0

    def print_salary(self):
        print("Salary :", self.value)

    def print_net_salary(self,rate_percentage):
        rate = self.value / rate_percentage
        print("Net Salary :", self.value-rate)


salaryObj = salary()

salaryObj.value = 1500

salaryObj.print_salary()

salaryObj.print_net_salary(10)
