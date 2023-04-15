from user import User

final = {}

Stefani = User(id, "Stefani", "Page", "Stef", 1/15/1988, "Female", "stefani.page@gmail.com", "password", "Golds")
Tracy = User(id, "Tracy", "Boone", "Trace", 4/6/1970, "Female", "tracy.boone@gmail.com", "getout", "Golds")
Sam = User(id, "Sam", "Jones", "Sjones", 3/14/1991, "Male", "sam.jones@gmail.com", "flower", "Golds")

Stefani.routineset = {1, 2, 3, 4, 5}
Tracy.routineset = {1, 2, 3}
Sam.routineset = {3}
#user_pool = [0, 1, 2]
user_pool = ["Stefani", "Tracy", "Sam"]

print(Stefani.routineset) 
final = Stefani.routine_match(Stefani.id, user_pool)
print('Final: ', str(final))
