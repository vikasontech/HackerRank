#Function Description
#
#Complete the function minimumSwaps in the editor below. It must return an integer representing the minimum number of swaps to sort the array.
#
#minimumSwaps has the following parameter(s):
#
#arr: an unordered array of integers
#Input Format
#
#The first line contains an integer, , the size of .
#The second line contains  space-separated integers .
#
#source: https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen
#
#
def mini(arr):
    temp = [0] * (len(arr) + 1) 

    for pos, val in enumerate(arr):
        print(str(pos) + ','+str(val))

        temp[val] = pos

    swaps = 0 

    print('temp: '+ str(temp))
    print('arr:' + str(arr))

    for i in range (len(arr)):
        if arr[i] != i + 1:
            swaps += 1
            t = arr[i]
            arr[i] = i + 1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
            print('-----------------------')
            print('temp: '+ str(temp))
            print('arr:' + str(arr))
    return swaps

#-----------------------------
lst = [7,1,3,2,4,5,6]
lst = [4,3,1,2]
print(mini(lst))

