# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        self.name = name
        self.bio = bio
        self.age = age



class Club():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.president = None
        self.member = []


    def assign_president(self, person):
        self.president = person


    def recruit_member(self, person):
        self.member.append(person)


    def print_member_list(self):
        for member in self.member:
            if member.name == self.president.name:
                print("- %s (%s yers old, President) - %s" %(member.name, member.age, member.bio))
            else:
                print("- %s (%s yers old, ) - %s" %(member.name, member.age, member.bio))
