# 클래스 정의 및 테스트 코드 통합
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        #f-string문법(python 3.6)
        print(f"ID: {self.id}, Name: {self.name}")


class Manager(Person):
    def __init__(self, id, name, title):
        #부모를 지칭하는 함수
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")


class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")


# 테스트 코드
def run_tests():
    print("===== 테스트 1: Person 객체 생성 및 출력 =====")
    p1 = Person(1, "Alice")
    p1.printInfo()

    print("\n===== 테스트 2: Manager 객체 생성 및 출력 =====")
    m1 = Manager(2, "Bob", "Project Manager")
    m1.printInfo()

    print("\n===== 테스트 3: Employee 객체 생성 및 출력 =====")
    e1 = Employee(3, "Charlie", "Python")
    e1.printInfo()

    print("\n===== 테스트 4: Manager 객체 타이틀 확인 =====")
    m2 = Manager(4, "David", "Team Lead")
    assert m2.title == "Team Lead"
    m2.printInfo()

    print("\n===== 테스트 5: Employee 객체 스킬 확인 =====")
    e2 = Employee(5, "Eve", "Java")
    assert e2.skill == "Java"
    e2.printInfo()

    print("\n===== 테스트 6: Person 리스트 출력 =====")
    people = [Person(6, "Frank"), Person(7, "Grace")]
  