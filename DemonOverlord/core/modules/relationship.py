import discord

# user JSON object
# "user_{uid}": {
#     "uid":"{uid}"
#     "relationships": {
#         "good": {
#             "user_{uid}": {
#                 "status": "friend"
#             },
#             "user_{uid}": {
#                 "status": "enemy"
#             }
#         },
#         "bad": {}
#     }
# }


class User:
    __slots__ = (
        "uid", "relationships"
    )

    def __init__(self, user: discord.Member = None, user_dict: dict = None):
        self.uid = user.id
        self.relationships = []

        if user_dict:
            for key in user_dict["relationship"]:
                rel = User.build_relationship(user_dict)
                self.relationships.append()

    @staticmethod
    def build_relationship(self, uid: int) -> Relationship:
        pass

    def __dict__(self) -> dict:
        temp = dict()
        temp["uid"] = self.uid
        temp["relationships"] = dict(good=dict(), bad=dict())

        for elem in self.relationships:
            if isinstance(elem, GoodRelationship):
                temp["relationships"]["good"][f'uid_{elem.uid}'] = elem.name

        return temp


class Relationship:
    __slots__ = (
        "user", "status"
    )
    def __init__(self, status: str, user: User):
        self.user = user
        self.status = status



class GoodRelationship(Relationship):
    def __init__(self, status: str, user: User):
        super().__init__(status, user)


class BadRelationship(Relationship):
    def __init__(self, status: str, user: User):
        super().__init__(status, user)

