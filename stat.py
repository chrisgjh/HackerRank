#from statistics import mode

#============================
def mode(array):
    most = max(list(map(array.count, array)))
    return list(set(filter(lambda x: array.count(x) == most, array)))
#============================ find multiple mode and put them in a list

count = int(input())
num_arr = input().split(' ')
dic = dict()
for i in range(0, len(num_arr)):
    num_arr[i] = int(num_arr[i])
    if (num_arr[i]) in dic:
        dic[num_arr[i]] += 1
    else:
        dic[num_arr[i]] = 1
num_arr = sorted(num_arr)
mean = sum(num_arr)/len(num_arr)

if (len(num_arr) % 2 == 0):
    median = (num_arr[len(num_arr)//2-1] + num_arr[(len(num_arr)//2)]) / 2
else:
    median = num_arr[len(num_arr)//2-1]
if max(dic.values()) == 1 and len(dic)==count:
    mode1 = min(dic)
else:
    mode1 = min(mode(num_arr))

print("{:.1f}".format(mean))
print(median)
print(mode1)