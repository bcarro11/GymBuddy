import itertools

"""
This module is used as a staging ground of sorts. Not utilized directly, but to allow
the team to conceptualize different things prior to implementing them into the system
such as user matching and the user objects themselves. Will be removed in Phase 4.
"""

class User:

    id_iter = itertools.count() #increments the user id

    id = None
    firstname = None
    lastname = None
    nickname = None
    dob = None
    gender = None
    email = None
    password = None
    preferredgym = None
    #usericon = None

    routineset = set()
    routinematchdictionary = {}

    def __init__(self, id, firstname, lastname, nickname, dob, gender, email, password, preferredgym):

        self.id = next(User.id_iter)
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.dob = dob
        self.gender = gender
        self.email = email
        self.password = password
        self.preferredgym = preferredgym

    def set_routine(self, element):

        self.routineset.add(element); 
    
    def routine_match(self, id, user_pool):

        print('User pool:', user_pool)
        currentuser_set = self.routineset
        routinematchdictionary = {}
        final_dictionary = {}

        for i in range(len(user_pool)):

            if user_pool[i] == self:

                continue

            partneruser_set = user_pool[i].routineset
            print ('partner set', partneruser_set)
            overlap_set = currentuser_set.intersection(partneruser_set)
            length_overlap = len(overlap_set)
            routinematchdictionary[user_pool[i]] = length_overlap

        sorted_routinematchdictionary = sorted(routinematchdictionary.items(),
        key = lambda x:x[1], reverse = True)

        final_dictionary = dict(sorted_routinematchdictionary)

        return final_dictionary
    