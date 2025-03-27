import sqlite3


connection = sqlite3.connect('fivetables/ft.sqlite3')


def create_tables():
    queries = [
            'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE);',
            '''CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                user_id INTEGER,
                order_text VARCHAR(255),
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE );
            ''',
            '''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(64) NOT NULL, price INTEGER)''',
            '''CREATE TABLE IF NOT EXISTS order_item (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            order_id INTEGER NOT NULL, 
            product_id INTEGER NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
            FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE );
            '''
        ]

    try:
        cursor = connection.cursor()

        for q in queries:
            cursor.execute(q)

        connection.commit()

    except Exception as er:
        print(er)
    
def insert_data():
    queries = [
        'INSERT INTO users (name, email) VALUES ("John Doe", "johndoe@gmail.com")',
        'INSERT INTO users (name, email) VALUES ("Evgen Dvodnenko", "evgendvodnenko@gmail.com")',
        'INSERT INTO users (name, email) VALUES ("Anton Andreiev", "andreiev@gmail.com")',

        'INSERT INTO products (title, price) VALUES ("Bread", 30)',
        'INSERT INTO products (title, price) VALUES ("Milk", 35)',
        'INSERT INTO products (title, price) VALUES ("Tea", 15)',
        'INSERT INTO products (title, price) VALUES ("Cookie", 25)',

        'INSERT INTO orders (user_id, order_text) VALUES (2, "Order")',
        'INSERT INTO orders (user_id, order_text) VALUES (1, "ahahha")',

        'INSERT INTO order_item (order_id, product_id) VALUES (2, 4)',
        'INSERT INTO order_item (order_id, product_id) VALUES (1, 3)',
        'INSERT INTO order_item (order_id, product_id) VALUES (2, 2)',
    ]

    try:
        cursor = connection.cursor()

        for q in queries:
            cursor.execute(q)
        
        connection.commit()

    except Exception as er:
        print(er)

def select_data():
    queries = [
        'SELECT * FROM users WHERE name = "John Doe";',
        'SELECT name, order_text FROM users INNER JOIN orders ON orders.user_id = users.id;',
    ]

    try:
        cursor = connection.cursor()

        for q in queries:
            cursor.execute(q)
            print(cursor.fetchall())
            print()

    except Exception as er:
        print(er)


if __name__ == '__main__':
    create_tables()
    # insert_data()
    select_data()

    connection.close()
