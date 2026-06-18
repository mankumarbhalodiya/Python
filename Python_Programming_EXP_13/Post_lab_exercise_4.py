with open("ict.txt", 'r') as f1, open("ict1.txt", 'r') as f2, open("merged.txt", 'w') as fout:
    fout.write(f1.read())
    fout.write("\n")
    fout.write(f2.read())