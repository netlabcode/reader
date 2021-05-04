import psycopg2
from datetime import datetime
import binascii
import _thread
import time
import socket

PORT1 = 8801
 

def serverX():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
            s1.bind(('',PORT1))
            s1.listen()
            conn1, addr = s1.accept()
            with conn1:
                print('Server 1 from:',addr)

                conn = psycopg2.connect(host="131.180.165.7",database="CRoF",user="postgres", password="crpg")
                  
                cursor = conn.cursor()
                
                

                while True:
                    data = "a"
                    dataxy = data.encode()
                    try:
                        
                        #Format: mu01_id+value
                        


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
            


