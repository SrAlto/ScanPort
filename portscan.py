import socket

print("""
+++++++++++++++++++++++++++++
+ SCRIPT FEITO POR SR. ALTO +
+                           +
+ https://github.com/SrAlto +
+++++++++++++++++++++++++++++                                                                                                                                                                                        
""")

ip = raw_input("Digite o ip do alvo: ")
for port in range(1,65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s.connect_ex((ip, port)) == 0:
        print "Porta ",port," Aberta"
        s.close()
        

