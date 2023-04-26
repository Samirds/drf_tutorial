# # # print("hi")


# ps = "Samir123"

# # # print(len(ps))

# # # print(str.__contains__("Hello from AskPython", "AskPython"))

# special_charecter = ["@", "&", "#", "$", "%", "_"]

# # if any(substring in ps for substring in special_charecter):
# #     # 👇️ this runs
# #     print('The string contains at least one element from the list')
# # else:
# #     print('The string does NOT contain any of the elements in the list')

# print(substring in ps)




# print(str.__contains__(ps, special_charecter))
# # for i in special_charecter:


# # # l = [4, 3, 2, 0]                              
# # # print(any(l))  
# # for i in ps:
# #     if i in special_charecter:
# #         print("exisrt")

# #     else:
# #         print("false")

# # [i for  i in ps ]


# my_str = 'one two three'

# my_list = ['a', 'two', 'c']

# if any(substring in my_str for substring in my_list):
#     # 👇️ this runs
#     print('The string contains at least one element from the list')
# else:
#     print('The string does NOT contain any of the elements in the list')




ps = "Samir@123"
special_charecter = ["@", "&", "#", "$", "%", "_"]

if (len(ps) >= 8 and  bool(any(i in ps for i in special_charecter))):
            
            print("haha")
else:
        print("holo na")