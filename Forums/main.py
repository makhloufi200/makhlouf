import models
import memberstore

def add_members(member, instance):
    instance.add_member(member)

def add_posts(post, instance_post):
    instance_post.add_post(post)


####### create member
member1 = models.Member("Mohamed", 60)
member2 = models.Member("Smail", 40)

instance = memberstore.MemberStore()
add_members(member1,instance)
add_members(member2,instance)

post1 = models.Post("First Post", "This is My First Post", 1)

post2 = models.Post("Hello My Friend", "Hello My Friend, Good Luck", 2)

post3 = models.Post("Third Post", "My Third Post", 3)

instance_post = memberstore.MemberStore()
add_posts(post1,instance_post)
add_posts(post2, instance_post)
add_posts(post3, instance_post)

