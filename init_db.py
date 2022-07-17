import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO tickets (ticket_number, ticket_status, ticket_agent, ticket_type, ticket_group, ticket_sla, ticket_url) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('11223344', 'Aberto', 'William', 'Customer Care Baixo',
             'Customer Care - YV', '25/07/2022 15:06:33', 'www.google.com')
            )

connection.commit()
connection.close()
