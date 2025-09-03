import x


class Parent:
    def __init__(self, name, job):
        self.name = name
        self.job = job

class Dad(Parent):
    def __init__(self,relationship):
        super(). __init__(name="john", job="military")
        self.relationship = relationship

    def __str__(self):
        return (f"My dad name is {self.name}"
                f"He is a {self.job} in South sudan defense forces")

    def relations(self):
        print(f"He is my {self.relationship}")

class Mom(Parent):
    def __init__(self,relationship):
        super(). __init__(name="mary", job="housewife")
        self.relationship = relationship

    def __str__(self):
        return (f"My mom name is {self.name}"
                f"She is a {self.job} and takes cares of us")

    def relations(self):
        print(f"She is my {self.relationship}")


c = Mom("Mom")
c2 = Dad("father")

for x in [c,c2]:
    print(x.name)
    print(x.job)
    print(x.__str__())
    x.relations()