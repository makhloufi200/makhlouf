class MemberStore:
    members = []
    posts = []

    def add_member(self, member):
        MemberStore.members.append(member)

    def get_all_member(self):
        return MemberStore.members

    def add_post(self, post):
        MemberStore.posts.append(post)

    def get_all_post(self):
        return MemberStore.posts