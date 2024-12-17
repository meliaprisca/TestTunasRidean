
# Online Python - IDE, Editor, Compiler, Interpreter

m = 2

ai = [8, 9, 3, 2] 
bi = [5, 4, 1, 3]

My_list = [] 
  
# Value to begin and end with 
start, end = 1, 1000
  
# Check if start value is smaller than end value 
if start < end: 
    # unpack the result 
    My_list.extend(range(start, end)) 
    # Append the last value 
    My_list.append(end) 
  

test_a = []
for index, value in zip(range(len(ai)), zip(ai,bi)):
    test_a.append(value)
    
    # test_a.sort()
    # print(value)
print(test_a)
test_a.sort(key=lambda tup: tup[0])
print(test_a)
for a in test_a:
    if m >= a[0]:
        m += a[1]
    else:
        break
print(m)
        # if a >= ai:
        #     a += bi
