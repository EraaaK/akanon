import sqlite3
from api import InboxAPI as function


def initDB():

    ticketList = function.GetTicketsByDepartment()
    connection = sqlite3.connect('database.db')

    with open('schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    for i in range(len(ticketList)):
        cur.execute("INSERT INTO tickets (ticket_number, ticket_status, ticket_agent, ticket_type, ticket_group, ticket_sla, ticket_url) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (
                        ticketList[i]['number'],
                        ticketList[i]['state']['name'],
                        ticketList[i]['responsible']['name'],
                        ticketList[i]['type']['name'],
                        ticketList[i]['group']['name'],
                        str(ticketList[i]['deadline']),
                        '-')
                    )

    connection.commit()
    connection.close()
