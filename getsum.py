def score(list):

    sum=0
    aces=0
    for i in range(len(list)):
        if list[i][0]=="J" or list[i][0]=="Q" or list[i][0]=="K":
            sum+=10
        elif list[i][0]=="A":
            sum+=11
            aces+=1
        else:
            sum+=list[i][0]
    if sum>21 and aces==0:
        return sum

    while aces>0:
        aces-=1
        sum-=10
        if sum<22:
            break
    return sum
