# google sheet regex match
if __name__ == '__main__':
    for i in range(2, 1100):
        print("=IF(REGEXMATCH(Sheet4!A1, \"\\b\" & B" + str(i) + " & \"\\b\"), \"✓\", \"x\")")
