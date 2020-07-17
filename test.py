class B:
    # def __str__(self):
    #     return " b str"

    def __repr__(self):
        return " b repr"


class A(B):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # return self.name

    # def __str__(self):
    #     return self.age + "," + self.name

    # def __repr__(self):
    #     return self.age + "," + self.name


a = A("a", "1234")
print(a.name)

print(str(a))
print(str(a.name))