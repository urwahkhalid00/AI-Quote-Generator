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
    
    
def save_favorite(quote, author, category):

    conn = sqlite3.connect("quotes.db")

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO favorites (quote, author, category)
        VALUES (?, ?, ?)
    """, (quote, author, category))

    conn.commit()

    conn.close() 
       
    
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
    
def quote_exists(quote):

    conn = sqlite3.connect("quotes.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT id
        FROM favorites
        WHERE quote = ?
    """, (quote,))

    result = cursor.fetchone()

    conn.close()

    return result

def search_favorites(search):

    conn = sqlite3.connect("quotes.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM favorites
        WHERE quote LIKE ?
        OR author LIKE ?
        OR category LIKE ?
    """, (f"%{search}%", f"%{search}%", f"%{search}%"))

    favorites = cursor.fetchall()

    conn.close()

    return favorites


def filter_favorites(search, category):

    conn = sqlite3.connect("quotes.db")

    cursor = conn.cursor()

    query = """
        SELECT * FROM favorites
        WHERE 1=1
    """

    values = []

    if search:

        query += """
            AND (
                quote LIKE ?
                OR author LIKE ?
            )
        """

        values.extend([
            f"%{search}%",
            f"%{search}%"
        ])

    if category and category != "all":

        query += " AND category = ?"

        values.append(category)

    cursor.execute(query, values)

    favorites = cursor.fetchall()

    conn.close()

    return favorites