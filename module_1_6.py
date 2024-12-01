#Работа со словарями
print('Работа со словарями')
my_dict = {'September': 9, 'October': 10, 'November': 11}
print(my_dict)
print(my_dict['September'])
# print (my_dict.get('September'))
print(my_dict.get('December'))
my_dict.update({'January': 1, 'February':2})
a=my_dict.pop('October')
print(a)
print(my_dict)
#Работа с множествами
print(' ')
print('Работа с множествами')
my_set = {1,1,2,3,5,2,5,3,5,8, 'September', 'September', (8,9,0)}
print(my_set)
my_set.update({(6,4,7),'October'})
print(my_set)
print(my_set.discard('September'))
print(my_set)
