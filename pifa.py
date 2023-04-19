def pif(lst):
    if lst[2]**2 == (lst[0]**2) + (lst[1] ** 2):
        print('True')
    else:
        print('False')
lst = sorted([int(input()),int(input()),int(input())])
pif(lst)