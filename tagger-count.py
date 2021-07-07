import nltk,numpy,csv,glob,os,shutil

directory_path = os.getcwd()

def folderProcess():
    #print('folderprocess called')
    if not os.path.exists('Results'):
        print('Please use tagger-algo to generate raw data first')
        return []
    else:
        os.chdir(os.path.join(os.getcwd(),'Results'))
        os.chdir(os.path.join(os.getcwd(),'ModifiedTags'))
        filenames = glob.glob('*.txt')
        validnames =[]
        for name in filenames:
            validnames.append(name)
        #print(validnames)
        return validnames


def taggerCount(data,filename):
    tag_dict = {
            'Tokens':0.0,
            'AWL':0.0,
            'AMP':0.0,
            'ANDC':0.0,
            'BEMA':0.0,
            'BYPA':0.0,
            'CAUS':0.0,
            'CONC':0.0,
            'COND':0.0,
            'CONJ':0.0,
            'CONT':0.0,
            'DEMO':0.0,
            'DEMP':0.0,
            'DPAR':0.0,
            'DWNT':0.0,
            'EMPH':0.0,
            'EX':0.0,
            'FPP1':0.0,
            'GER':0.0,
            'HDG':0.0,
            'INPR':0.0,
            'JJ':0.0,
            'NEMD':0.0,
            'NN':0.0,
            'NOMZ':0.0,
            'OSUB':0.0,
            'PASS':0.0,
            'PASTP':0.0,
            'PEAS':0.0,
            'PHC':0.0,
            'PIN':0.0,
            'PIRE':0.0,
            'PIT':0.0,
            'PLACE':0.0,
            'POMD':0.0,
            'PRED':0.0,
            'PRESP':0.0,
            'PRIV':0.0,
            'PRMD':0.0,
            'PROD':0.0,
            'PUBV':0.0,
            'RB':0.0,
            'SERE':0.0,
            'SMP':0.0,
            'SPAU':0.0,
            'SPIN':0.0,
            'SPP2':0.0,
            'STPR':0.0,
            'SUAV':0.0,
            'SYNE':0.0,
            'THAC':0.0,
            'THATD':0.0,
            'THVC':0.0,
            'TIME':0.0,
            'TO':0.0,
            'TOBJ':0.0,
            'TPP3':0.0,
            'TSUB':0.0,
            'VBD':0.0,
            'VPRT':0.0,
            'WHCL':0.0,
            'WHOBJ':0.0,
            'WHQU':0.0,
            'WHSUB':0.0,
            'WZPAST':0.0,
            'WZPRES':0.0,
            'XX0':0.0}
    total_word_length=0
    total_tokens=0
    for line in data:
        word = line.replace('\n','').split('_')
        for fragIndex in range(len(word)):
            if fragIndex==0:
                total_word_length += len(word[fragIndex]) 
            else:
                if(tag_dict.get(word[fragIndex])!= None):
                    tag_dict[word[fragIndex]] = tag_dict.get(word[fragIndex])+1
        total_tokens+=1
    tag_dict['Tokens'] = total_tokens
    tag_dict['AWL'] = float(total_word_length/total_tokens)

    for i in tag_dict.keys():
        if i != "Tokens" and i != "AWL":
            tag_dict[i] = float(tag_dict.get(i))/total_tokens * 100

    OutputFilePath = os.path.join(directory_path,"Results/FieldScore")
    OutputFilePath = os.path.join(OutputFilePath,filename)
    OutputFilePath=OutputFilePath.replace('txt','csv')
    with open (OutputFilePath,'w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow([a for a in tag_dict.keys()])
        writer.writerow(['%.2f' % float(tag_dict.get(index)) for index in tag_dict.keys()])
        file.close()
    return tag_dict

def dimensionsCal(tag_dict,filename):
    biber_means ={"VBD" : 4.01, "PEAS" : 0.86, "VPRT" : 7.77, "PLACE" : 0.31, "TIME" : 0.52, "FPP1" : 2.72, "SPP2" : 0.99, "TPP3" : 2.99, "PIT" : 1.03, "DEMP" : 0.46, "INPR" : 0.14, "PROD" : 0.30, "WHQU" : 0.02, "NOMZ" : 1.99, "GER" : 0.7, "NN" : 18.05, "PASS" : 0.96, "BYPA" : 0.08, "BEMA" : 2.83, "EX" : 0.22, "THVC" : 0.33, "THAC" : 0.03, "WHCL" : 0.06, "TO" : 1.49, "PRESP" : 0.1, "PASTP" : 0.01, "WZPAST" : 0.25, "WZPRES" : 0.16, "TSUB" : 0.04, "TOBJ" : 0.08, "WHSUB" : 0.21, "WHOBJ" : 0.14, "PIRE" : 0.07, "SERE" : 0.01, "CAUS" : 0.11, "CONC" : 0.05, "COND" : 0.25, "OSUB" : 0.1, "PIN" : 11.05, "JJ" : 6.07, "PRED" : 0.47, "RB" : 6.56, "TTR" : 51.1, "AWL" : 4.5, "CONJ" : 0.12, "DWNT" : 0.2, "HDG" : 0.06, "AMP" : 0.27, "EMPH" : 0.63, "DPAR" : 0.12, "DEMO" : 0.99, "POMD" : 0.58, "NEMD" : 0.21, "PRMD" : 0.56, "PUBV" : 0.77, "PRIV" : 1.80, "SUAV" : 0.29, "SMP" : 0.08, "CONT" : 1.35, "THATD" : 0.31, "STPR" : 0.2, "SPIN" : 0, "SPAU" : 0.55, "PHC" : 0.34, "ANDC" : 0.45, "SYNE" : 0.17, "XX0" : 0.85}
    biber_sds ={"VBD" : 3.04, "PEAS" : 0.52, "VPRT" : 3.43, "PLACE" : 0.34, "TIME" : 0.35, "FPP1" : 2.61, "SPP2" : 1.38, "TPP3" : 2.25, "PIT" : 0.71, "DEMP" : 0.48, "INPR" : 0.20, "PROD" : 0.35, "WHQU" : 0.06, "NOMZ" : 1.44, "GER" : 0.38, "NN" : 3.56, "PASS" : 0.66, "BYPA" : 0.13, "BEMA" : 0.95, "EX" : 0.18, "THVC" : 0.29, "THAC" : 0.06, "WHCL" : 0.1, "TO" : 0.56, "PRESP" : 0.17, "PASTP" : 0.04, "WZPAST" : 0.31, "WZPRES" : 0.18, "TSUB" : 0.08, "TOBJ" : 0.11, "WHSUB" : 0.20, "WHOBJ" : 0.17, "PIRE" : 0.11, "SERE" : 0.04, "CAUS" : 0.17, "CONC" : 0.08, "COND" : 0.22, "OSUB" : 0.11, "PIN" : 2.54, "JJ" : 1.88, "PRED" : 0.26, "RB" : 1.76, "TTR" : 5.2, "AWL" : 0.4, "CONJ" : 0.16, "DWNT" : 0.16, "HDG" : 0.13, "AMP" : 0.26, "EMPH" : 0.42, "DPAR" : 0.23, "DEMO" : 0.42, "POMD" : 0.35, "NEMD" : 0.21, "PRMD" : 0.42, "PUBV" : 0.54, "PRIV" : 1.04, "SUAV" : 0.31, "SMP" : 0.1, "CONT" : 1.86, "THATD" : 0.41, "STPR" : 0.27, "SPIN" : 0.00001, "SPAU" : 0.25, "PHC" : 0.27, "ANDC" : 0.48, "SYNE" : 0.16, "XX0" : 0.61}
    for field in tag_dict.keys():
        if field!="Tokens":
            tag_dict[field] = (tag_dict[field]- biber_means[field]/biber_sds[field])

    dimensions ={"D1":0.0,"D2":0.0,"D3":0.0,"D4":0.0,"D5":0.0}
    dimensions["D1"] = tag_dict["PRIV"] + tag_dict["THATD"] + tag_dict["CONT"] + tag_dict["VPRT"] +tag_dict["SPP2"]+tag_dict["PROD"]+tag_dict["XX0"]+tag_dict["DEMP"]+tag_dict["EMPH"]+tag_dict["FPP1"]+tag_dict["PIT"]+tag_dict["BEMA"]+tag_dict["CAUS"]+tag_dict["DPAR"]+tag_dict["INPR"]+tag_dict["AMP"]+tag_dict["POMD"]+tag_dict["ANDC"]+tag_dict["STPR"]-tag_dict["NN"]-tag_dict["AWL"]-tag_dict["PIN"]-tag_dict["JJ"]
    dimensions["D2"] = tag_dict["VBD"] + tag_dict["TPP3"] + tag_dict["PEAS"] + tag_dict["PUBV"] + tag_dict["SYNE"] + tag_dict["PRESP"]
    dimensions["D3"] = (tag_dict["WHOBJ"] + tag_dict["WHSUB"] + tag_dict["PHC"] + tag_dict["NOMZ"]) - (tag_dict["TIME"] + tag_dict["PLACE"] + tag_dict["RB"])
    dimensions["D4"] = tag_dict["TO"] + tag_dict["PRMD"] + tag_dict["SUAV"] + tag_dict["COND"] + tag_dict["NEMD"] + tag_dict["SPAU"]
    dimensions["D5"] = tag_dict["CONJ"] + tag_dict["PASS"] + tag_dict["WZPAST"] + tag_dict["OSUB"]

    out = os.path.join(directory_path,"Results/DimensionScore")
    out = os.path.join(out,filename)
    out = out.replace('txt','csv')
    with open(out,'w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow([a for a in dimensions.keys()])
        writer.writerow(['%.2f' % float(dimensions.get(index)) for index in dimensions.keys()])
        file.close()
    return dimensions

def __main__():
    if not os.path.exists('Results'):
        os.mkdir(os.path.join(os.getcwd(),'Results'))    
    os.chdir(os.path.join(os.getcwd(),'Results'))
    if not os.path.exists('FieldScore'):
        os.mkdir(os.path.join(os.getcwd(),'FieldScore'))
    if not os.path.exists('DimensionScore'):
        os.mkdir(os.path.join(os.getcwd(),'DimensionScore'))
    os.chdir('..')

    files = folderProcess()
    for file in files:
        filepath = os.path.join(directory_path,"Results/ModifiedTags")
        filepath = os.path.join(filepath,file)
        reader = open(filepath,'r')
        data=[]
        for line in reader:
            #print(line)
            data.append(line)
        reader.close()
        tag_dict = taggerCount(data,file)
        dimensionsCal(tag_dict,file)
    return

__main__()