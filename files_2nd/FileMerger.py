import csv,glob,os,shutil

def csvRead(filename):
    csvReads = csv.reader(open(filename), delimiter=' ', quotechar='|')
    return csvReads

def csvRowProcess(csvDictionary):
    #fileNames =[]
    if os.path.isdir('output')==False:
        print('break1')
        try:
            os.mkdir(os.getcwd()+"/output")
        except OSError:
            print("Directory creation failed")
        else:
            print("Successfully created the directory")
    else:
        try:
            shutil.rmtree(os.getcwd()+"/output")
            os.mkdir(os.getcwd()+"/output")
        except OSError:
            print("Directory recreation failed")
        else:
            print("Successfully recreated the directory")

    print('break2')
    rowCounts=0
    for row in csvDictionary:
        rowValue = ','.join(row)
        rowField = rowValue.split(";")
        if rowCounts!=0:
            fileName = rowField[7]+".txt"
            fileSpliter = rowField[7].split('_')
            outfile = open(os.getcwd()+'/output/'+fileSpliter[0]+'_'+rowField[1]+'_'+rowField[5].replace("-","")+'.txt','a')
            filePath = find(fileName)
            if filePath!='':
                with open(filePath) as infile:
                    for line in infile:
                        outfile.write(line)
                infile.close()
            outfile.close()
            rowCounts+=1
            print("File merging:"+rowField[7]+"; CSV Index:"+str(rowCounts))
            #fileNames.extend(rowField[8])
        else:
            rowCounts+=1
    return

def find(text):
    path = glob.glob('**/'+text,recursive=True)
    if len(path)==1:
        return path[0]
    else:
        return ''

csvDict = csvRead(os.getcwd()+'\\files_2nd\##Final.csv')
print('break0')
csvRowProcess(csvDict)
