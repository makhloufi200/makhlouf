class Member:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = 0
        #print ('Name: {}\t\tAge: {}'.format(self.name, self.age))
    def __str__(self):
        return 'Name: {}, Age: {}'.format(self.name, self.age)


class Post:

    def __init__(self, title, body, member_id):
        self.id = 0
        self.title = title
        self.body = body
        self.member_id = member_id
        #print ('Title: {}\tBody:{}'.format(self.title, self.body))
        #print self.title + " " + self.body
    def __str__(self):
        return 'Title: {}, Body:{}'.format(self.title, self.body)