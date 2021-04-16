import psycopg2
from datetime import datetime
import binascii
import _thread
import time
import socket

PORT1 = 8809
 
conn = psycopg2.connect(host="131.180.165.7",database="CRoF",user="postgres", password="crpg")


cursor = conn.cursor()

#Value id 75-83
cursor.execute('''SELECT value from objects WHERE id=75''')
result = cursor.fetchone()
record1 = result[0]
cursor.execute('''SELECT value from objects WHERE id=76''')
result = cursor.fetchone()
record2 = result[0]
cursor.execute('''SELECT value from objects WHERE id=77''')
result = cursor.fetchone()
record3 = result[0]
cursor.execute('''SELECT value from objects WHERE id=78''')
result = cursor.fetchone()
record4 = result[0]
cursor.execute('''SELECT value from objects WHERE id=79''')
result = cursor.fetchone()
record5 = result[0]
cursor.execute('''SELECT value from objects WHERE id=80''')
result = cursor.fetchone()
record6 = result[0]
cursor.execute('''SELECT value from objects WHERE id=81''')
result = cursor.fetchone()
record7 = result[0]
cursor.execute('''SELECT value from objects WHERE id=82''')
result = cursor.fetchone()
record8 = result[0]
cursor.execute('''SELECT value from objects WHERE id=83''')
result = cursor.fetchone()
record9 = result[0]


#Value code
cursor.execute('''SELECT code from objects WHERE id=75''')
result = cursor.fetchone()
r1 = result[0]
cursor.execute('''SELECT code from objects WHERE id=76''')
result = cursor.fetchone()
r2 = result[0]
cursor.execute('''SELECT code from objects WHERE id=77''')
result = cursor.fetchone()
r3 = result[0]
cursor.execute('''SELECT code from objects WHERE id=78''')
result = cursor.fetchone()
r4 = result[0]
cursor.execute('''SELECT code from objects WHERE id=79''')
result = cursor.fetchone()
r5 = result[0]
cursor.execute('''SELECT code from objects WHERE id=80''')
result = cursor.fetchone()
r6 = result[0]
cursor.execute('''SELECT code from objects WHERE id=81''')
result = cursor.fetchone()
r7 = result[0]
cursor.execute('''SELECT code from objects WHERE id=82''')
result = cursor.fetchone()
r8 = result[0]
cursor.execute('''SELECT code from objects WHERE id=83''')
result = cursor.fetchone()
r9 = result[0]


try:                   
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
        s1.bind(('',PORT1))
        s1.listen()
        conn1, addr = s1.accept()
        with conn1:
            print('Server 1 from:',addr)
            while True:
                a = 1
                while a < 6:
                    #Format: mu01_id+value
                    cursor.execute('''SELECT value from objects WHERE id=75''')
                    result = cursor.fetchone()
                    if record1 != result[0]:
                        print(result[0])
                        string = "mu01_"+str(r1)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record1 = result[0]

                    cursor.execute('''SELECT value from objects WHERE id=76''')
                    result = cursor.fetchone()
                    if record2 != result[0]:
                        print(result[0])
                        string = "mu02_"+str(r2)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record2 = result[0]

                    cursor.execute('''SELECT value from objects WHERE id=77''')
                    result = cursor.fetchone()
                    if record3 != result[0]:
                        print(result[0])
                        string = "mu03_"+str(r3)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record3 = result[0]
                            
                    cursor.execute('''SELECT value from objects WHERE id=78''')
                    result = cursor.fetchone()
                    if record4 != result[0]:
                        print(result[0])
                        string = "mu04_"+str(r4)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record4 = result[0]
                        
                    cursor.execute('''SELECT value from objects WHERE id=79''')
                    result = cursor.fetchone()
                    if record5 != result[0]:
                        print(result[0])
                        string = "mu05_"+str(r5)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record5 = result[0]
                            
                    cursor.execute('''SELECT value from objects WHERE id=80''')
                    result = cursor.fetchone()
                    if record6 != result[0]:
                        print(result[0])
                        string = "mu05_"+str(r6)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record6 = result[0]

                    cursor.execute('''SELECT value from objects WHERE id=81''')
                    result = cursor.fetchone()
                    if record7 != result[0]:
                        print(result[0])
                        string = "mu06_"+str(r7)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record7 = result[0]
                            
                    cursor.execute('''SELECT value from objects WHERE id=82''')
                    result = cursor.fetchone()
                    if record8 != result[0]:
                        print(result[0])
                        string = "mu07_"+str(r8)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record8 = result[0]
                    
                    cursor.execute('''SELECT value from objects WHERE id=83''')
                    result = cursor.fetchone()
                    if record9 != result[0]:
                        print(result[0])
                        string = "mu07_"+str(r9)+"+"+str(result[0])
                        datax = string.encode()
                        conn1.sendall(datax)
                        print(string)
                        record9 = result[0]

except:
   print ("Error: unable to start thread")
   conn.close()

while 1:
   pass

