# Arithmetic Operators

x = 2
y = 7

total = x + y
print(total)

total = x - y
print(total)

total = x * y
print(total)

total = y/x
print(total)

total = y % x
print(total)

total = y**x
print(total)

#Comparison Oper

a = 30
b = 60

out = (a < b)
print(out)

out = (a > b)
print(out)

out = (a == b)
print(out)

out = (a != b)
print(out)

out = (a <= b)
print(out)

out = (a >= b)
print(out)

# Assigment Oper

c = 0
d = 1

#c+=d # c = c+d

print(c)

c-=d
print(c)

#Logical Oper

a = 40
b = 60
x = 2
y = 3

out = (a < b) or (x > y)
print(out)

out = (a > b) or (x < y)
print(out)

out = (a > b) or (x > y)
print(out)

out = (a > b) and (x < y)
print(out)

out = (a < b) and (x < y)
print(out)

out = not(a < b)
print(out)

#Membership Oper

second_list = ("str1", "DevOps", 47, "num1", 1.5)
ans = "DevOps" in second_list
print(ans)

ans = "DevOps" not in second_list
print(ans)

ans = 47 not in second_list
print(ans)

# Identity Oper

a = 12
b = 15

result = 1 is b
print(result)

result = 1 is not b
print(result)

