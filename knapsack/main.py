item_weights = [0,2,10,3,6,18]
item_values = [0,1,20,3,14,100]

n = len(item_weights)
W = 15 #Total capacity
K = [[0 for w in range(W+1)] for i in range(n)]

#Recureence
for i in range(1,n):
    for w in range(1, W + 1):
        wi = item_weights[i]
        vi = item_values[i]

    if wi <= w:
        K[i][w] = max([K[i-1][w -wi] + vi, K[i - 1][w]])
    else:
        K[i][w] = K[i - 1][w]

#RESUlTS
print("Result: ", K[n - 1][W])

