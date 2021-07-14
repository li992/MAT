import csv,glob,os,shutil,argparse

def csvRead(filename):
    csvReads = csv.reader(open(filename), delimiter=' ', quotechar='|')
    return csvReads

def csvRowProcess(csvDictionary):
    #fileNames =[]
    if not os.path.exists('MergedFiles'):
        try:
            os.mkdir(os.path.join(os.getcwd(),'MergedFiles'))
        except OSError:
            print("Directory creation failed")
        else:
            print("Successfully created the directory")
    else:
        try:
            shutil.rmtree(os.path.join(os.getcwd(),'MergedFiles'))
            os.mkdir(os.path.join(os.getcwd(),'MergedFiles'))
        except OSError:
            print("Directory recreation failed")
        else:
            print("Successfully recreated the directory")

    rowCounts=0
    for row in csvDictionary:
        rowValue = ','.join(row)
        rowField = rowValue.split(";")
        if rowCounts!=0:
            fileName = rowField[7]+".txt"
            fileSpliter = rowField[7].split('_')
            outfilestr = os.path.join(os.getcwd(),'MergedFiles')
            tempstr = fileSpliter[0]+'_'+rowField[1]+'_'+rowField[5].replace("-","")+'.txt'
            outfilestr = os.path.join(outfilestr,tempstr)
            outfile = open(outfilestr,'a')
            filePath = find(fileName)
            if filePath!='':
                with open(filePath) as infile:
                    for line in infile:
                        outfile.write(line)
                infile.close()
            outfile.close()
            rowCounts+=1
            print("File merging:"+rowField[7]+"; CSV Index:"+str(rowCounts))
        else:
            rowCounts+=1
    return

def find(text):
    path = glob.glob('**/'+text,recursive=True)
    if len(path)==1:
        return path[0]
    else:
        return ''

path = os.getcwd()
outpath = os.getcwd()
parser = argparse.ArgumentParser(description="Text file merger")
parser.add_argument('-p','--path',type=str,default=os.getcwd(),help='To define where the seperated text files are, it has to be the root of all flies and contains a #final.csv file')

args = parser.parse_args()
if args.path != os.getcwd():
    path = args.path
    path = os.path.join(path,'##Final.csv')
else:
    path = os.path.join(path,'files_2nd/##Final.csv')

csvDict = csvRead(path)
csvRowProcess(csvDict)
