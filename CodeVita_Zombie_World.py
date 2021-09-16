

energy = []

K = int(input("Enter the no of test cases:"))

for i in range(0, K):
    N, T = map(int, input("Enter the number of zombies and time limit:").split())
    
    for j in range(0, N):
        energy.append(int(input()))
    
    P, D = map(int, input("Enter the initial player energy and required energy for next level:").split())
    
    optimal = sorted(energy)
    
    for k in range(0, len(optimal)):
        
        if T != 0:
            if optimal[k] <= P:
                P += (P - optimal[k])
                
            T -= 1
            
            
    if P >= D:
        print("Yes")
    else:
        print("No")
        
    energy = []
    
