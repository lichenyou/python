
 
if __name__=="__main__":  
        import socket    
        print "Server is starting"  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        sock.bind(('localhost', 8001))   
        sock.listen(5) 
        print "Server is listenting port 8001, with max connection 5"   
        while True:   
                  
                connection,address = sock.accept()    
                try:    
                        i = 1
                        connection.settimeout(50)   
                        while True:
                            i = i +1
                            if i < 5 :
                                connection.send('welcome to server!')
                            else :
                                break
                                # buf = connection.recv(1024)    
                                # print "Get value " +buf  
                                # if buf == '1':    
                                #     print "send welcome"  
                                #     connection.send('welcome to server!')    
                                # elif buf!='0':    
                                #     connection.send('please go out!')   
                                #     print "send refuse"  
                                # else:   
                                #     print "close"  
                                #     break   
                except socket.timeout: 
                  print 'time out'  
  
                print "closing one connection" 
                connection.close()    
