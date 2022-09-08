#Capgemini python internship task
#1.Design and build employer as part of company Fields

class Employer:
    
    employers_list = []
    def __init__(self,name,
                 last_name,age,
                 job,salary):
        
        self.name = name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.salary = salary
        self.employers_list.append(self)
        self.bonus = 0
        self.total_salary = self.bonus + self.salary

    def apply_bonus(self,bonus):
        self.bonus = bonus
        self.total_salary = self.bonus + self.salary
    
    @staticmethod
    def number_of_employers():
        print('All employers: ',len(Employer.employers_list))
        
    
    @classmethod
    def employer_info(cls,name,last_name):
        for employer in cls.employers_list:
            if employer.name == name and employer.last_name == last_name:
                print('--------------------------------------------')
                print(f'Employer:\nName: {employer.name} Last name: {employer.last_name} ')
                print(f'Age: {employer.age} Job: {employer.job} salary: {employer.salary}')
                print(f'Bonus: {employer.bonus} total salary: {employer.total_salary}')
                print('---------------------------------------------')
               
    
    def delete(self):
        
        self.delete()
    
    @classmethod
    def get_employer(cls,name,last_name):
        for employer in cls.employers_list:
            if employer.name == name and employer.last_name == last_name:
                return employer
    
    @classmethod
    def employers(cls):
        for employer in cls.employers_list:
            print('--------------------------------------------')
            print(f'Employer:\nName: {employer.name} Last name: {employer.last_name} ')
            print(f'Age: {employer.age} Job: {employer.job} salary: {employer.salary}')
            print(f'Bonus: {employer.bonus} total salary: {employer.total_salary}')
            print('---------------------------------------------')
    
    
    
    
class Departments(Employer):
    
    departments = []
    def __init__(self,name):
        self.name = name
        self.departments.append(self)
        self.users = []
        
    @classmethod  
    def add_user(cls,user,department):
        for cls.departm in cls.departments:
            if cls.departm.name == department:
                cls.departm.users.append(user)
                
    @classmethod  
    def display_users(cls,department):
        for departm in cls.departments:
            if departm.name == department:
                for user in departm.users:
                    user.employers()

    @classmethod
    def display_departments(cls):
        print('Departments:')
        for cls.department in cls.departments:
            print(f'Name of department: {cls.department.name} Users in department: {len(cls.department.users)}')
           
            
    def remove_user_from_department(self,name,last_name):
        for user in self.users:
            if user.name == name and user.last_name == last_name:
                self.users.remove(user)
            else:
                print('Invalid name or last name')
                
           
    def apply_bonus(self,bonus):
        for user in self.users:
            user.apply_bonus(bonus)
        
        
        
        
o2 = Employer('Adam','Soja',26,'cos',5000)                 
o = Employer('Sebastian','Soja',22,'JAVA',300)
dep = Departments('AEI')
dep2 = Departments('ISIE')
dep3 = Departments('javson')

Departments.add_user(o2, 'AEI')
while True:
    print('---------------------------------------------')
    print('Add an employer choose 1 ')
    print('Add department choose 2 ')
    print('Add an employer to department choose 3 ')
    print('Bonus an employer choose 4 ')
    print('Bonus to employers of exact department choose 5 ')
    print('Remove an employer choose 6 ')
    print('Remove an employer from department choose 7 ')
    print('See how many employers are there: 8')
    print('See info about employer: 9')
    print('See info about departments: 10')
    print('Display users of exact department: 11')
    choice = int(input('>>>'))
    if choice == 1:
        print('Give required info about employer:')
        name = input('Name: ')
        last_name = input('Last name: ')
        age = input('Age: ')
        job = input('job: ')
        salary = int(input('Salary: '))
        employer = Employer(name, last_name, age, job, salary)
        
    if choice == 2:
        name = input('Department name: ')
        department = Departments(name)
        
    if choice == 3:
        print('Input name and last name of an employer')
        name = input('Employer name: ')
        last_name = input('Employer last name: ')
        department = input('Enter the name of department: ')
        employer = Employer.get_employer(name, last_name)
        Departments.add_user(employer, department)
        
        
    if choice == 8:
        Employer.number_of_employers()
    
    
    if choice == 9:
        print('---------------------------------------------')
        name = input('input name of employer: ')
        last_name = input('input last name of employer: ')
        Employer.employer_info(name, last_name)
        
    if choice == 10:
        Departments.display_departments()
        
    if choice == 11:
        department = input('Enter the name of department: ')
        Departments.display_users(department)
    
    
    