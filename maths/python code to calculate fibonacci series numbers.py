


# get the number of terms from the user
n_terms = int(input("Enter the number of terms: "))

# initialize the first two terms
term1 = 0
term2 = 1

# print the first two terms
print(term1)
print(term2)

# generate the remaining terms
for i in range(2, n_terms):
    # calculate the next term
    next_term = term1 + term2

    # print the next term
    print(next_term)

    # update the values of the previous two terms
    term1 = term2
    term2 = next_term