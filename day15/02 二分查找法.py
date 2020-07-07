'''
1,算法：二分查找，树运算，堆，栈....

'''
#前提，有序且唯一的数字数列
# l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
# print(l.index(66))
# count = 0
# for i in l:
#     if i == 66:
#         print(count)
#         break
#     count += 1


# ,1,aim 6
# 2,aim与list的中间的数进行比较mid，aim > mid  取mid --end 中间的数与aim在进行比较
# 3,aim与list的中间的数进行比较mid，aim < mid  取start --min 中间的数与aim在进行比较



# def two_search(li, aim):
#     mid_index = len(li) // 2  # 3
#     if li[mid_index] < aim:
#         return two_search(li[mid_index+1:],aim)
#     elif li[mid_index] > aim:
#         return two_search(li[:mid_index],aim)  #（[2,3,5],3）
#     elif li[mid_index] == aim:
#         return mid_index
#     else:
#         return '没有此值'
# print(two_search(l,17))
'''
1: aim 15, start:0 end:6 min_index:3 , li[min_index]:10
2: aim 15, start:4 end:6 min_index:5   li[min_index]:33
3, aim 15, start:4 end:4 min_index:4   li[min_index]:15
'''
l = [2, 3, 5, 10, 15, 33, 55]
def two_search(li, aim, start=0, end=None):
    end = len(li) if end is None else end
    mid_index = (end - start) // 2 + start  # 3
    if start <= end:
        if li[mid_index] < aim:
            return two_search(li, aim, start=mid_index+1, end=end)
        elif li[mid_index] > aim:
            return two_search(li, aim, start=start, end=mid_index-1)  #（[2,3,5],3）
        elif li[mid_index] == aim:
            return mid_index
        else:
            return '没有此值'
    else:
        return '没有此值'
print(two_search(l,100))