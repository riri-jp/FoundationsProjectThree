# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = input("what is your name")
my_age = input("How old are you")
my_bio = input("Tell me somthing about your self")
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)
    options()

def options():
    print("-"*20)
    print("would you like to:")
    text="""
    1) Create a new club.
    or:
    2) Browse and join clubs.
    or:
    3)View existing clubs.
    or:
    4)Display members of a club.
    or:
    -1)Close application.
    """
    print(text)
    while True:
        options= input()
        if options == "1":
            create_club()
        elif options == "2":
            join_clubs()
        elif options == "3":
            view_clubs()
        elif options == "4":
            view_club_members()
        elif options == "-1":
            print("Goodbye!")
            quit()
        else:
            options = input("Invalid Option")

def create_club():
    club_name = input("What do you like to name your club? ")
    club_description = input("Describe your club: ")
    new_club= Club(club_name, club_description)
    new_club.recruit_member(myself)
    new_club.assign_president(myself)
    clubs.append(new_club)
    print ("Enter the numbers of the people you would like to recruit to your new club and (-1 to stop)")
    print ("-"*20)
    for index,person in enumerate(population):
        print ("[%s] %s"% (index+1, person.name))
    while True:
        member = input()
        if member == "-1":
            break
        elif int(member)>=1 and int(member)<= len(population):
            new_club.recruit_member(population[int(member)-1])
            print("Member added successfully")
        else:
            print("invalid ")
    text=("""
        Here's your club:
        %s
        %s
        Members:
        """%(new_club.name,new_club.description))
    print (text)
    new_club.print_member_list()

def view_clubs():
    for club in clubs:
        text=("""
            Name: %s
            Description: %s
            Member: %s
            """%(club.name, club.description, len(club.member)))
    print(text)
    

def view_club_members():
    flage=False
    view_clubs()
    club_name= input("Enter the name of the club whose members you'd like to see: ")
    for club in clubs:
        if club.name.lower() == club_name.lower():
            club.print_member_list()
            flage=True
    if flage == False:
        print("Clube name doesn't exist")
        view_club_members()

def join_clubs():
    flage=False
    view_clubs()
    club_name= input("Enter the name of club you'd like to join :")
    for club in clubs:
        if club.name.lower() == club_name.lower():
            club.recruit_member(myself)
            flage=True
    if flage == False:
        print("Club name doesn't exist")
        join_clubs()


def application():
    introduction()
    # your code goes here!
    
