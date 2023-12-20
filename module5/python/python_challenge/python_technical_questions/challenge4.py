# Writing a well-documented code create a function that calculates simple interest.

def calculate_simple_interest(P, R, T):
    SI = P * R * T/100
    return SI


simple_interest = calculate_simple_interest(10000, 4, 5)

print(simple_interest)
