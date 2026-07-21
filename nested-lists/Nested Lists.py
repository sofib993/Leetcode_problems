if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    
    scores = sorted(set(record[1] for record in records))
    sec = scores[1]
    
    final = []
    for rec in records:
        if rec[1] == sec:
            final.append(rec[0])
    final.sort()
    for _ in final:
        print(_)
