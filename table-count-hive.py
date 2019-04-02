#!/usr/bin/env python
import pyhs2

with pyhs2.connect(host='localhost',
                   port=10000,
                   authMechanism="PLAIN",
                   user='aiden',
                   password='test',
                   database='default') as conn:
    with conn.cursor() as cur:
        #Show databases
        #print(cur.getDatabases())
        f = open("./result.data", 'w')
        f.write("database\ttable\tcount\n")
        for db in cur.getDatabases():
            print(db[0])
            cur.execute("use " + db[0])
            cur.execute("show tables")
            for table in cur.fetch():
                #print(table)
                cur.execute("select count(*) from " + table[0])
                count = cur.fetchone()
                data = "%s\t%s\t%s\n" % (db[0], table[0], count[0])
                f.write(data)

        f.close()
