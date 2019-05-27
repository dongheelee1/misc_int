'''
could possibly do better with other algorithms...this is probably the worst way to sort something (bubble sort), find a better way 
'''
def sort_names(names):

    for i in range(len(names)):

        for j in range(len(names) - i - 1):

            if names[j] > names[j+1]:
                #swap

                names[j], names[j+1] = names[j+1], names[j]

    print(names)
