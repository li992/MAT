import csv,glob,os,shutil,argparse

def csvRead(filename):
    csvReads = csv.reader(open(filename), delimiter=' ', quotechar='|')
    return csvReads

def csvRowProcess(csvDictionary):
    # exist file check
    currIndex = 0
    if os.path.exists('MergedIndex.txt'):
        indexReaderPath = os.path.join(os.getcwd(),"MergedIndex.txt")
        indexReader = open(indexReaderPath,'r')
        currIndex = indexReader.readline()
        currIndex.replace('\n','')

    print("Coverd Lines:"+ str(int(currIndex)+1))

    # merger algo
    rowCounts=0
    for row in csvDictionary:
        if rowCounts<=int(currIndex):
            rowCounts+=1
            continue
        else:
            # record last processed index
            indexOutPath = os.path.join(os.getcwd(),"MergedIndex.txt")
            indexOut = open(indexOutPath,'w')
            indexOut.write(str(rowCounts))
            indexOut.close()

            rowValue = ','.join(row)
            rowField = rowValue.split(";")

            # processing target
            fileName = rowField[7]+".txt"
            fileSpliter = rowField[7].split('_')

            # each fragment path
            fragFileName = fileSpliter[0]+'_'+rowField[1]+'_'+rowField[5].replace("-","")+'_'+rowField[10].replace("_","#")
            fragFolderPath = os.path.join(os.getcwd(),'FileFragments')
            fragFolderPath = os.path.join(fragFolderPath,fragFileName)

            # merger path    
            outFileName = fileSpliter[0]+'_'+rowField[1]+'_'+rowField[5].replace("-","")+'.txt'
            outFolderPath = os.path.join(os.getcwd(),'MergedFiles')          
            outFolderPath = os.path.join(outFolderPath,outFileName)

            # record
            outfile = open(outFolderPath,'a')
            fragfile = open(fragFolderPath,'w')
            filePath = find(fileName)
            if filePath!='':
                with open(filePath) as infile:
                    for line in infile:
                        outfile.write(line)
                        fragfile.write(line)
                infile.close()
            outfile.close()
            rowCounts+=1
            print("File merging:"+rowField[7]+"; CSV Index:"+str(rowCounts))
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
parser.add_argument('-r','--restart',type=str,default="false",help='To restart the merging process, set value to true; to continue the process with existing index, set value to false')

# initialize folders
if not os.path.exists('MergedFiles'):
    try:
        os.mkdir(os.path.join(os.getcwd(),'MergedFiles'))
    except OSError:
        print("MergedFiles creation failed")
    else:
        print("Successfully created MergedFiles")
if not os.path.exists('FileFragments'):
    try:
        os.mkdir(os.path.join(os.getcwd(),'FileFragments'))
    except OSError:
        print("FileFragments creation failed")
    else:
        print("Successfully created FileFragments")

#argument passing
args = parser.parse_args()
if args.path != os.getcwd():
    path = args.path
    path = os.path.join(path,'##Final.csv')
else:
    path = os.path.join(path,'files_2nd/##Final.csv')

if args.restart == "true":
    print("Restart statement: true")
    if os.path.exists('MergedFiles'):
        shutil.rmtree(os.path.join(os.getcwd(),"MergedFiles"))
        try:
            os.mkdir(os.path.join(os.getcwd(),'MergedFiles'))
        except OSError:
            print("MergedFiles recreation failed")
        else:
            print("Successfully recreated MergedFiles")
    if os.path.exists('FileFragments'):
        shutil.rmtree(os.path.join(os.getcwd(),"FileFragments"))
        try:
            os.mkdir(os.path.join(os.getcwd(),'FileFragments'))
        except OSError:
            print("FileFragments recreation failed")
        else:
            print("Successfully recreated FileFragments")
    if os.path.exists('MergedIndex.txt'):
        os.remove(os.path.join(os.getcwd(),"MergedIndex.txt"))
else:
    print("Restart statement: false")
    

csvDict = csvRead(path)
csvRowProcess(csvDict)
