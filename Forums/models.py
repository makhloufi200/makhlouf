class Member:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print self.name + " " + str(self.age)

class Post:

    def __init__(self, title, body):
        self.title = title
        self.body = body

        print self.title + " " + self.body