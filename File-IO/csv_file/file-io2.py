with open('File-IO\\csv_file\\book.csv') as f :  
    rows = f.readlines()  
    isFirstLine = True
    for r in rows :  
        if isFirstLine :
            isFirstLine = False  
            continue
        cols = r.split(',')
        print('Student Name = ', cols[0], end=" ")  
        print('\t subject = ', cols[1], end=" ")  
        print('\t marks = \t', cols[2])