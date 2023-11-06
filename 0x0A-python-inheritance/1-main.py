#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()

my_list.append(float('inf'))
my_list.append('nan')
my_list.append(8)
my_list.append(-6)

print(my_list)
my_list.print_sorted()
print(my_list)
