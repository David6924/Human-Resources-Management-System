#Implementações atuais do projeto de software 
from datetime import datetime

class Employees: # Criação de uma classe de objetos para os trabalhadores empregados 

    number_of_employees = 0 # contador de empregrados

    def __init__(self, name, age, email, departament, work_position, salary_per_hours, hire_date):
        self.name = name 
        self.age = age
        self.email = email 
        self.departament = departament  
        self.work_position = work_position
        self.salary_per_hours = salary_per_hours
        self.hire_date = hire_date
        self.benefits = []
        self.performance = []
        self.training = []
        self.request = []
        Employees.number_of_employees += 1
    # Retorna o nome do empregado
    def __str__(self):
        return self.name 
    # Metodo de impressão de empregados
    def descrition_of_employees(self):
        print(f"Name : {self.name}\nAge : {self.age}\nEmail : {self.email}\nDepartament : {self.departament}\nPosition : {self.work_position}\nSalary per hours : {self.salary_per_hours}\nHire Date : {self.hire_date}\nBenefits: {', '.join(self.benefits) if self.benefits else 'None'}")
    # Leave Request
    def add_leave_requests(self, start_date, end_date, reason):
        leave = {
            "f_Date" : start_date,
            "s_Date" : end_date,
            "Description" : reason
        }
        self.request.append(leave) # Motivos de afastamento
    def remove_leave_requests (self, index):
        if len (self.request) <= 0:
            print("There's nothing here")
        elif 0 <= index < len(self.request):
            removed = self.request.pop(index)
            print(f"The leave requeste period is {removed['f_Date']} at {removed['s_Date']} was removed")
    def show_leave_requests (self):
        print(f"Leave requeste scheduled for {self.name}")
        if not self.request:
            print(f"There's no leave requeste scheduled for {self.name}")
        else:
            for i, leave in enumerate(self.request, 1):
                print(f"{i}) {leave['f_Date']} at {leave['s_Date']} - {leave['Description']}")
    # Training -------------------------------------------------------------------
    def add_training (self, date_str, time_str, description): # Marcar reuniões e horários para os funcionários
        session = {
            "Date" : date_str,
            "Time" : time_str,
            "Description" : description
        }
        self.training.append(session) # Desmarcar reuniões 
    def remove_training (self, index):
        if len(self.training) <= 0:
            print("There's nothing here")
        elif 0 <= index < len(self.training):
            removed = self.training.pop(index)
            print(f"The training session on {removed['Date']} at {removed['Time']} was removed.")
        else:
            print("Invalid Index")
    def show_training (self):
        print(f"training sessions scheduled for {self.name}")
        if not self.training:
            print(f"There's no session scheduled for {self.name}")
        else:
            for i, session in enumerate(self.training, 1):
                print(f"{i}) {session['Date']} at {session['Time']} - {session['Description']}")
    # Performace Evaluation -----------------------------------------------------------
    def add_Performace_evaluation (self, level): # Estudar um sistema de análise de performace do trabalhador
        performance_levels= {
            1 : "Good",
            2 : "Avarege",
            3 : "Bad"
        }
        if level in performance_levels:
            self.performance.append(level)
            print(f"Avaliation '{performance_levels[level]}' added for {self.name}.")
        else:
            print("Invalid input")
    def remove_performance_evaluation (self, level):
        performance_levels= {
            1 : "Good",
            2 : "Avarege",
            3 : "Bad"
        }
        if 0 <= level < len(self.performance):
            removed= self.performance.pop(level)
            print(f"Avaliation '{performance_levels[removed]}' was removed sucessfuly.")
        else:
            print("Invalid index")
    def show_performace (self):
        performance_levels= {
            1 : "Good",
            2 : "Avarege",
            3 : "Bad"
        }

        print(f"\nPerformance evaluation of {self.name}:")
        if self.performance:
            for i, level in enumerate(self.performance, 1):
                print(f"{i}) {performance_levels[level]}")
        else:
            print("No one evaluated")
    # Benefits -------------------------------------------------------------
    def add_benefits(self,benefit): # Os beneficios que serão acumulados serão inseridos em uma lista vazia
        if benefit not in self.benefits:
            self.benefits.append(benefit)
            print(f"The benefit {benefit} was added in {self.name}")
        else:
            print("The benefit was already added")
    def remove_benefits(self, benefit):
        if benefit in self.benefits:
            self.benefits.remove(benefit)
            print(f"The benefit {benefit} was removed in {self.name}")
        else:
            print("The benefit was already removed")
    
#-------------------------------------------------------------------
class Atendence: # Realiza a chamada dos funcionários e vai servir como parametro para a função de pagamento

    def __init__(self, employee):
        self.employee = employee
        self.record = []

    def clock_in (self):
        now = datetime.now() # Pega o tempo e a data atual
        self.record.append({"in": now, "out": None}) # Tulpla com biblioteca para organizar as informações
        print(f"{self.employee.name} clocked in at {now.strftime('%H:%M:%S')}")

    def clock_out (self):
        now = datetime.now()
        if self.record and self.record[-1]["out"] is None:
            self.record[-1]["out"] = now
            print(f"{self.employee.name} clocked out at {now.strftime('%H:%M:%S')}")
        else :
            print("You need to clock in before clock out")

    def show_records (self):
        print(f"\nRecords of {self.employee.name}: ")
        for i, record in enumerate(self.record, 1):
            in_time = record['in'].strftime('%Y-%m-%d %H:%M:%S')
            out_time = record['out'].strftime('%Y-%m-%d %H:%M:%S') if record['out'] else "Still working"
            print(f"{i}) IN: {in_time} | OUT: {out_time}")

    def worked_hours_per_day(self):
        print(f"\nWorked hours for {self.employee.name}:")
        total_seconds = 0

        for i, record in enumerate(self.record, 1):
            in_time = record["in"]
            out_time = record["out"]

            if out_time is not None:
                worked = out_time - in_time
                total_seconds += worked.total_seconds()
                print(f"{i}) {in_time.strftime('%Y-%m-%d')} - {worked}")
            else:
                print(f"{i}) {in_time.strftime('%Y-%m-%d')} - still working...")

        total_hours = total_seconds // 3600
        total_minutes = (total_seconds % 3600) // 60

        print(f"\nTotal worked time: {int(total_hours)} hours and {int(total_minutes)} minutes\n")

#---------------------------------------------------------------
class Payment:
    def __init__(self, attendence, salary_per_hours):
        self.attendece = attendence 
        self.salary_per_hours = salary_per_hours

    def caculate_payment (self):
        total_seconds = 0
        for record in self.attendece.record:
            if record["in"] and record["out"]:
                worked = record["out"] - record["in"]
                total_seconds += worked.total_seconds()
            total_hours = total_seconds / 3600
            pay = total_hours * self.salary_per_hours
            
            return pay 
   
    
# Exemplo de empregados 
employee_1 = Employees("Marcela Rocha", 19, "Marcela_2023@gmail.com", "Sistemas embarcados","Especialista em Hardware",500,2023)
employee_2 = Employees("Fernando Emídio", 21, "Fe_Emi@gmail.com", "Redes de computadores","Especialista em Redes Móveis",200, 2024)
employee_3 = Employees("David Kelve", 20, "dkob@ic.ufal.br", "Recursos humanos","Especialista em HRCM",300, 2025)

atendence_1 = Atendence(employee_1)
atendence_2 = Atendence(employee_2)
atendence_3 = Atendence(employee_3)
# Lista de empregrados 

employees_list = [employee_1, employee_2, employee_3]
atendence_list = [atendence_1, atendence_2, atendence_3]

# Terminal interativo
 
while True:
    print("============== Human Resources Management System ==============\n")
    print("Chose your action: ")
    print("(1) Employees Data\n(2) Management\n(3) Payment\n(4) Exit")

    chose = int(input())

    match chose:
        case 1:
            print("Chose your action: ")
            print("(1) Employees documentation\n(2) Add a new employee\n(3) Employees modify\n(4) Remove an Employee\n(5) Benefits management ")
            chose_1 = int(input())
            # Informações do trabalhador
            match chose_1:
                case 1: # Employee documentation
                    print("\n")
                    for employees in employees_list:
                        employees.descrition_of_employees()
                        print("\n")
                    print(f"Number of employess : {Employees.number_of_employees}")
                case 2: # add a new employee -> Recrutamento
                    print("Please, right bellow add the new employee documentation !")

                    while True:
                        name = input("Name: ")
                        age = input("Age: ")
                        email = input("Email: ")
                        departament = input("Departament: ")
                        Work_position = input("Work Position: ")
                        salary = input("salary per hours: ")
                        hire_date = input("Hire Date: ")

                        new_employee = Employees(name, age, email, departament, Work_position, salary, hire_date)

                        employees_list.append(new_employee)

                        print("\nEmployee successfully added!")
                        print(f"Number of employees : {Employees.number_of_employees}")
                        again = input("Do you want to add another employee ? (y/n) ").lower()
                        if again != 'y':
                            print("\n")
                            break
                case 3: # Employees modification 
                    while True:
                        j = 1
                        print("Employees list")
                        for employee in employees_list:
                            print(f"({j}) {employee.name}")
                            j += 1
                        try:

                            mod = int(input("Chose the employee who you want modify: "))
                            chosen_one = employees_list[mod-1]

                            types_of_datas = {
                                1: "name",
                                2: "age",
                                3: "email",
                                4: "departament",
                                5: "Work_position",
                                6: "salary_per_hours",
                                7: "hire_date"
                            }
                            if 0 < mod <= len(employees_list):
                                print("(1) Name || (2) Age || (3) Email || (4) Departament || (5) Work Position || (6) Salary per hours|| (7) Hire Date")
                                data = int(input("Chose one data who you want modify: "))
                                if data in types_of_datas:
                                    new_value = input(f"Enter the new data for {types_of_datas[data]}: ")
                                if types_of_datas[data] in ["age", "hire_date", "salary_per_hours"]:
                                    new_value = int(new_value)
                                setattr(chosen_one, types_of_datas[data], new_value)
                                print(f"{types_of_datas[data]} was modified successfully")

                                loop = (input("Do you want modify some atribute again (y/n)?"))
                                if loop != 'y':
                                    break

                            else :
                                print("Invalid employee number\n")
                                
                        except ValueError:
                            print("Invalid input. Please enter a number.\n")

                        
                case 4: # Remove an employee
                    while True:
                        i = 1
                        print("Employees list")
                        for employee in employees_list:
                            print(f"({i}) {employee.name}")
                            i += 1
                        if len(employees_list) == 0:
                                print("Theres nothing here")
                                break
                        remove_index = int(input("Enter the number of the employee to remove: "))
                        try:
                            
                            if 0 < remove_index <= len(employees_list):
                                removed = employees_list.pop(remove_index-1)
                                Employees.number_of_employees -= 1
                                print(f"{removed.name} has been removed from the system.\n")
                            else :
                                print("Invalid employee number\n")
                        except ValueError:
                            print("Invalid input. Please enter a number.\n")

                        again = input("Do you want to add another employee ? (y/n) ").lower()
                        if again != 'y':
                            print("\n")
                            break
                case 5: # Benefits
                    print("Employees list")
                    for i, employee in enumerate(employees_list, start=1):
                        print(f"({i}) {employee.name}")
                    try:
                        chosen = int(input("Chose an employee"))-1
                        if 0 <= chosen < len(employees_list):
                            chosen_one = employees_list[chosen]
                            print(f"Managing benefits of {chosen_one}")
                            print("(1) Add benefit\n(2) Remove benefit\n(3) Show benefits")
                            
                            act = int(input("Chose you action: "))

                            if act == 1 :
                                benefit = input("Enter the benefit to add: ")
                                chosen_one.add_benefits(benefit)
                            elif act == 2:
                                benefit = input("Enter the benefit to remove: ")
                                chosen_one.remove_benefits(benefit)
                            elif act == 3: 
                                print("Benefits: ", ", ".join(chosen_one.benefits) if chosen_one.benefits else "None")
                            else:
                                print("Invalid option")
                        else: 
                            print("Invalid Employee number")

                    except ValueError:
                        print("Invalid input. Please enter a number.\n")
                case _: 
                    print("Invalid option") 
        case 2: # Manegement
            print("Chose your action: ")
            print("(1) Time tracking register\n(2) Atendence Records\n(3) Show worked hours per employee\n(4) Performance Evaluation management\n(5) Meetings\n(6) Leave request")
            chose_2 = int(input())
            match chose_2:
                case 1:
                    clock = int(input("what you want register ?\n(1)Clock in\n(2)clock out\n"))
                    print("Employees list")
                    for i, employee in enumerate(employees_list, start=1):
                        print(f"({i}) {employee.name}")
                    try:
                        chose = int(input("Chose one employee to register: "))-1
                        chosen_one = atendence_list[chose]

                        if clock == 1:
                            chosen_one.clock_in()
                        elif clock == 2:
                            chosen_one.clock_out()
                        else:
                            print("Invalid option")
                    except ValueError:
                        print("Invalid input. Please enter a number.\n")
                case 2:
                    for atendence in atendence_list:
                        atendence.show_records()
                        print()
                case 3: 
                    print("Employees list")
                    for i, employee in enumerate(employees_list, start=1):
                        print(f"({i}) {employee.name}")
                    try: 
                        chose = int(input("Chose one employee to view worked hours: "))-1
                        if 0 <= chose < len(employees_list):
                            atendence_list[chose].worked_hours_per_day()
                        else:
                            print("Invalid employee number.\n")
                    except ValueError:
                        print("Invalid input")
                case 4: 
                    print("Employees list")
                    for i, employee in enumerate(employees_list, start=1):
                        print(f"({i}) {employee.name}")
                        
                    try:
                        chose = int(input())- 1
                        chosen_one = employees_list[chose]
                        if 0 <= chose < len(employees_list):
                            print("(1) Add a evaluation\n(2) Remove a evaluation\n(3) Show the evaluation ")
                            case = int(input("Chose one index: "))
                            if case == 1:
                                print("Chose the evaluation level: ")
                                print("(1) Good\n(2) Avarage\n(3) Bad")
                                eva = int(input("Level: "))
                                chosen_one.add_Performace_evaluation(eva)
                            elif case == 2: 
                                chosen_one.show_performace()
                                index = int(input("Type the number who you want remove: ")) -1
                                chosen_one.remove_performance_evaluation(index)
                            elif case == 3:
                                chosen_one.show_performace()
                            else: 
                                print("Invalid index")
                        else:
                            print("Invalid employee number.\n")

                    except ValueError:
                        print("Invalid input")
                case 5:
                    print("Employees list")
                    for i, employee in enumerate(employees_list, start=1):
                        print(f"({i}) {employee.name}")
                    try:
                        chose = int(input("Chose one employee to analize the meeting schedule: "))- 1
                        chosen_one = employees_list[chose]
                        if 0 <= chose < len(employees_list):
                            print("(1) Add a new meet\n(2) Remove a meet\n(3) Show the meets ")
                            case = int(input("Chose one index: "))
                            if case == 1:
                                data = str(input("Date: "))
                                temp = str(input("Hour: "))
                                description = str(input("Description: "))
                                chosen_one.add_training(data, temp, description)
                            elif case == 2:
                                chosen_one.show_training()
                                index = int(input("Type the number who you want remove: "))-1
                                chosen_one.remove_training(index)
                            elif case == 3:
                                chosen_one.show_training()
                            else:
                                print("Invalid index")
                        else:
                            print("Invalid employee number.\n")

                    except ValueError:
                        print("Invalid input")
                case 6:
                    print("Employees list")
                    for i, employee in enumerate(employees_list, start=1):
                        print(f"({i}) {employee.name}")
                    try:
                        chose = int(input("Chose one employee to manage leave requests: ")) - 1
                        if 0 <= chose < len(employees_list):
                            chosen_one = employees_list[chose]
                            print(f"Managing leave requests for {chosen_one.name}")
                            print("(1) Add leave request\n(2) Remove leave request\n(3) Show leave requests")
                            action = int(input("Choose your action: "))

                            if action == 1:
                                start_date = input("Enter start date (e.g., 01/08): ")
                                end_date = input("Enter end date (e.g., 05/08): ")
                                reason = input("Enter reason: ")
                                chosen_one.add_leave_requests(start_date, end_date, reason)
                            elif action == 2:
                                chosen_one.show_leave_requests()
                                index = int(input("Enter the index of the leave request to remove: ")) - 1
                                chosen_one.remove_leave_requests(index)
                            elif action == 3:
                                chosen_one.show_leave_requests()
                            else:
                                print("Invalid option")
                        else:
                            print("Invalid employee number.")
                    except ValueError:
                        print("Invalid input. Please enter numbers.")
                case _:
                    print("Chose your action: ")
        case 3:
            print("(1) Payment without benefits\n(2) Payment with benifits")
            chose = int(input("Chose your action: "))
            match chose:
                case 1:
                    for i, employee in enumerate(employees_list, start=1):
                        print(f"({i}) {employee.name}")
                    person = int(input("Chose the employee who you want calculate the salary: "))-1
                    
                    try:
                        if 0 <= person < len(employees_list):
                            employee = employees_list[person]
                            attendence = atendence_list[person]
                            payment = Payment(attendence, employee.salary_per_hours)
                            money = payment.caculate_payment()

                            print(f"\nTotal payment for {employee.name}: R$ {money:.2f}\n")
                        else:
                            print("Invalid employee number\n")
                    except ValueError:
                        print("Invalid input")
                case _:
                    print("Chose your action: ")
        case 4:
            exit = input("Are you sure ? (y/n) ").lower()
            if exit == 'y':
                break
        case _:
            print("Invalid option")




