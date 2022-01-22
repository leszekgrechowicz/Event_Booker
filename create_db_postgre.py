from psycopg2 import connect, OperationalError

db_name = "event-booker"


def db_connect():
    connected = False
    while not connected:

        user = input("Please provide Data-Base user name: ")
        password = input("Password: ")

        try:
            cnx = connect(user=f"{user}", password=f"{password}", host="localhost")
            cnx.autocommit = True
            connected = True

        except OperationalError as error:
            print(f"Error ! --> {error} ")

    db_created = False
    while not db_created:

        print("You are successfully connected to the database !")

        sql = f"CREATE DATABASE {db_name};"

        try:
            cursor = cnx.cursor()
            cursor.execute(sql)
            print(f"Database named: '{db_name}' has been created.")

        except OperationalError as error:
            print(f"Error ! --> {error} ")
        else:
            cursor.close()
            cnx.close()
            break


print("\nWelcome in Event-Booker Data-Base creator !\n"
      "----------------------------------------\n"
      "I am going to create DB for you - DB name => event-booker. ")

not_accepted = True
while not_accepted:
    confirmation = input('\nDo you want to proceed ? y/n -> enter\n>>> ')
    if confirmation.lower() == 'y':
        db_connect()
        not_accepted = False
    else:
        print('Thank you for using our DB creator, Good bye !')
        not_accepted = False
