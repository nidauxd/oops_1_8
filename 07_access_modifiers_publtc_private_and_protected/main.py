class Employee:
    def __init__(self, name , salary ,ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn
if __name__ == "__main__":
    emp = Employee("Farah" , 75000 , "234-567-89")
    # access public variable
    print("public", emp.name)
    # access protecte variable
    print("protected",emp._salary)
    # access private variable
    try:
      print("protecred",emp.__ssn)
    except AttributeError:
     print("private cannot access")

