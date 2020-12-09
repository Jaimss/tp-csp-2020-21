import multifactorgui as mfg

# create a multi-factor interface to a restircted app
my_auth = mfg.MultiFactorAuth()

# get a username and password
valid = False
while not valid:
    try:
        username = input("What is your username? ")
        password = input("What is your password? ")
        my_auth.set_authorization(username, password)
        valid = True
    except ValueError:
        print('Invalid Username / Password. Passoword and Username must be > 8 characters, and < 28. Password must have letters and numbers.\n')

auth_info = my_auth.get_authorization()
print(auth_info)

# set the users authentication information
question = "What is your favorite color? "
answer = input(question)
my_auth.set_authentication(question, answer)

# start the GUI
my_auth.mainloop()
