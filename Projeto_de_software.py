#Implementações atuais do projeto de software 

class Employees: # Criação de uma classe de objetos para os trabalhadores empregados 

    number_of_employees = 0 # contador de empregrados

    def __init__(self, name, age, salary, work_position, hire):
        self.name = name 
        self.age = age 
        self.salary = salary
        self.work_position = work_position
        self.hire = hire
        Employees.number_of_employees += 1
    # Retorna o nome do empregado
    def __str__(self):
        return self.name and self.work_position
    # Metodo de impressão de empregados
    def descrition_of_employees(self):
        print(f"Name : {self.name}\nAge : {self.age}\nSalary : {self.salary}\nJob : {self.work_position}\nIs hired : {self.hire}")

# Exemplo de empregados 

employee_1 = Employees("Marcela Rocha", 19, 50000, "Especialista em sistemas embarcados", True)
employee_2 = Employees("Fernando Emídio", 21, 8000, "Especialista em redes de computadores", True)
employee_3 = Employees("David Kelve", 20, 20000, "Recursos humanos", True)

# Lista de empregrados 

employees_list = [employee_1, employee_2, employee_3]

# Terminal interativo
 
print("============== Human Resources Management System ==============\n")
print("Chose your action :")
print("(1) For see employees descritions\n(2) Something in the future...\n(3) something in the future...")

chose = int(input())
print("\n")

match chose:
    case 1:
        for employees in employees_list:
            employees.descrition_of_employees()
            print("\n")
        print(f"Number of employess : {Employees.number_of_employees}")
    case 2:
        print("Something in the future")
    case 3:
        print("Something in the future")
    case _:
        print("Invalid option")




