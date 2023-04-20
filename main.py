from user import User

global user_pool

user_pool = []
final = {}

Stefani = User(id, "Stefani", "Page", "Stef", 1/15/1988, "Female", "stefani.page@gmail.com", "password", "Golds")
user_pool.append(Stefani)
Tracy = User(id, "Tracy", "Boone", "Trace", 4/6/1970, "Female", "tracy.boone@gmail.com", "getout", "Golds")
user_pool.append(Tracy)
Sam = User(id, "Sam", "Jones", "Sjones", 3/14/1991, "Male", "sam.jones@gmail.com", "flower", "Golds")
user_pool.append(Sam)
Kate = User(id, "Kate", "Smith", "Kay", 6/8/1978, "Female", "kate.smith@gmail.com", "pickle", "Golds")
user_pool.append(Kate)
Jim = User(id, "Jim", "Halpert", "Big Tuna", 8/9/1984, "Male", "jim.halpert@gmail.com", "pamiscute", "Golds")
user_pool.append(Jim)

Stefani.routineset = {1, 2, 3, 4, 5, 6}
Tracy.routineset = {1, 2, 3}
Sam.routineset = {8}
Kate.routineset = {1, 2, 3, 4, 5}
Jim.routineset = {1, 2, 3, 4, 5, 6}
#user_pool = [0, 1, 2]
#user_pool = ["Stefani", "Tracy", "Sam"]

#print(Stefani.routineset) 
#final = Tracy.routine_match(Tracy.id, user_pool)
#print('Final: ', str(final))

Stefani.add_rating(Tracy, 4)
Stefani.add_rating(Kate, 1)
Stefani.add_rating(Jim, 5)
Stefani.add_rating(Sam, 3)
Stefani.avg_user_rating = Stefani.get_average_rating()
print(str(Stefani.avg_user_rating))
print(str(Stefani.get_rating(Tracy)))