from imports import *

mydb = pg.connect(
        host = "localhost",
        user = "postgres",
        password = "root3",
        database = "BizCardx",
        port = "5432"
                   )
mycursor = mydb.cursor()

# TABLE CREATION
mycursor.execute('''CREATE TABLE IF NOT EXISTS card_data
                   (company_name TEXT,
                    card_holder TEXT,
                    designation TEXT,
                    mobile_number VARCHAR(50),
                    email TEXT,
                    website TEXT,
                    area TEXT,
                    city TEXT,
                    state TEXT,
                    pin_code VARCHAR(10)
                    )''')
