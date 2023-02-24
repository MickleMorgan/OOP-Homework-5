import logging
logger = logging.getLogger('simple_example')
ch = logging.FileHandler(__name__)
ch.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class TooMuchStudents(Exception):
    """
    Exception raised when trying to add more students than the group size limit.

    Attributes:
        max_group (int): Maximum group size limit.
    """
    def __init__(self, max_group: int):
        self.max_group = max_group

    def __str__(self):
        return f'You can\'t add more than {self.max_group} students'


class StudentAlreadyExist(Exception):
    """
        Exception raised when trying to add a student who is already in the group.

        Attributes:
            student (str): Name of the student.
            group_name (str): Name of the group.
    """
    def __init__(self, student, group_name):
        self.student = student
        self.group_name = group_name

    def __str__(self):
        return f'{self.student} is already in group {self.group_name}'


class Person:
    """
        Class representing a person.

        Attributes:
            name (str): First name of the person.
            surname (str): Last name of the person.
            sex (str): Sex of the person.
            age (int): Age of the person.
            nationality (str): Nationality of the person.
    """
    def __init__(self, name, surname, sex, age, nationality):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age
        self.nationality = nationality

    def __str__(self):
        """
                Returns a string representation of the person.

                Raises:
                    TypeError: If the person's nationality is Russian.

                Returns:
                    str: String representation of the person.
        """
        if self.nationality.lower() == ('russian'):
            raise TypeError('russian ship go to hell')
        else:
            return f'Name: {self.name} {self.surname}\nSex: {self.sex}\nAge {self.age} years\n' \
                   f'Nationality {self.nationality}'


class Student(Person):
    """
        Class representing a student.

        Attributes:
            status (str): Status of the student .
            name (str): First name of the student.
            surname (str): Last name of the student.
            sex (str): Sex of the student.
            age (int): Age of the student.
            nationality (str): Nationality of the student.
    """
    def __init__(self, name, surname, sex, age, nationality, status):
        super().__init__(name, surname, sex, age, nationality)
        self.status = status

    def __str__(self):
        return f'{super().__str__()}\nStatus:{self.status}\n'


class Group:
    """
       Class representing a group of students.

       Attributes:
           speciality (str): Name of the group's speciality.
           group_type (str): Type of the group .
           group_size (int): Maximum size limit of the group (default: 10).
           students (list): List of students in the group.
    """
    def __init__(self, speciality, group_type, group_size=10):
        self.speciality = speciality
        self.group_type = group_type
        self.students = []
        self.group_size = group_size
        self.index = 0

    def add_student(self, student):
        if len(self.students) >= self.group_size:
            raise TooMuchStudents(self.group_size)
        if student in self.students:
            raise StudentAlreadyExist(student, self.speciality)
        self.students.append(student)
        logger.info('Student added')

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def find_student(self, surname):
        find_student = []
        for person in self.students:
            if person.surname == surname:
                find_student.append(person)
        return find_student

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        value = self.students[self.index]
        self.index += 1
        return value

    def __str__(self):
        return f'Group:{self.speciality}\n{self.group_type}\n\n' + '\n'.join(map(str, self.students))


my_group = Group('Math', 'Advanced')

my_group.add_student(Student('Andrey', 'Nikolov', 'Male', 22, 'American', 'Undergraduate'))
my_group.add_student(Student('Andrey2', 'Nikolov2', 'Female', 23, 'Canadian', 'Graduate'))
my_group.add_student(Student('Andrey3', 'Nikolov3', 'Male', 24, 'British', 'Undergraduate'))

for student in my_group:
    print(student)
