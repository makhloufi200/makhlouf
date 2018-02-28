class MemberStore:
    members = []
    posts = []
    last_id = 1

    def add(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_all(self):
        return MemberStore.members

    def get_by_id(self, id):
        all_members = self.get_all()
        result = None
        for member in all_members:
            if member.id == id:
                result = member
                break
        return result

    def entity_exists(self, member):
        result = False
        if self.get_by_id(member.id) is not None:
            result = True
        return result

    def delete(self, id):
        set_member = self.get_by_id(id)
        MemberStore.members.remove(set_member)

    def update(self, member):
        self.members
    def add_post(self, post):
        MemberStore.posts.append(post)

    def get_all_post(self):
        return MemberStore.posts