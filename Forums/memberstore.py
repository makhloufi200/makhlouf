import itertools
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

    def get_by_name(self, member_name):
        all_members = self.get_all()
        for member in all_members:
            if member.name == member_name:
                yield member

    def entity_exists(self, member):
        result = False
        if self.get_by_id(member.id) is not None:
            result = True
        return result

    def delete(self, id):
        set_member = self.get_by_id(id)
        MemberStore.members.remove(set_member)

    def update(self, member):
        result = None
        all_members = self.get_all()
        for i,item in enumerate(all_members):
            if member.id == item.id:
                all_members[i] = member
                break
        return result

    def get_members_with_posts(self, all_posts):
            all_members = (self.get_all())
            all_posts = self.get_all_post()
            member_with_post = []
            for member in all_members:
                for post in all_posts:
                    if member.id == post.member_id:
                        member_with_post.append(member)
            return member_with_post

    def get_top_two(self, post_store):
        all_members = self.get_members_with_posts(post_store)
        all_members = sorted(all_members, key=lambda x: len(x.posts), reverse=True)
        return all_members[:2]

    def add_post(self, post):
        MemberStore.posts.append(post)

    def get_all_post(self):
        return MemberStore.posts