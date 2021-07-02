import csv, sys, getopt

def csvRead(filename):
    csvReads = csv.DictReader(open(filename))
    return csvReads

def typePercent(csvDictionary):
    totalArticle=0
    undefinedArticle=0
    typeDict = {
        'intimate interpersonal interaction':0,
        'informational interaction':0,
        'scientific exposition':0,
        'learned exposition':0,
        'imaginative narrative':0, 
        'general narrative exposition':0, 
        'situated reportage':0,
        'involved persuasion':0
    }
    for row in csvDictionary:
        NumberOfType = int(typeDict.get(row['Closest Text Type'].lower()))
        totalArticle+=1
        if NumberOfType!=None:
            typeDict.update({row['Closest Text Type'].lower(): NumberOfType+1})
        else:
            undefinedArticle+=1
    print("Intimate interpersonal interaction percentage:", float(typeDict.get('intimate interpersonal interaction')/totalArticle*100), "%\n")
    print("Informational interaction percentage:", float(typeDict.get('informational interaction')/totalArticle*100), "%\n")
    print("Scientific exposition percentage:", float(typeDict.get('scientific exposition')/totalArticle*100), "%\n")
    print("Learned exposition percentage:", float(typeDict.get('learned exposition')/totalArticle*100), "%\n")
    print("Imaginative narrative percentage:", float(typeDict.get('imaginative narrative')/totalArticle*100), "%\n")
    print("General narrative exposition percentage:", float(typeDict.get('general narrative exposition')/totalArticle*100), "%\n")
    print("Situated reportage percentage:", float(typeDict.get('situated reportage')/totalArticle*100), "%\n")
    print("Involved persuasion percentage:", float(typeDict.get('involved persuasion')/totalArticle*100), "%\n")
    print("Undefined article percentage:", float(undefinedArticle/totalArticle*100), "%\n")
    return

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt=='-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i","--ifile"):
            inputfile = arg
        elif opt in ("-o","--ofile"):
            outputfile = arg
    print ("Input file is ",inputfile)
    print ("Output file is", outputfile)
    if(inputfile!=''):
        data = csvRead(inputfile)
        typePercent(data)
    else:
        print("File not found")
    return

if __name__ == "__main__":
    main(sys.argv[1:])