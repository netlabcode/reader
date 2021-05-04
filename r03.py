import psycopg2
from datetime import datetime
import binascii
import _thread
import time
import socket

PORT1 = 8803
 

def serverX():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
            s1.bind(('',PORT1))
            s1.listen()
            conn1, addr = s1.accept()
            with conn1:
                print('Server 1 from:',addr)

                conn = psycopg2.connect(host="131.180.165.7",database="CRoF",user="postgres", password="crpg")
                  
                cursor = conn.cursor()

                #Value id 16-24
                cursor.execute('''SELECT value from objects WHERE id=16''')
                result = cursor.fetchone()
                record1 = result[0]
                cursor.execute('''SELECT value from objects WHERE id=17''')
                result = cursor.fetchone()
                record2 = result[0]
                cursor.execute('''SELECT value from objects WHERE id=18''')
                result = cursor.fetchone()
                record3 = result[0]
                cursor.execute('''SELECT value from objects WHERE id=19''')
                result = cursor.fetchone()
                record4 = result[0]
                cursor.execute('''SELECT value from objects WHERE id=20''')
                result = cursor.fetchone()
                record5 = result[0]
                cursor.execute('''SELECT value from objects WHERE id=21''')
                result = cursor.fetchone()
                record6 = result[0]
                cursor.execute('''SELECT value from objects WHERE id=22''')
                result = cursor.fetchone()
                record7 = result[0]
                cursor.execute('''SELECT value from objects WHERE id=23''')
                result = cursor.fetchone()
                record8 = result[0]
                cursor.execute('''SELECT value from objects WHERE id=24''')
                result = cursor.fetchone()
                record9 = result[0]

                #Value code
                cursor.execute('''SELECT code from objects WHERE id=16''')
                result = cursor.fetchone()
                r1 = result[0]
                cursor.execute('''SELECT code from objects WHERE id=17''')
                result = cursor.fetchone()
                r2 = result[0]
                cursor.execute('''SELECT code from objects WHERE id=18''')
                result = cursor.fetchone()
                r3 = result[0]
                cursor.execute('''SELECT code from objects WHERE id=19''')
                result = cursor.fetchone()
                r4 = result[0]
                cursor.execute('''SELECT code from objects WHERE id=20''')
                result = cursor.fetchone()
                r5 = result[0]
                cursor.execute('''SELECT code from objects WHERE id=21''')
                result = cursor.fetchone()
                r6 = result[0]
                cursor.execute('''SELECT code from objects WHERE id=22''')
                result = cursor.fetchone()
                r7 = result[0]
                cursor.execute('''SELECT code from objects WHERE id=23''')
                result = cursor.fetchone()
                r8 = result[0]
                cursor.execute('''SELECT code from objects WHERE id=24''')
                result = cursor.fetchone()
                r9 = result[0]
                
                

                while True:
                    data = "a"
                    dataxy = data.encode()
                    try:
                        
                        #Format: mu01_id+value
                        cursor.execute('''SELECT value from objects WHERE id=16''')
                        result = cursor.fetchone()
                        if record1 != result[0]:
                            print(result[0])
                            string = "mu01_"+str(r1)+"+"+str(result[0])
                            datax = string.encode()
                            conn1.sendall(datax)
                            print(string)
                            record1 = result[0]

                        cursor.execute('''SELECT value from objects WHERE id=17''')
                        result = cursor.fetchone()
                        if record2 != result[0]:
                            print(result[0])
                            string = "mu02_"+str(r2)+"+"+str(result[0])
                            datax = string.encode()
                            conn1.sendall(datax)
                            print(string)
                            record2 = result[0]

                        cursor.execute('''SELECT value from objects WHERE id=18''')
                        result = cursor.fetchone()
                        if record3 != result[0]:
                            print(result[0])
                            string = "mu03_"+str(r3)+"+"+str(result[0])
                            datax = string.encode()
                            conn1.sendall(datax)
                            print(string)
                            record3 = result[0]
                                
                        cursor.execute('''SELECT value from objects WHERE id=19''')
                        result = cursor.fetchone()
                        if record4 != result[0]:
                            print(result[0])
                            string = "mu03_"+str(r4)+"+"+str(result[0])
                            datax = string.encode()
                            conn1.sendall(datax)
                            print(string)
                            record4 = result[0]
                            
                        cursor.execute('''SELECT value from objects WHERE id=20''')
                        result = cursor.fetchone()
                        if record5 != result[0]:
                            print(result[0])
                            string = "mu04_"+str(r5)+"+"+str(result[0])
                            datax = string.encode()
                            conn1.sendall(datax)
                            print(string)
                            record5 = result[0]
                                
                        cursor.execute('''SELECT value from objects WHERE id=21''')
                        result = cursor.fetchone()
                        if record6 != result[0]:
                            print(result[0])
                            string = "mu05_"+str(r6)+"+"+str(result[0])
                            datax = string.encode()
                            conn1.sendall(datax)
                            print(string)
                            record6 = result[0]

                        cursor.execute('''SELECT value from objects WHERE id=22''')
                        result = cursor.fetchone()
                        if record7 != result[0]:
                            print(result[0])
                            string = "mu06_"+str(r7)+"+"+str(result[0])
                            datax = string.encode()
                            conn1.sendall(datax)
                            print(string)
                            record7 = result[0]
                                
                        cursor.execute('''SELECT value from objects WHERE id=23''')
                        result = cursor.fetchone()
                        if record8 != result[0]:
                            print(result[0])
                            string = "mu06_"+str(r8)+"+"+str(result[0])
                            datax = string.encode()
                            conn1.sendall(datax)
                            print(string)
                            record8 = result[0]
                        
                        cursor.execute('''SELECT value from objects WHERE id=24''')
                        result = cursor.fetchone()
                        if record9 != result[0]:
                            print(result[0])
                            string = "mu06_"+str(r9)+"+"+str(result[0])
                            datax = string.encode()
                            conn1.sendall(datax)
                            print(string)
                            record9 = result[0]
                        


                        conn1.sendall(dataxy)
                        #print(record1)
                        time.sleep(1)
                        
                    except:
                        conn1.close()
                        conn.close()
                        print("Connection Close")
                        break
                
                conn1.close()
                print("Restart Server")
                conn.close()
                s1.close()
                time.sleep(1)
                serverX()

serverX()
            


