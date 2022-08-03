#
# def fibonacci(n):
#     list = []
#     if n == 1:
#         list.append(1)
#     elif n == 2:
#         list.append(1)
#         list.append(1)
#     else:
#         list.append(1)
#         list.append(1)
#         for i in range(1, n+1):
#             a = list[-1]
#             b = list[-2]
#             list.append(a+b)
#     return list[n-1]
#
# print(fibonacci(6))
#
# def fibonacci(n):
#     int1 = 1
#     int2 = 1
#     for i in range(2, n+1):
#         int_result = int1+int2
#         int1 = int2
#         int2 = int_result
#     return int2
#
# print(fibonacci(7))
#
#
# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print(fibonacci(3))