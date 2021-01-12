lines_seen = set() # holds lines already seen

with open("symbollink.csv", "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i not in lines_seen:
            f.write(i)
            lines_seen.add(i)
    f.truncate()
