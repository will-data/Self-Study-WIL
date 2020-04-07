m, n = map(int, input().split())
magazine = input().split()
ransom = input().split()


# My original solutoin. It works but takes too much time
# def ransom_note(magazine, ransom):
#    answer = True
#    for word in ransom:
#        if word in magazine:
#            magazine.remove(word)
#        else:
#            answer = False
#            break
#    return(answer)

# Therefore, use dictionary to count items and used the counted dict
def ransom_note(magazine, ransom):
    word_cnt = {};
    ransom_cnt = {}
    for word in magazine:
        if (word in word_cnt):
            word_cnt[word] += 1
        else:
            word_cnt[word] = 1
    answer = True
    for word in ransom:
        if (word in word_cnt):
            if word_cnt[word] > 0:
                word_cnt[word] -= 1
            else:
                answer = False;
                break
        else:
            answer = False;
            break
    return (answer)


print('Yes' if ransom_note(magazine, ransom) else 'No')

