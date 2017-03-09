from infininum import InfiniNum

my_num = InfiniNum(28, log=True)
my_num_2 = InfiniNum(12)

# should be 41
my_num.plus(my_num_2)

print(my_num)
