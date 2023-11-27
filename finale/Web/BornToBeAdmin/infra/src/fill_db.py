import sqlite3
from hashlib import sha256
import random
import names

# Function to create the database tables
def create_tables():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL,
            is_admin BOOLEAN NOT NULL DEFAULT 0
        )
    ''')

    # Create data table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Function to fill the users table with random data
def fill_users_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Generate and insert random user data
    for _ in range(10):
        username = names.get_full_name()
        password = sha256(str(random.randint(1, 1000000)).encode()).hexdigest()
        is_admin = False

        cursor.execute('INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)', (username, password, is_admin))
    cursor.execute('INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)', ("redpanda-master", sha256("redpandas4ever".encode()).hexdigest(), True))
    for _ in range(72):
        username = names.get_full_name()
        password = sha256(str(random.randint(1, 1000000)).encode()).hexdigest()
        is_admin = False

        cursor.execute('INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)', (username, password, is_admin))
    conn.commit()
    conn.close()

# Function to fill the data table with British puns
def fill_data_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # British puns
    puns = ["Born to be mild", "Born to be wild", "Born to be a star", "Born to be free",
            "Born to be a legend", "Born to be awesome", "Born to be a hero",
            "Born to stand out", "Born to shine", "Born to be extraordinary",
            "Born to be remarkable", "Born to be unique", "Born to be great",
            "Born to be fabulous", "Born to be fantastic", "Born to be incredible",
            "Born to be phenomenal", "Born to be outstanding", "Born to be spectacular",
            "Born to be legendary", "Born to be iconic", "Born to be a king",
            "Born to be a queen", "Born to be a princess", "Born to be a prince",
            "Born to be royalty", "Born to be majestic", "Born to be regal",
            "Born to be noble", "Born to be grand", "Born to be splendid",
            "Born to be majestic", "Born to be opulent", "Born to be sumptuous",
            "Born to be lavish", "Born to be luxurious", "Born to be grandiose",
            "Born to be palatial", "Born to be dignified", "Born to be stately",
            "Born to be elegant", "Born to be graceful", "Born to be sophisticated",
            "Born to be polished", "Born to be refined", "Born to be cultured",
            "Born to be tasteful"]
    # Red panda facts
    red_panda_facts = [
    "Red pandas are also known as lesser pandas.",
    "Red pandas are not closely related to giant pandas.",
    "Red pandas were discovered about 50 years before giant pandas.",
    "Red pandas are native to the eastern Himalayas and southwestern China.",
    "Their scientific name is Ailurus fulgens.",
    "Red pandas are solitary animals, except during the mating season.",
    "They have a reddish-brown fur coat, a masked face, and a bushy ringed tail.",
    "Red pandas have a unique extension on their wrist called a 'false thumb' that helps them grip bamboo.",
    "Their diet consists mainly of bamboo leaves, but they also eat fruits, berries, acorns, and insects.",
    "Red pandas are excellent climbers and spend much of their time in trees.",
    "They have a slow metabolism and can spend up to 13 hours a day sleeping.",
    "Red pandas are crepuscular, meaning they are most active during dawn and dusk.",
    "The gestation period for red pandas is about 112 to 158 days.",
    "Red pandas usually give birth to one to four cubs, with twins being the most common.",
    "Newborn red panda cubs are blind and completely dependent on their mothers for the first few months.",
    "Red panda cubs stay in the nest for about 90 days before venturing out on their own.",
    "Their average lifespan in the wild is around 8 to 10 years.",
    "Red pandas communicate using various vocalizations, including squeaks, twitters, and huff-quacks.",
    "They have a keen sense of smell, and scent marking is an essential part of their communication.",
    "Red pandas have a special adaptation on their tongue that helps them grip bamboo leaves and remove any dirt.",
    "Red pandas have retractable claws, similar to a cat's, which help them climb trees.",
    "They are listed as endangered due to habitat loss and poaching.",
    "Efforts are being made to conserve red pandas through breeding programs and protected areas.",
    "Red pandas have a natural predator in the wild, which includes snow leopards and martens.",
    "Their fur on the soles of their feet helps them stay warm and provides a better grip on tree branches.",
    "Red pandas are skilled swimmers and are known to paddle in streams and rivers.",
    "They are also known by the nickname 'fire fox' because of their reddish fur.",
    "Red pandas have a 'bark' vocalization that sounds like a dog's bark, used as an alarm call.",
    "In Chinese, red pandas are called 'hun-ho,' which means fire fox."
    ]

    # Insert puns into the data table
    for pun in puns:
        cursor.execute('INSERT INTO data (content) VALUES (?)', (pun,))
    # Insert red pandas fun facts into the data table
    for fact in red_panda_facts:
        cursor.execute('INSERT INTO data (content) VALUES (?)', (fact,))

    conn.commit()
    conn.close()

# Main function to create and fill the database
def main():
    create_tables()
    fill_users_table()
    fill_data_table()

if __name__ == '__main__':
    main()
