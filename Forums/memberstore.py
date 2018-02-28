class MemberStore:
    members = []
    posts = []
    last_id = 1
    def add_member(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_all_member(self):
        return MemberStore.members

    def get_by_id(self, id):
        all_members = self.get_all_member()
        result = ''
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

    def delete_member(self, id):
        set_member = self.get_by_id(id)
        set_member.remove()

    def add_post(self, post):
        MemberStore.posts.append(post)

    def get_all_post(self):
        return MemberStore.posts