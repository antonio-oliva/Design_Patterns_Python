from abc import ABC, abstractmethod
from typing import List


class Student:

    def __init__(self, name: str, rollNo: int) -> "Student":
        self._name = name
        self._rollNo = rollNo

    def getName(self) -> str:
        return self._name

    def setName(self, name: str) -> None:
        self._name = name

    def getRollNo(self) -> int:
        return self._rollNo

    def setRollNo(self, rollNo: int) -> None:
        self._rollNo = rollNo


class StudentDAOInterface(ABC):

    @abstractmethod
    def getAllStudents(self) -> List[Student]:
        pass

    @abstractmethod
    def getStudent(self, rollNo: int) -> Student:
        pass

    @abstractmethod
    def updateStudent(self, student: Student) -> None:
        pass

    @abstractmethod
    def deleteStudent(self, student: Student) -> None:
        pass


class StudentDAO(StudentDAOInterface):

    def __init__(self):
        student1 = Student("Robert", 0)
        student2 = Student("John", 1)
        self.students = [student1, student2]

    def getAllStudents(self) -> List[Student]:
        return self.students

    def getStudent(self, rollNo: int) -> Student:
        return self.students[rollNo]

    def updateStudent(self, student: Student) -> None:
        self.students[student.getRollNo()].setName(student.getName())
        print(f"Student: RollNo {student.getRollNo()}, updated in the database")

    def deleteStudent(self, student: Student) -> None:
        self.students.remove(self.students[student.getRollNo()])
        print(f"Student: RollNo {student.getRollNo()}, deleted from the database")


if __name__ == "__main__":

    studentDAO = StudentDAO()

    # Print all students
    for student in studentDAO.getAllStudents():
        print(f"Student: [RollNo : {student.getRollNo()}, Name : {student.getName()}]")

    print("")

    # Update student
    student = studentDAO.getStudent(0)
    student.setName("Micheal")
    studentDAO.updateStudent(student)

    # Get the student
    studentUpdated = studentDAO.getStudent(0)
    print(f"Student: [RollNo : {studentUpdated.getRollNo()}, Name : {studentUpdated.getName()}]")
