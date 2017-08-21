def area(s):
    ch=True
    for i in range(len(s)):
        for_s=(s[0]+s[1]+s[2])/2
        if for_s==s[0] or for_s==s[1] or for_s==s[2]or s[1]==0 or s[2]==0 or s[0]==0:
            ch=False
    return ch
#################################################
final_triangles=[]
size=int(input())
sides=[]
sums=[]
sum=0
allsides=[]
sums.append(input().strip().split(" "))
j=0
break_loop=False
for i in range(size):
    # print("i is",i)
    sums[0][i]=int(sums[0][i])
for i in range(size):
    sum=0
    sides_dict = []
    for j in range(i,i+3):
        # print("j currently is",j)
        if j==size:
            break_loop=True
            break
        # print("sums at [0][j]",sums[0][j])
        sides_dict.append(sums[0][j])
        sum=sum+sums[0][j]
        # print("sum is",sum)
    if break_loop==True:
        break
    sides.append(sum)               #sides has the perimeter
    allsides.append(sides_dict)              #all sides has all the different sides
final_perimeter=[]
for i in range(len(allsides)):
    result=area(allsides[i])                   #function applied
    if result==False:
        continue
    else:
        final_triangles.append(allsides[i])
        final_perimeter.append(sides[i])
print(final_triangles)
print(final_perimeter)
max=0
for i in range(len(final_perimeter)):
    if final_perimeter[i]>max:
        max=final_perimeter[i]
c=0
count_more=False
repeat=[]
for j in range(len(final_perimeter)):
    if final_perimeter[j]==max:
        repeat.append(final_triangles[j])
        c+=1
        if c>1:
            count_more=True
if count_more==True:
    max_side=[]
    min = 10 ** 10
    min_sides=[]
    max_side_var=0
    for i in range(len(repeat)):
        maximum=0
        min=10**10
        for j in range(len(repeat[i])):
            # print("repeat at i at j",repeat[i][j])
            if repeat[i][j]>maximum:
                maximum=repeat[i][j]
        for j in range(len(repeat[i])):
            if repeat[i][j]<min:
                min=repeat[i][j]
        min_sides.append(min)
        max_side.append(maximum)
    print(min_sides)
    print(max_side)
min_tri=[]
min_values_oftri=[]
count_min=0
if count_more==True:
    min_all=10**10
    max_all=0
    count_max=0
    max_tri=[]
    final_largest_traingle=[]
    for i in range(len(max_side)):
        if max_side[i]>max_all:
            max_all=max_side[i]
    for i in range(len(max_side)):
        if max_side[i]==max_all:
            count_max+=1
            print("repeat at max",repeat[i])
            print("count_max",count_max)
            max_tri.append(repeat[i])
        for j in range(len(max_tri)):
            for k in range(len(max_tri[j])):
                if max_tri[j][k]<min_all:
                    min_all=max_tri[j][k]
                min_values_oftri.append(min_all)
    for i in range(len(min_values_oftri)):
        if min_values_oftri[i]==min_all:
            count_min+=1
            if count_min>1:
                final_largest_traingle.append(repeat[i])
            else:
                final_largest_traingle.append(repeat[i])
    print(final_largest_traingle)








                    # max_all=max_side[i]
                    # index=i






# if count_more==True
#     max_after_max_side=0
#
#     for i in range(len(max_side)):
#         for j in range(len(max_side)):
#             if max_side[i]==max_side[j]:
#                 for
#








    # for i in range(len(max_side)):
    #     if max_side[i]>max_side_var:
    #         print("maxside[i]",max_side[i])
    #         max_side_var=max_side[i]
    #         print(max_side_var)



