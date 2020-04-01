T = int(input())
for i in range(T):
    S = str(input())
    # My original code
    # S_even = ""
    # S_odd = ""
    # for j in range(len(S)):
    #     if j%2 == 0:
    #         S_even += S[j]
    #     else:
    #         S_odd += S[j]

    # print(S_even,S_odd)

    # Better code with extended slice
    ## Can get detailed info in below link
    ## https://docs.python.org/release/2.3.5/whatsnew/section-slices.html
    print(S[::2], S[1::2])

