# class A():
#     a = [0, 0]

#     def __init__(self):
#         self.b = [10, 10]

#     def func(self, change):
#         self.a[0] = change
#         self.b[0] = change

# a = A()
# b = A()
# b.func(1)
# print(a.a)
# print(a.b)

# def f(a, b):
#     def f1():
#         pass
#     a.append(f1)
#     b.append(f1)

# a = [0]
# b = [1]
# f(a, b)

# print(a[1] == b[1])
# print(f"{a[1]}\n{b[1]}")

def rem(l, num, length):
    new = []
    for i in range(length):
        if l[i] != num:
            new.append(l[i])
    return new

a = [0, 1, 2, 0, 3, 0, 0]
print(rem(a, 0, 7))
print(a)