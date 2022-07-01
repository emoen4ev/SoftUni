#  ------ original ----------------

# x = "global"
#
# def outer():
#     x = "local"
#
#     def inner():
#         x = "nonlocal"
#         print("inner:", x)
#
#     def change_global():
#         x = "global: changed!"
#
#     print("outer:", x)
#     inner()
#     print("outer:", x)
#     change_global()
#
# print(x)
# outer()
# print(x)

# ---------------------------------------------


x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)

'''
global
outer: local
inner: nonlocal
outer: nonlocal
global: changed!
'''


# def get_print_list_func(separator_char):
#     def internal_print(ll):
#         print(separator_char.join(str(x) for x in ll))
#
#     return internal_print
#
# print_list = get_print_list_func('; ')
#
# print_list([1, 2, 3])