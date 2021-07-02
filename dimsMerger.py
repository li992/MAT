import csv,glob,os,shutil

directory_path = os.getcwd()

#gather all data and put them togather
def dimsIntegration(filename):
    print("dimsIntegration called")
    csvReads = csv.reader(open(filename),delimiter=' ',quotechar='|')
    
    rowCounts =0
    rowDict = {}
    nameField=[]

    for row in csvReads:
        #initiate name field
        if rowCounts==0:
            nameField = ','.join(row).split('\\')
            for i in range(0,len(nameField)):
                rowDict[nameField[i]]=0.0
        #process data one row by another
        if rowCounts!=0:
            dataField = ','.join(row).split('\\')
            for index in range(0,len(dataField)):
                originalData = rowDict.get(nameField[index])
                rowDict[nameField[index]] = originalData+float(dataField[index])
        rowCounts+=1
    
    #process the final data
    length = rowDict.get('length.length')
    for dictIndex in range(0,len(rowDict)):
        currData = rowDict.get(nameField[dictIndex])
        rowDict[nameField[dictIndex]] = currData/length

    return rowDict

    
def folderProcess():
    print('folderprocess called')
    if not os.path.exists('output'):
        print('Please use biber-dim to generate raw data first')
        return
    else:
        os.chdir(directory_path+'\output')
        filenames = glob.glob('*.txt')
        validnames =[]
        for name in filenames:
            if '_dims' in name:
                validnames.append(name)
        print(validnames)
        return validnames

#folder creation
if not os.path.exists('outputDims'):
    try:
        os.mkdir(directory_path+"/outputDims")
    except OSError:
        print("Directory creation failed")
    else:
        print("Successfully created the directory")
else:
    try:
        shutil.rmtree(directory_path+"/outputDims")
        os.mkdir(directory_path+"/outputDims")
    except OSError:
        print("Directory recreation failed")
    else:
        print("Successfully recreated the directory")

#process all files
files = folderProcess()
for file in files:
    fileData = dimsIntegration(directory_path+"/output/"+file)
    keys = fileData.keys()
    outfilename = file.replace('.txt','.csv')
    outfile = open(directory_path+'\\outputDims\\'+outfilename,'w')
    outfile.write('\\'.join([n for n in fileData.keys()]))
    outfile.write('\n')
    outfile.write('\\'.join(['%.5f' % fileData[d] for d in keys]))