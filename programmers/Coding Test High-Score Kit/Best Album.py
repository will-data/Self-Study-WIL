def solution(genres, plays):
    genreCnt = {}; genreList = {}; answer = []
    for i, (genre,play) in enumerate(zip(genres, plays)):
        if genre in genreCnt:
            genreCnt[genre] += play
            genreList[genre].append((i,play))
        else:
            genreCnt[genre] = play
            genreList[genre] = [(i,play)]

    for genre in sorted(genreCnt, key=genreCnt.get, reverse=True):
        if len(genreList[genre]) >= 2:
            topMusics = sorted(genreList[genre], key = lambda k: k[1], reverse = True)
            answer += topMusics[0][0],topMusics[1][0]
        else:
            answer.append(genreList[genre][0][0])
    return(answer)