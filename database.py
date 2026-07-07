import sqlite3


def create_database():

    conn = sqlite3.connect("quotes.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorites(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            quote TEXT NOT NULL,

            author TEXT NOT NULL,

            category TEXT NOT NULL

        )
    """)

    conn.commit()

    conn.close()
    
# def save_favorite(quote, author, category):

#     conn = sqlite3.connect("quotes.db")

#     cursor = conn.cursor()

#     cursor.execute("""
#         INSERT INTO favorites (quote, author, category)
#         VALUES (?, ?, ?)
#     """, (quote, author, category))

#     conn.commit()

#     conn.close()    
    
def get_favorites():

    conn = sqlite3.connect("quotes.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM favorites
    """)

    favorites = cursor.fetchall()

    conn.close()

    return favorites

def delete_favorite(id):

    conn = sqlite3.connect("quotes.db")

    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM favorites
        WHERE id = ?
    """, (id,))

    conn.commit()

    conn.close()