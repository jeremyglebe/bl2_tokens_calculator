from math import pow, log10
choice = input("Choose\n[1] BA Rank -> BA Tokens\n[2] BA Tokens -> BA Rank\n")
choice = int(choice)
if choice <= 1:
    ba_rank = int(input("Enter Your Badass Rank: "))
    ba_tokens = round(pow(10, (log10(ba_rank) / 1.8)))
    print("Rank: {0}, Tokens: {1}".format(ba_rank, ba_tokens))
else:
    ba_tokens = int(input("Enter Your # of Badass Tokens: "))
    ba_rank = round(pow(ba_tokens, 1.8))
    print("Rank: {0}, Tokens: {1}".format(ba_rank, ba_tokens))