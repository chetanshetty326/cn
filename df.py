P=int(input("Enter the prime number:"))
G=int(input("Enter the primitive root:"))
a=int(input("Enter Alice prvate key:"))
b=int(input("Enter Bob private key:"))
x=int(pow(G,a,P))
y=int(pow(G,b,P))
ka=int(pow(y,a,P))
kb=int(pow(x,b,P))
print("Public key of Alice is:",x)
print("Public key of Bob is:",y)
print("Secret key for the Alice is:",ka)
print("Secret Key for the Bob is:",kb)