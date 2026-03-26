num=int(input("enter number :"))

sum_num=0

for i in range(1,num+1):
    if i % 2 ==0 :
        sum_num += i

print(f"the sum of even numbers is:{sum_num}")       

