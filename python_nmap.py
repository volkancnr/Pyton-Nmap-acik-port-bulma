import socket
import pyfiglet

volky = pyfiglet.figlet_format("VOLKY")
nmap=pyfiglet.figlet_format("Nmap For Python")
print("*"*58)


print(volky)
print(nmap)
print("*"*58)


print("*"*58)
while True:  
    print("_"*58)
    
    print("(1)Port Check \n(2)Port Scan \n(3)Exit")
    s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)

    opt=int(input("Option--> "))
    if opt==1:
        site=input("*Website or Ip(site.com)--> ")
        port=int(input("PORT--> "))
        try:
            s.connect((site,port))
            print("{✓}PORT OPEN--",str(port))
        except:
            print("{X}PORT CLOSE--",str(port))
    elif opt==2:
        site=input("*Website or Ip(site.com)--> ")
        min=int(input(" Minimum PORT--> "))
        max=int(input(" Maximum PORT--> "))
        for port in range (min,max+1):
            try:
                s.connect((site,port))
                print("{✓ }PORT OPEN--",str(port))
                
            except:
                print("{X}PORT CLOSE--",str(port))
        
    elif opt==3:
        print("Exiting...")
        break
    else:
        print("Error...\n[WRONG OPTİON!!!!!!]\nSelect Again... ")
        