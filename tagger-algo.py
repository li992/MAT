import glob,os,stanza
from datetime import datetime

# route initiation
directory_path = os.getcwd()

#stanford tagger initiation
nlp = stanza.Pipeline('en')
dimDict ={}

# type specifiers
have = ["have","has","'ve","had","having","hath"]
do = ["do","does","did","doing","done"]
wp = ["who","whom","whose","which"]
be = ["be","am","is","are","was","were","been","being","'s","'m","'re"]
who = ["what","where","when","how","whether","why","whoever","whomever","whichever","wherever","whenever","whatever","however"]
preposition = ["against","amid","amidst","among","amongst","at","besides","between","by","despite","during","except","for","from","in","into","minus","notwithstanding","of","off","on","onto","opposite","out","per","plus","pro","than","through","throughout","thru","toward","towards","upon","versus","via","with","within","without"]
public = ["acknowledge","acknowledged","acknowledges","acknowledging","add","adds","adding","added","admit","admits","admitting","admitted","affirm","affirms","affirming","affirmed","agree","agrees","agreeing","agreed","allege","alleges","alleging","alleged","announce","announces","announcing","announced","argue","argues","arguing","argued","assert","asserts","asserting","asserted","bet","bets","betting","boast","boasts","boasting","boasted","certify","certifies","certifying","certified","claim","claims","claiming","claimed","comment","comments","commenting","commented","complain","complains","complaining","complained","concede","concedes","conceding","conceded","confess","confesses","confessing","confessed","confide","confides","confiding","confided","confirm","confirms","confirming","confirmed","contend","contends","contending","contended","convey","conveys","conveying","conveyed","declare","declares","declaring","declared","deny","denies","denying","denied","disclose","discloses","disclosing","disclosed","exclaim","exclaims","exclaiming","exclaimed","explain","explains","explaining","explained","forecast","forecasts","forecasting","forecasted","foretell","foretells","foretelling","foretold","guarantee","guarantees","guaranteeing","guaranteed","hint","hints","hinting","hinted","insist","insists","insisting","insisted","maintain","maintains","maintaining","maintained","mention","mentions","mentioning","mentioned","object","objects","objecting","objected","predict","predicts","predicting","predicted","proclaim","proclaims","proclaiming","proclaimed","promise","promises","promising","promised","pronounce","pronounces","pronouncing","pronounced","prophesy","prophesies","prophesying","prophesied","protest","protests","protesting","protested","remark","remarks","remarking","remarked","repeat","repeats","repeating","repeated","reply","replies","replying","replied","report","reports","reporting","reported","say","says","saying","said","state","states","stating","stated","submit","submits","submitting","submitted","suggest","suggests","suggesting","suggested","swear","swears","swearing","swore","sworn","testify","testifies","testifying","testified","vow","vows","vowing","vowed","warn","warns","warning","warned","write","writes","writing","wrote","written"]
private = ["accept","accepts","accepting","accepted","anticipate","anticipates","anticipating","anticipated","ascertain","ascertains","ascertaining","ascertained","assume","assumes","assuming","assumed","believe","believes","believing","believed","calculate","calculates","calculating","calculated","check","checks","checking","checked","conclude","concludes","concluding","concluded","conjecture","conjectures","conjecturing","conjectured","consider","considers","considering","considered","decide","decides","deciding","decided","deduce","deduces","deducing","deduced","deem","deems","deeming","deemed","demonstrate","demonstrates","demonstrating","demonstrated","determine","determines","determining","determined","discern","discerns","discerning","discerned","discover","discovers","discovering","discovered","doubt","doubts","doubting","doubted","dream","dreams","dreaming","dreamt","dreamed","ensure","ensures","ensuring","ensured","establish","establishes","establishing","established","estimate","estimates","estimating","estimated","expect","expects","expecting","expected","fancy","fancies","fancying","fancied","fear","fears","fearing","feared","feel","feels","feeling","felt","find","finds","finding","found","foresee","foresees","foreseeing","foresaw","forget","forgets","forgetting","forgot","forgotten","gather","gathers","gathering","gathered","guess","guesses","guessing","guessed","hear","hears","hearing","heard","hold","holds","holding","held","hope","hopes","hoping","hoped","imagine","imagines","imagining","imagined","imply","implies","implying","implied","indicate","indicates","indicating","indicated","infer","infers","inferring","inferred","insure","insures","insuring","insured","judge","judges","judging","judged","know","knows","knowing","knew","known","learn","learns","learning","learnt","learned","mean","means","meaning","meant","note","notes","noting","noted","notice","notices","noticing","noticed","observe","observes","observing","observed","perceive","perceives","perceiving","perceived","presume","presumes","presuming","presumed","presuppose","presupposes","presupposing","presupposed","pretend","pretend","pretending","pretended","prove","proves","proving","proved","realize","realise","realising","realizing","realises","realizes","realised","realized","reason","reasons","reasoning","reasoned","recall","recalls","recalling","recalled","reckon","reckons","reckoning","reckoned","recognize","recognise","recognizes","recognises","recognizing","recognising","recognized","recognised","reflect","reflects","reflecting","reflected","remember","remembers","remembering","remembered","reveal","reveals","revealing","revealed","see","sees","seeing","saw","seen","sense","senses","sensing","sensed","show","shows","showing","showed","shown","signify","signifies","signifying","signified","suppose","supposes","supposing","supposed","suspect","suspects","suspecting","suspected","think","thinks","thinking","thought","understand","understands","understanding","understood"]
suasive = ["agree","agrees","agreeing","agreed","allow","allows","allowing","allowed","arrange","arranges","arranging","arranged","ask","asks","asking","asked","beg","begs","begging","begged","command","commands","commanding","commanded","concede","concedes","conceding","conceded","decide","decides","deciding","decided","decree","decrees","decreeing","decreed","demand","demands","demanding","demanded","desire","desires","desiring","desired","determine","determines","determining","determined","enjoin","enjoins","enjoining","enjoined","ensure","ensures","ensuring","ensured","entreat","entreats","entreating","entreated","grant","grants","granting","granted","insist","insists","insisting","insisted","instruct","instructs","instructing","instructed","intend","intends","intending","intended","move","moves","moving","moved","ordain","ordains","ordaining","ordained","order","orders","ordering","ordered","pledge","pledges","pledging","pledged","pray","prays","praying","prayed","prefer","prefers","preferring","preferred","pronounce","pronounces","pronouncing","pronounced","propose","proposes","proposing","proposed","recommend","recommends","recommending","recommended","request","requests","requesting","requested","require","requires","requiring","required","resolve","resolves","resolving","resolved","rule","rules","ruling","ruled","stipulate","stipulates","stipulating","stipulated","suggest","suggests","suggesting","suggested","urge","urges","urging","urged","vote","votes","voting","voted"]
symbols = [",",".","!","@","#","$","%","^","&","*","(",")","<",">","/","?","{","}","[","]","\\","|","-","+","=","~","`"]
indefinitePN = ["anybody","anyone","anything","everybody","everyone","everything","nobody","none","nothing","nowhere","somebody","someone","something"]
quantifier = ["each","all","every","many","much","few","several","some","any"]
quantifierPN = ["everybody","somebody","anybody","everyone","someone","anyone","everything","something","anything"]
conjunctives = ["alternatively","consequently","conversely","eg","e.g.","furthermore","hence","however","i.e.","instead","likewise","moreover","namely","nevertheless","nonetheless","notwithstanding","otherwise","similarly","therefore","thus","viz."]
timeABV = ["afterwards","again","earlier","early","eventually","formerly","immediately","initially","instantly","late","lately","later","momentarily","now","nowadays","once","originally","presently","previously","recently","shortly","simultaneously","subsequently","today","to-day","tomorrow","to-morrow","tonight","to-night","yesterday"]
placeABV = ["aboard","above","abroad","across","ahead","alongside","around","ashore","astern","away","behind","below","beneath","beside","downhill","downstairs","downstream","east","far","hereabouts","indoors","inland","inshore","inside","locally","near","nearby","north","nowhere","outdoors","outside","overboard","overland","overseas","south","underfoot","underground","underneath","uphill","upstairs","upstream","west"]
narrative = ["ask","asks","asked","asking","tell","tells","told","telling"]

# tag specifiers
v = ["VBG","VBN","VB","VBD","VBP","VBZ"]
nn = ["NN","NNP","NNPS","NNS"]

def printWithTime(Strr):
    now=datetime.now()
    dt = now.strftime("%Y-%m-%d %H:%M:%S")
    print(dt+" INFO: "+Strr)

def tagger(data,file):
    printWithTime("   Creating Stanford Tags....")
    doc = nlp(data)
    printWithTime("   Finished")
    stftoutfilepath = os.path.join(directory_path,'Results')
    stftoutfilepath = os.path.join(stftoutfilepath,'StanfordTags')
    stftoutfilepath = os.path.join(stftoutfilepath,file)
    tagoutfilepath = os.path.join(directory_path,'Results')
    tagoutfilepath = os.path.join(tagoutfilepath,'ModifiedTags')
    tagoutfilepath = os.path.join(tagoutfilepath,file)
    out = open(stftoutfilepath,'w')
    dout = open(tagoutfilepath,'w')
    printWithTime("   Generating Analyzed Tags...")
    for i,sent in enumerate(doc.sentences):
        linewords=[]
        for word in sent.words:
            outstr = f'{word.text}_{word.xpos}\n'
            linewords.append(f'{word.text}_{word.xpos}')
            out.write(outstr)
        taglist = taggerAnalyzer(linewords)
        for tags in taglist:
            dout.write(tags+"\n")
    printWithTime("   Finished")
    out.close()
    dout.close()
    return

def folderProcess():
    #print('folderprocess called')
    if not os.path.exists('MergedFiles'):
        printWithTime('Error: Please use FileMerger.py to generate raw data first')
        return
    else:
        os.chdir(os.path.join(directory_path,'MergedFiles'))
        filenames = glob.glob('*.txt')
        validnames =[]
        for name in filenames:
            validnames.append(name)
        #print(validnames)
        return validnames

def taggerAnalyzer(wordList):
        #first loop to define prepositions
        for i in range(len(wordList)):
            word = wordList[i].split('_')
            if i<len(wordList)-1:
                next_word = wordList[i+1].split('_')
            else:
                next_word = ['','NULL']

            if(word[0].lower()=="to" and (next_word[0] in wp or any(n in wordList[i+1] for n in ["IN","CD","DT","JJ","PRPS","WPS","NN","NNP","PDT","PRP","WDT","WRB"]))):
                wordList[i] = word[0] + "_PIN"

        #second loop to define simple types
        for i in range(len(wordList)):
            word = wordList[i].split('_')
            # negation
            if("not" in word[0] or "n't" in word[0]) and "RB" in wordList[i]:
                wordList[i] = word[0] + "_XX0"

            # preposition
            if word[0] in preposition:
                wordList[i] = word[0] + "_PIN"

            #indefinite pronouns
            if word[0] in indefinitePN:
                wordList[i] = word[0] + "_INPR"

            #quantifier
            if word[0] in quantifier:
                wordList[i] = word[0] + "_QUAN"

            #quantifier pronouns
            if word[0] in quantifierPN:
                wordList[i] = word[0] + "_QUPR"

        # third loop to define complex types
        for i in range(len(wordList)):
            word = wordList[i].split('_')
            if i<len(wordList)-4:
                fourth_next_word = wordList[i+4].split('_')
            else:
                fourth_next_word = ['','NULL']
            if i<len(wordList)-3:
                third_next_word = wordList[i+3].split('_')
            else:
                third_next_word = ['','NULL']
            if i<len(wordList)-2:
                second_next_word = wordList[i+2].split('_')
            else:
                second_next_word = ['','NULL']
            if i<len(wordList)-1:
                next_word = wordList[i+1].split('_')
            else:
                next_word = ['','NULL']
            if i>=1:
                previous_word = wordList[i-1].split('_')
            else:
                previous_word = ['','NULL']
            if i>=2:
                second_previous_word = wordList[i-2].split('_')
            else:
                second_previous_word = ['','NULL']
            if i>=3:
                third_previous_word = wordList[i-3].split('_')
            else:
                third_previous_word = ['','NULL']
            if i>=4:
                fourth_previous_word = wordList[i-4].split('_')
            else:
                fourth_previous_word = ['','NULL']
            if i>=5:
                fifth_previous_word = wordList[i-5].split('_')
            else:
                fifth_previous_word = ['','NULL']
            if i>=6:
                sixth_previous_word = wordList[i-6].split('_')
            else:
                sixth_previous_word = ['','NULL']

            #adverbial subordinators
            if word[0].lower() in ["since","while","whilst","whereupon","whereas","whereby"]:
                wordList[i]=wordList[i]+'_OSUB'
                word = wordList[i].split('_')
            if (
                (word[0].lower() == "such" and next_word[0].lower() == "that") or 
                (word[0].lower() == "inasmuch" and next_word[0].lower() == "as") or
                (word[0].lower() == "forasmuch" and next_word[0].lower() == "as") or
                (word[0].lower() == "insofar" and next_word[0].lower() == "as") or
                (word[0].lower() == "insomuch" and next_word[0].lower() == "as") or
                (word[0].lower() == "so" and next_word[0].lower() == "that" and any(n in second_next_word for n in ["NN","NNP","JJ"])) 
                ):
                wordList[i]=wordList[i]+'_OSUB'
                word = wordList[i].split('_')
                wordList[i+1]=wordList[i]+'_NULL'
                next_word = wordList[i+1].split('_')
            if ((word[0].lower() =="as") and (next_word[0].lower() in ["long","soon"]) and (second_next_word[0].lower() =="as")):
                wordList[i]=wordList[i]+'_OSUB'
                word = wordList[i].split('_')
                wordList[i+1]=next_word[0].lower()+'_NULL'
                next_word = wordList[i+1].split('_')
                wordList[i+2]=second_next_word[0].lower()+'_NULL'
                second_next_word = wordList[i+2].split('_')

            #predicative adjectives
            if (word[0].lower() in be and "JJ" in next_word and any(n in second_next_word for n in ["JJ","RB","NN","NNP"])):
                wordList[i+1]=wordList[i+1]+'_PRED'
                next_word = wordList[i+1].split('_')
            if (word[0].lower() in be and "RB" in next_word and "JJ" in second_next_word and any(n in third_next_word for n in ["JJ","RB","NN","NNP"])):
                wordList[i+2]=wordList[i+2]+'_PRED'
                second_next_word = wordList[i+2].split('_')
            if (word[0].lower() in be and "XX0" in next_word and "JJ" in second_next_word and any(n in third_next_word for n in ["JJ","RB","NN","NNP"])):
                wordList[i+2]=wordList[i+2]+'_PRED'
                second_next_word = wordList[i+2].split('_')
            if (word[0].lower() in be and "XX0" in next_word and "RB" in second_next_word and "JJ" in third_next_word and any(n in fourth_next_word for n in ["JJ","RB","NN","NNP"])):
                wordList[i+3]=wordList[i+3]+'_PRED'
                third_next_word = wordList[i+3].split('_')
            if ("JJ" in word and "PHC" in previous_word and "PRED" in second_previous_word):
                wordList[i]=wordList[i]+'_PRED'   
                word = wordList[i].split('_')
            
            #tags conjuncts
            if (word[0].lower() in symbols and next_word[0].lower() in ["else","altogether","rather"]):
                wordList[i+1]=wordList[i+1]+"_CONJ"
                next_word = wordList[i+1].split('_')
            if word[0].lower() in conjunctives:
                wordList[i]=wordList[i]+"_CONJ"
                word = wordList[i].split('_')
            if ((word[0].lower()=="in" and next_word[0].lower() in ["comparison","contrast","particular","addition","conclusion","consequence","sum","summary"]) or
                (word[0].lower()=="for" and next_word[0].lower() in ["example","instance"]) or
                (word[0].lower()=="instead" and next_word[0].lower()=="of") or
                (word[0].lower()=="by" and next_word[0].lower() in ["contrast","comparison"])):
                wordList[i]=wordList[i]+"_CONJ"
                wordList[i+1]=next_word[0].lower()+"_NULL"
                word = wordList[i].split('_')
                next_word = wordList[i+1].split('_')
            if((word[0].lower()=="in" and next_word[0].lower()=="any" and second_next_word[0].lower() in ["event","case"]) or
                (word[0].lower()=="in" and next_word[0].lower()=="other" and second_next_word[0].lower()=="words") or
                (word[0].lower()=="as" and next_word[0].lower()=="a" and second_next_word[0].lower() in ["consequence","result"]) or
                (word[0].lower()=="on" and next_word[0].lower()=="the" and second_next_word[0].lower()=="contrary") ):
                wordList[i]=wordList[i]+"_CONJ"
                wordList[i+1]=next_word[0].lower()+"_NULL"
                wordList[i+2]=second_next_word[0].lower()+"_NULL"
                word = wordList[i].split('_')
                next_word = wordList[i+1].split('_')
                second_next_word = wordList[i+2].split('_')
            if(word[0].lower()=="on" and next_word[0].lower()=="the"and second_next_word[0].lower()=="other" and third_next_word[0].lower()=="hand"):
                wordList[i]=word[0].lower()+"_CONJ"
                wordList[i+1]=next_word[0].lower()+"_NULL"
                wordList[i+2]=second_next_word[0].lower()+"_NULL"
                wordList[i+3]=third_next_word[0].lower()+"_NULL"
                word = wordList[i].split('_')
                next_word = wordList[i+1].split('_')
                second_next_word = wordList[i+2].split('_')
                third_next_word = wordList[i+3].split('_')

            #tags emphatics
            if word[0].lower() in ["just","really","most","more"]:
                wordList[i]=wordList[i]+"_EMPH"
                word = wordList[i].split('_')
            if((word[0].lower() in ["real","so"] and any(n in next_word for n in ["JJ","PRED"])) or
                (word[0].lower() in do and any(n in next_word for n in v))):
                wordList[i]=wordList[i]+"_EMPH"
                word = wordList[i].split('_')
            if((word[0].lower() == "for" and next_word[0].lower()=="sure") or
                (word[0].lower()=="a" and next_word[0].lower()=="lot") or
                (word[0].lower()=="such" and next_word[0].lower()=="a")):
                wordList[i]=wordList[i]+"_EMPH"
                wordList[i+1]=next_word[0].lower()+"_NULL"
                word = wordList[i].split('_')
                next_word = wordList[i+1].split('_')
            
            #tags phrasal "and" coordination
            if word[0].lower()=="and":
                if((("RB" in previous_word and "RB" in next_word)) or
                (any(n in previous_word for n in nn) and any(n in next_word for n in nn)) or
                (any(n in previous_word for n in v) and any(n in next_word for n in v)) or
                (any(n in previous_word for n in ["JJ","PRED"]) and any(n in next_word for n in ["JJ","PRED"]))):
                    wordList[i]=wordList[i]+"_PHC"
                    word = wordList[i].split('_')

            #tags pro-verb do
            if word[0].lower() in do:
                if (all(n not in next_word for n in v) and
                    (previous_word[0].lower() not in symbols) and
                    (all(n not in next_word for n in ["RB","XX0"]) and all(n not in second_previous_word for n in v)) and
                    (all(n not in next_word for n in ["RB","XX0"]) and "RB" not in second_next_word and all(n not in third_next_word for n in v)) and
                    (previous_word[0].lower() in wp or previous_word[0].lower() in who)):
                    wordList[i]=wordList[i]+"_PROD"
                    word = wordList[i].split('_')
            
            #tags WH questions
            if ((word[0].lower() in symbols and next_word[0].lower() in who and next_word[0].lower() not in ["however","whatever"] and "MD" in second_next_word) or
                (word[0].lower() in symbols and next_word[0].lower() in who and next_word[0].lower() not in ["however","whatever"] and (second_next_word[0].lower() in do or second_next_word[0].lower() in have or second_next_word[0].lower() in be)) or
                (word[0].lower() in symbols and second_next_word[0].lower() in who and second_next_word[0].lower() not in ["however","whatever"] and (third_next_word[0].upper() in be))):
                wordList[i+1]=wordList[i+1]+"_WHQU"
                next_word = wordList[i+1].split('_')

            #tags sentence relatives
            if(word[0].lower() in symbols and next_word[0].lower()=="which"):
                wordList[i+1]=wordList[i+1]+"_SERE"
                next_word = wordList[i+1].split('_')

            #tags perfect aspects
            if word[0].lower() in have:
                if (any(n in next_word for n in ["VBD","VBN"]) or
                    (any(n in next_word for n in ["RB","XX0"]) and any(n in second_next_word for n in ["VBD","VBN"])) or
                    (any(n in next_word for n in ["RB","XX0"]) and any(n in second_next_word for n in["RB","XX0"]) and any(n in third_next_word for n in ["VBD","VBN"])) or
                    (any(n in next_word for n in ["NN","NNP","PRP"]) and any(n in second_next_word for n in ["VBD","VBN"])) or
                    ("XX0" in next_word and any(n in second_next_word for n in["NN","NNP","PRP"]) and any(n in third_next_word for n in ["VBN","VBD"]))):
                    wordList[i]=wordList[i]+"_PEAS"
                    word = wordList[i].split('_')

            #tags passives
            if word[0].lower() in be or word[0].lower() in ["have","had","has","get"]:
                if((any(n in next_word for n in ["VBD","VBN"])) or
                    (any(n in next_word for n in ["RB","XX0"]) and any(n in second_next_word for n in ["VBD","VBN"])) or
                    (any(n in next_word for n in ["RB","XX0"]) and any(n in second_next_word for n in ["RB","XX0"]) and any(n in third_next_word for n in ["VBD","VBN"])) or
                    ("XX0" in next_word and any(n in second_next_word for n in ["NN","NNP","PRP"]) and any(n in third_next_word for n in ["VBD","VBN"])) or
                    (any(n in next_word for n in ["NN","NNP","PRP"]) and any(n in second_next_word for n in ["VBD","VBN"]))):
                    wordList[i] = wordList[i]+"_PASS" 
                    word = wordList[i].split('_') 

            #tags "by passives"
            if word[0].lower() in be or word[0].lower() in ["have","had","has","get"]:
                if ((any(n in next_word for n in ["VBD","VBN"]) and second_next_word[0].lower() =="by") or
                    (any(n in next_word for n in ["RB","XX0"]) and any(n in second_next_word for n in ["VBD","VBN"]) and third_next_word[0].lower()=="by") or
                    (any(n in next_word for n in ["RB","XX0"]) and any(n in second_next_word for n in ["RB","XX0"]) and any(n in third_next_word for n in ["VBD","VBN"]) and fourth_next_word[0].lower()=="by") or
                    (any(n in next_word for n in ["NN","NNP","PRP"]) and any(n in second_next_word for n in ["VBD","VBN"]) and third_next_word[0].lower()=="by") or
                    ("XX0" in next_word and any(n in second_next_word for n in ["NN","NNP","PRP"]) and any(n in third_next_word for n in ["VBD","VBN"]) and fourth_next_word[0].lower()=="by")):
                    if ("PASS" in wordList[i]):
                        wordList[i]=wordList[i].replace("PASS","BYPA")
                    else:
                        wordList[i]=wordList[i]+"_BYPA"
                    word = wordList[i].split('_')

            #tags be as main verb
            if(("EX" not in second_previous_word and "EX" not in previous_word and word[0].lower() in be and any(n in next_word for n in ["CD","DT","PDT","PRPS","PRP","JJ","PRED","PIN","QUAN"])) or
                ("EX" not in second_previous_word and "EX" not in previous_word and word[0].lower() in be and any(n in next_word for n in ["RB","XX0"]) and any(n in second_next_word for n in ["CD","DT","PDT","PRPS","PRP","JJ","PRED","PIN","QUAN"]))):
                wordList[i] = wordList[i]+"_BEMA"
                word = wordList[i].split('_')

            #tags wh clauses
            if(word[0].lower() in public or word[0].lower() in private or word[0].lower() in suasive) and (next_word[0].lower() in wp or next_word[0].lower() in who) and (second_next_word[0].lower() in do or second_next_word[0].lower() in be or second_next_word[0].lower() in have or "MD" in second_next_word): 
                wordList[i+1]=wordList[i+1]+"_WHCL"
                next_word = wordList[i+1].split('_')

            #tags pied-piping relative clauses
            if "PIN" in word and next_word[0].lower() in ["who","whom","whose","which"]:
                wordList[i+1]=wordList[i+1]+"_PIRE"
                next_word = wordList[i+1].split('_')

            #tags stranded preposisitons
            if "PIN" in word and next_word[0].lower()!="besides" and next_word[0].lower() in [",","."]:
                wordList[i] = wordList[i]+"_STPR"
                word = wordList[i].split('_')

            #tags split infinitives
            if ((word[0].lower()=="to" and any(n in next_word for n in ["RB","AMPLIF","DWNT"]) and next_word[0].lower() in ["just","really","most","more"] and any(n in second_next_word for n in v)) or
                (word[0].lower()=="to" and any(n in next_word for n in ["RB","AMPLIF","DWNT"]) and next_word[0].lower() in ["just","really","most","more"] and any(n in second_next_word for n in ["RB","AMPLIF","DOWNTON"]) and any(n in third_next_word for n in v))):
                wordList[i] = wordList[i]+"_SPIN"
                word = wordList[i].split('_')

            #tags split auxiliaries
            if(((word[0].lower() in do or word[0].lower() in have or word[0].lower() in be) and "MD" in word and any(n in next_word for n in ["RB","AMPLIF","DOWNTON"]) and (next_word[0].lower() in ["just","really","most","more"]) and any(n in second_next_word for n in v)) or
                ((word[0].lower() in do or word[0].lower() in have or word[0].lower() in be) and "MD" in word and any(n in next_word for n in ["RB","AMPLIF","DOWNTON"]) and (next_word[0].lower() in ["just","really","most","more"]) and "RB" in second_next_word and any(n in third_next_word for n in v))):
                wordList[i] = wordList[i]+"_SPAU"
                word = wordList[i].split('_')

            #tags synthetic negation
            if((word[0].lower()=="no" and any(n in next_word for n in ["JJ","PRED","NN","NNP"])) or
                word[0].lower() =="neither" or 
                word[0].lower() =="nor"):
                wordList[i] = word[0].lower()+"_SYNE"
                word = wordList[i].split('_')

            #tags time adverbials
            if(word[0].lower() in timeABV):
                wordList[i] = word[0].lower()+"_TIME"
                word = wordList[i].split('_')

            if(word[0].lower()=="soon" and next_word[0].lower()=="as"):
                wordList[i] = word[0].lower()+"_TIME"
                word = wordList[i].split('_')

            #tags place adverbials
            if word[0].lower() in placeABV and "NNP" not in word:
                wordList[i] = word[0].lower()+"_PLACE"
                word = wordList[i].split('_')
                
            #tags 'that' verb complement
            if((previous_word[0].lower() in ["and","nor","but","or","also"] or previous_word[0].upper() in symbols )and word[0].lower()=="that" and (next_word[0].lower()=="there" or any(n in next_word for n in ["DT","QUAN","CD","PRP","NNS","NNP"])) or
                ((previous_word[0].lower() in public or previous_word[0].lower() in private or previous_word[0].lower() in suasive or (previous_word[0].lower() in ["seem","seems","seemed","seeming","appear","appears","appeared","appearing"] and any(n in previous_word for n in v))) and word[0].lower()=="that" and (next_word[0].lower() in do or next_word[0].lower() in be or next_word[0].lower() in have) or any(n in next_word for n in v) or "MD" in next_word or next_word[0].lower()=="and") or
                ((fourth_previous_word[0] in public or fourth_previous_word[0] in private or fourth_previous_word[0] in suasive) and "PIN" in third_previous_word and any(n in second_previous_word for n in nn) and any(n in previous_word for n in nn) and word[0].lower() =="that") or
                ((fifth_previous_word[0] in public or fifth_previous_word[0] in private or fifth_previous_word[0] in suasive ) and "PIN" in fourth_previous_word and any(n in third_previous_word for n in nn) and any(n in second_previous_word for n in nn) and any(n in previous_word for n in nn) and word[0].lower() =="that") or
                ((sixth_previous_word[0] in public or sixth_previous_word[0] in private or sixth_previous_word[0] in suasive ) and "PIN" in fifth_previous_word and any(n in fourth_previous_word for n in nn) and any(n in third_previous_word for n in nn) and any(n in second_previous_word for n in nn) and any(n in previous_word for n in nn) and word[0].lower() =="that")):
                if(word[0].lower()=="that"):
                    wordList[i] = wordList[i]+"_THVC"
                word = wordList[i].split('_')

            #tags 'that' adjective complementss
            if (any(n in previous_word for n in ["JJ","PRED"]) and word[0].lower()=="that"):
                wordList[i] = wordList[i]+"_THAC"
                word = wordList[i].split('_')
            
            #tags present participial clauses
            if previous_word[0].upper() in symbols and "VBG" in word and (any(n in next_word for n in ["PIN","DT","QUAN","CD","WPs","PRP","RB"]) or next_word[0].lower() in wp or next_word[0].lower() in who):
                wordList[i] = wordList[i]+"_PRESP"
                word = wordList[i].split('_')

            #tags past participial clauses
            if previous_word[0].upper() in symbols and "VBN" in word and any(n in next_word for n in ["PIN","RB"]):
                wordList[i] = wordList[i]+"_PASTP"
                word = wordList[i].split('_')

            #tags past participial WHIZ deletion relatives
            if (any(n in wordList[i-1] for n in nn) or "QUPR" in previous_word) and "VBN" in word and (any(n in next_word for n in ["PIN","RB"]) or next_word[0].lower() in be):
                wordList[i] = wordList[i]+"_WZPAST"
                word = wordList[i].split('_')

            #tags present participial WHIZ deletion relatives
            if any(n in previous_word for n in nn) and "VBG" in word:
                wordList[i] = wordList[i]+"_WZPRES"
                word = wordList[i].split('_')

            #tags "that" relative clauses on subject position
            if ((any(n in previous_word for n in nn) and word[0].lower()=="that" and (any(n in next_word for n in v) or "MD" in next_word or next_word[0].lower() in do or next_word[0].lower() in be or next_word[0].lower() in have)) or
                (any(n in previous_word for n in nn) and word[0].lower()=="that" and any(n in next_word for n in ["RB","XX0"]) and (any(n in second_next_word for n in v) or "MD" in second_next_word or second_next_word[0].lower() in do or second_next_word[0].lower() in be or second_next_word[0].lower() in have)) or
                (any(n in previous_word for n in nn) and word[0].lower()=="that" and any(n in next_word for n in ["RB","XX0"]) and any(n in second_next_word for n in ["RB","XX0"]) and (any(n in third_next_word for n in v) or "MD" in third_next_word or third_next_word[0].lower() in do or third_next_word[0].lower() in be or third_next_word[0].lower() in have))):
                wordList[i] = word[0].lower()+"_TSUB"
                word = wordList[i].split('_')

            #tags "that" relative clauses on object positionW
            if((any(n in previous_word for n in nn) and word[0].lower() =="that" and (next_word[0].lower() in ["it","i","we","he","she","they"] or any(n in next_word for n in ["DT","QUAN","CD","JJ","NNS","NNP","PRPS"])))or
                (any(n in previous_word for n in nn) and word[0].lower()=="that" and any(n in next_word for n in nn) and "POS" in second_next_word)):
                wordList[i] = word[0].lower()+"_TOBJ"
                word = wordList[i].split('_')

            #tags WH relative clauses on subject position
            if((third_previous_word[0].lower() not in narrative and any(n in previous_word for n in nn) and word in wp and(next_word[0].lower() in do or next_word[0].lower() in be or next_word[0].lower() in have or any(n in next_word for n in v) or "MD" in next_word)) or
                (third_previous_word[0].lower() not in narrative and any(n in previous_word for n in nn) and word in wp and any(n in next_word for n in ["RB","XX0"]) and(second_next_word[0].lower() in do or second_next_word[0].lower() in be or second_next_word[0].lower() in have or any(n in second_next_word for n in v) or "MD" in second_next_word)) or
                (third_previous_word[0].lower() not in narrative and any(n in previous_word for n in nn) and word in wp and any(n in next_word for n in ["RB","XX0"]) and any(n in second_next_word for n in ["RB","XX0"]) and (third_next_word[0].lower() in do or third_next_word[0].lower() in be or third_next_word[0].lower() in have or any(n in third_next_word for n in v) or "MD" in third_next_word))):
                wordList[i] = wordList[i]+"_WHSUB"
                word = wordList[i].split('_')

            #tags WH relative clauses on object position
            if(third_previous_word[0].lower() not in narrative and any(n in previous_word for n in nn) and word in wp and(next_word[0].lower() in do or next_word[0].lower() in be or next_word[0].lower() in have or any(n in next_word for n in v) or any(n in next_word for n in ["MD","RB","XX0"]))):
                wordList[i] = wordList[i]+"_WHOBJ"
                word = wordList[i].split('_')

            #tags hedges
            if word[0].lower()=="maybe":
                wordList[i]= wordList[i]+"_HDG"
                word = wordList[i].split('_')
            if((word[0].lower()=="at" and next_word[0].lower()=="about") or
                (word[0].lower()=="something" and next_word[0].lower()=="like")):
                wordList[i]= wordList[i]+"_HDG"
                wordList[i+1]= next_word[0].lower()+"_NULL"
                word = wordList[i].split('_')
                next_word = wordList[i+1].split('_')
            if word[0].lower()=="more" and next_word[0].lower()=="or" and second_next_word[0].lower()=="less":
                wordList[i]= wordList[i]+"_HDG"
                wordList[i+1]= next_word[0].lower()+"_NULL"
                wordList[i+2]= second_next_word[0].lower()+"_NULL"
                word = wordList[i].split('_')
                next_word = wordList[i+1].split('_')
                second_next_word = wordList[i+2].split('_')
            if (((any(n in second_previous_word for n in ["DT","QUAN","CD","JJ","PRED","PRPS"]) or second_previous_word[0].lower() in who) and previous_word[0].lower()=="sort" and word[0].lower()=="of")or
                ((any(n in second_previous_word for n in ["DT","QUAN","CD","JJ","PRED","PRPS"]) or second_previous_word[0].lower() in who) and previous_word[0].lower()=="kind" and word[0].lower()=="of")):
                wordList[i]= wordList[i]+"_HDG"
                wordList[i-1]= previous_word[0].lower()+"_NULL"
                word = wordList[i].split('_')
                previous_word = wordList[i-1].split('_')

            #tags discourse particles
            if previous_word[0].upper() in symbols and word[0].lower() in ["well","now","anyhow","anyways"]:
                wordList[i] = wordList[i]+"_DPAR"
                word = wordList[i].split('_')


        for i in range(len(wordList)):
            word = wordList[i].split('_')
            if i<len(wordList)-1:
                next_word = wordList[i+1].split('_')
            else:
                next_word = ['','NULL']
            #tags demonstrative pronouns
            if ((word[0].lower() in ["that","this","these","those"] and "NULL" not in word and (next_word[0].lower() in do or next_word[0].lower() in be or next_word[0].lower() in have or next_word[0].lower() in wp or any(n in next_word for n in v) or "MD" in next_word or next_word[0].lower()=="and" or next_word[0].upper() in symbols) and all(n not in word for n in ["TOBJ","TSUB","THAC","THVC"])) or
                (word[0].lower()=="that" and next_word[0].lower() in ["'s","is"])):
                wordList[i] = wordList[i]+"_DEMP"
                word = wordList[i].split('_')

        for i in range(len(wordList)):
            word = wordList[i].split('_')
            if i<len(wordList)-1:
                next_word = wordList[i+1].split('_')
            else:
                next_word = ['','NULL']
            #tags demonstratives
            if word[0].lower() in ["that","this","these","those"] and all(n not in word for n in ["DEMP","TOBJ","TSUB","THAC","THVC","NULL"]):
                wordList[i] = wordList[i]+"_DEMO"
                word = wordList[i].split('_')

        for i in range(len(wordList)):
            word = wordList[i].split('_')
            if i<len(wordList)-4:
                fourth_next_word = wordList[i+4].split('_')
            else:
                fourth_next_word = ['','NULL']
            if i<len(wordList)-3:
                third_next_word = wordList[i+3].split('_')
            else:
                third_next_word = ['','NULL']
            if i<len(wordList)-2:
                second_next_word = wordList[i+2].split('_')
            else:
                second_next_word = ['','NULL']
            if i<len(wordList)-1:
                next_word = wordList[i+1].split('_')
            else:
                next_word = ['','NULL']
            #tags subordinator-that deletion
            if (((word[0].lower() in public or word[0].lower() in private or word[0].lower() in suasive) and (next_word[0].lower() in ["i","we","she","he","they"] or "DEMP" in next_word)) or
                ((word[0].lower() in public or word[0].lower() in private or word[0].lower() in suasive) and (["PRP"] in next_word or any(n in next_word for n in nn)) and (second_next_word[0].lower() in do or second_next_word[0].lower() in have or second_next_word[0].lower() in be or any(n in second_next_word for n in v) or "MD" in second_next_word)) or
                ((word[0].lower() in public or word[0].lower() in private or word[0].lower() in suasive) and any(n in next_word for n in ["JJ","PRED","RB","DT","QUAN","CD","PRPS"]) and any(n in second_next_word for n in nn) and (third_next_word[0].lower() in do or third_next_word[0].lower() in have or third_next_word[0].lower() in be or any(n in third_next_word for n in v) or "MD" in third_next_word)) or
                ((word[0].lower() in public or word[0].lower() in private or word[0].lower() in suasive) and any(n in next_word for n in ["JJ","PRED","RB","DT","QUAN","CD","PRPS"]) and any(n in second_next_word for n in ["JJ","PRED"]) and any(n in third_next_word for n in nn) and (fourth_next_word[0].lower() in do or fourth_next_word[0].lower() in have or fourth_next_word[0].lower() in be or any(n in fourth_next_word for n in v) or "MD" in fourth_next_word))):
                wordList[i] = wordList[i]+"_THATD"
                word = wordList[i].split('_')

        for i in range(len(wordList)):
            word = wordList[i].split('_')
            if i<len(wordList)-1:
                next_word = wordList[i+1].split('_')
            else:
                next_word = ['','NULL']
            #tags independent clause coordination
            if ((previous_word[0].upper()=="," and word[0].lower()=="and" and (next_word[0].lower() in ["it","so","then","you","u","we","he","she","they"] or "DEMP" in next_word)) or
                (previous_word[0].upper()=="," and word[0].lower()=="and" and next_word[0].lower()=="there" and second_next_word[0].lower() in be) or
                (previous_word[0].upper() in symbols and word[0].lower()=="and") or
                (word[0].lower()=="and" and (next_word[0].lower() in wp or next_word[0].lower() in who or next_word[0].lower() in ["because","although","though","tho","if","unless"] or any(n in next_word for n in ["OSUB","DPAR","CONJ"])))):
                wordList[i] = wordList[i]+"_ANDC"
                word = wordList[i].split('_')

        for i in range(len(wordList)):
            word = wordList[i].split('_')
            #basic tags
            if word[0].lower() in ["absolutely","altogether","completely","enormously","entirely","extremely","fully","greatly","highly","intensely","perfectly","strongly","thoroughly","totally","utterly","very"]:
                wordList[i] += "_AMP"
                word = wordList[i].split('_')

            if word[0].lower() in ["almost","barely","hardly","merely","mildly","nearly","only","partially","partly","practically","scarcely","slightly","somewhat"]:
                wordList[i] += "_DWNT"
                word = wordList[i].split('_')

            if ("tion"in word[0].lower() or "ment" in word[0].lower() or "ness" in word[0].lower() or "nesses" in word[0].lower() or "ity" in word[0].lower() or "ities" in word[0].lower()) and any(n in word for n in nn):
                wordList[i] += "_NOMZ"
                word = wordList[i].split('_')

            if ("ing" in word[0].lower() and any(n in word for n in nn)) or ("ings" in word[0].lower() and any(n in word for n in nn)):
                wordList[i] += "_GER"
                word = wordList[i].split('_')

            if any(n in word for n in nn):
                for n in nn:
                    wordList[i]=wordList[i].replace("_"+n,"")
                wordList[i] += "_NN"
                word = wordList[i].split('_')

            if any(n in word for n in ["JJS","JJR"]):
                for n in ["JJS","JJR"]:
                    wordList[i]=wordList[i].replace("_"+n,"")
                wordList[i] += "_JJ"
                word = wordList[i].split('_')

            if any(n in word for n in ["RBS","RBR","WRB"]):
                for n in ["RBS","RBR","WRB"]:
                    wordList[i]=wordList[i].replace("_"+n,"")
                wordList[i] += "_RB"
                word = wordList[i].split('_')

            if any(n in word for n in ["VBP","VBZ"]):
                for n in ["VBP","VBZ"]:
                    wordList[i]=wordList[i].replace("_"+n,"")
                wordList[i] += "_VPRT"
                word = wordList[i].split('_')

            if word[0].lower() in ["I","me","we","us","my","our","myself","ourselves"]:
                wordList[i] += "_FPP1"
                word = wordList[i].split('_')

            if word[0].lower() in ["you","your","yourself","yourselves","thy","thee","thyself","thou"]:
                wordList[i] += "_SPP2"
                word = wordList[i].split('_')

            if word[0].lower() in ["she","he","they","her","his","them","him","their","himself","herself","themselves"]:
                wordList[i] += "_TPP3"
                word = wordList[i].split('_')

            if word[0].lower() in ["it","its","itself"]:
                wordList[i] += "_PIT"
                word = wordList[i].split('_')

            if word[0].lower() in ["because"]:
                wordList[i] += "_CAUS"
                word = wordList[i].split('_')

            if word[0].lower() in ["although","though","tho"]:
                wordList[i] += "_CONC"
                word = wordList[i].split('_')

            if word[0].lower() in ["if","unless"]:
                wordList[i] += "_COND"
                word = wordList[i].split('_')

            if (word[0].lower() in ["can","may","might","could"]) or ("ca" in word[0].lower() and "MD" in word):
                wordList[i] += "_POMD"
                word = wordList[i].split('_')

            if word[0].lower() in ["ought","should","must"]:
                wordList[i] += "_NEMD"
                word = wordList[i].split('_')

            if (word[0].lower() in ["would","shall"]) or (("will" in word[0].lower() or "ll" in word[0].lower() or "wo" in word[0].lower() or "sha" in word[0].lower() or "'d" in word[0].lower()) and "MD" not in word):
                wordList[i] += "_PRMD"
                word = wordList[i].split('_')

            if word[0].lower() in public:
                wordList[i] += "_PUBV"
                word = wordList[i].split('_')

            if word[0].lower() in private:
                wordList[i] += "_PRIV"
                word = wordList[i].split('_')

            if word[0].lower() in suasive:
                wordList[i] += "_SUAV"
                word = wordList[i].split('_')

            if word[0].lower() in ["seem","seems","seemed","seeming","appear","appears","appeared","appearing"] and any(n in word for n in v):
                wordList[i] += "_SMP"
                word = wordList[i].split('_')

            if (word[0].lower() in ["\'ll","\'d"] or ("n\'t" in word[0].lower() and "XX0" in word) or ("\'" in word[0].lower() and any(n in word for n in v))):
                wordList[i] += "_CONT"
                word = wordList[i].split('_')

        return wordList

def __main__():
    printWithTime("Tagging program started")
    if not os.path.exists('Results'):
        os.mkdir(os.path.join(os.getcwd(),'Results'))
    os.chdir(os.path.join(os.getcwd(),'Results'))
    if not os.path.exists('StanfordTags'):
        os.mkdir(os.path.join(os.getcwd(),'StanfordTags'))
    if not os.path.exists('ModifiedTags'):
        os.mkdir(os.path.join(os.getcwd(),'ModifiedTags'))
    os.chdir('..')

    wordList = folderProcess()
    for file in wordList:
        printWithTime("Now processing file: "+file+"...")
        filepath = os.path.join(directory_path,"MergedFiles")
        filepath = os.path.join(filepath,file)
        with open(filepath,'r') as filecontent:
            data = filecontent.read().replace('\n',' ')
        tagger(data,file)
        printWithTime("Tag generation complete: "+file+"")
        break
    printWithTime("Tagging program finished\nPlease use tagger-count.py to generate analysis data")
    return

__main__()