import glob,os,stanza

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


def tagger(data,file):
    doc = nlp(data)
    stftoutfilepath = str(directory_path)+"/output/"+"stft_"+str(file)
    tagoutfilepath = str(directory_path)+"/outputDims/"+"tagged_"+str(file)
    out = open(stftoutfilepath,'w')
    dout = open(tagoutfilepath,'w')
    for i,sent in enumerate(doc.sentences):
        linewords=[]
        for word in sent.words:
            outstr = f'{word.text}_{word.xpos}\n'
            linewords.append(f'{word.text}_{word.xpos}')
            out.write(outstr)
        taglist = taggerAnalyzer(linewords)
        for tags in taglist:
            dout.write(tags+"\n")
    out.close()
    dout.close()
    return

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
            if (not '_dims' in name) and (not 'stft_' in name):
                validnames.append(name)
        print(validnames)
        return validnames

def taggerAnalyzer(wordList):
        for i in range(len(wordList)):
            word = wordList[i].split('_')
            if i<len(wordList)-1:
                next_word = wordList[i+1].split('_')
            else:
                next_word = ['','NULL']

            if(word[0].lower()=="to" and (next_word[0] in wp or next_word[1] in ["IN","CD","DT","JJ","PRPS","WPS","NN","NNP","PDT","PRP","WDT","WRB"])):
                wordList[i] = word[0] + "_PIN"

        for i in range(len(wordList)):
            word = wordList[i].split('_')
            # negation
            if("not" in word[0] or "n't" in word[0]) and word[1]=="RB":
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
                wordList[i]=word[0].lower()+'_OSUB'
                word = wordList[i].split('_')
            if (
                (word[0].lower() == "such" and next_word[0].lower() == "that") or 
                (word[0].lower() == "inasmuch" and next_word[0].lower() == "as") or
                (word[0].lower() == "forasmuch" and next_word[0].lower() == "as") or
                (word[0].lower() == "insofar" and next_word[0].lower() == "as") or
                (word[0].lower() == "insomuch" and next_word[0].lower() == "as") or
                (word[0].lower() == "so" and next_word[0].lower() == "that" and (second_next_word[1].upper() in ["NN","NNP","JJ"])) 
                ):
                wordList[i]=word[0].lower()+'_OSUB'
                word = wordList[i].split('_')
                wordList[i+1]=next_word[0].lower()+'_NULL'
                next_word = wordList[i+1].split('_')
            if ((word[0].lower() =="as") and (next_word[0].lower() in ["long","soon"]) and (second_next_word[0].lower() =="as")):
                wordList[i]=word[0].lower()+'_OSUB'
                word = wordList[i].split('_')
                wordList[i+1]=next_word[0].lower()+'_NULL'
                next_word = wordList[i+1].split('_')
                wordList[i+2]=second_next_word[0].lower()+'_NULL'
                second_next_word = wordList[i+2].split('_')

            #predicative adjectives
            if (word[0].lower() in be and next_word[1].upper() == "JJ" and second_next_word[1].upper() in ["JJ","RB","NN","NNP"]):
                wordList[i+1]=next_word[0].lower()+'_PRED'
                next_word = wordList[i+1].split('_')
            if (word[0].lower() in be and next_word[1].upper() == "RB" and second_next_word[1].upper()=="JJ" and third_next_word[1].upper() in ["JJ","RB","NN","NNP"]):
                wordList[i+2]=second_next_word[0].lower()+'_PRED'
                second_next_word = wordList[i+2].split('_')
            if (word[0].lower() in be and next_word[1].upper() == "XX0" and second_next_word[1].upper()=="JJ" and third_next_word[1].upper() in ["JJ","RB","NN","NNP"]):
                wordList[i+2]=second_next_word[0].lower()+'_PRED'
                second_next_word = wordList[i+2].split('_')
            if (word[0].lower() in be and next_word[1].upper() == "XX0" and second_next_word[1].upper()=="RB" and third_next_word[1].upper() =="JJ" and fourth_next_word in ["JJ","RB","NN","NNP"]):
                wordList[i+3]=third_next_word[0].lower()+'_PRED'
                third_next_word = wordList[i+3].split('_')
            if (word[1].upper() == "JJ" and previous_word[1].upper()=="PHC" and second_previous_word[1].upper()=="PRED"):
                wordList[i]=word[0].lower()+'_PRED'   
                word = wordList[i].split('_')
            
            #tags conjuncts
            if (word[0].lower() in symbols and next_word[0].lower() in ["else","altogether","rather"]):
                wordList[i+1]=next_word[0].lower()+"_CONJ"
                next_word = wordList[i+1].split('_')
            if word[0].lower() in conjunctives:
                wordList[i]=word[0].lower()+"_CONJ"
                word = wordList[i].split('_')
            if ((word[0].lower()=="in" and next_word[0].lower() in ["comparison","contrast","particular","addition","conclusion","consequence","sum","summary"]) or
                (word[0].lower()=="for" and next_word[0].lower() in ["example","instance"]) or
                (word[0].lower()=="instead" and next_word[0].lower()=="of") or
                (word[0].lower()=="by" and next_word[0].lower() in ["contrast","comparison"])):
                wordList[i]=word[0].lower()+"_CONJ"
                wordList[i+1]=next_word[0].lower()+"_NULL"
                word = wordList[i].split('_')
                next_word = wordList[i+1].split('_')
            if((word[0].lower()=="in" and next_word[0].lower()=="any" and second_next_word[0].lower() in ["event","case"]) or
                (word[0].lower()=="in" and next_word[0].lower()=="other" and second_next_word[0].lower()=="words") or
                (word[0].lower()=="as" and next_word[0].lower()=="a" and second_next_word[0].lower() in ["consequence","result"]) or
                (word[0].lower()=="on" and next_word[0].lower()=="the" and second_next_word[0].lower()=="contrary") ):
                wordList[i]=word[0].lower()+"_CONJ"
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
                wordList[i]=word[0].lower()+"_EMPH"
                word = wordList[i].split('_')
            if((word[0].lower() in ["real","so"] and next_word[1].upper() in ["JJ","PRED"]) or
                (word[0].lower() in do and next_word[1].upper() in v)):
                wordList[i]=word[0].lower()+"_EMPH"
                word = wordList[i].split('_')
            if((word[0].lower() == "for" and next_word[0].lower()=="sure") or
                (word[0].lower()=="a" and next_word[0].lower()=="lot") or
                (word[0].lower()=="such" and next_word[0].lower()=="a")):
                wordList[i]=word[0].lower()+"_EMPH"
                wordList[i+1]=next_word[0].lower()+"_NULL"
                word = wordList[i].split('_')
                next_word = wordList[i+1].split('_')
            
            #tags phrasal "and" coordination
            if((word[0].lower()=="and") or
                (previous_word[1].upper()=="RB" and next_word[1].upper()=="RB") or
                (previous_word[1].upper() in nn and next_word[1].upper() in nn) or
                (previous_word[1].upper() in v and next_word[1].upper() in v) or
                (previous_word[1].upper() in ["JJ","PRED"] and next_word[1].upper() in ["JJ","PRED"])):
                wordList[i]=word[0].lower()+"_PHC"
                word = wordList[i].split('_')

            #tags pro-verb do
            if word[0].lower() in do:
                if ((next_word[1].upper() not in v) and
                    (previous_word[0].lower() not in symbols) and
                    (next_word[1].upper() not in ["RB","XX0"] and second_next_word[1].upper() not in v) and
                    (next_word[1].upper() not in ["RB","XX0"] and second_next_word[1].upper() != "RB" and third_next_word[1].upper() not in v) and
                    (previous_word[0].lower() in wp or previous_word[0].lower() in who)):
                    wordList[i]=wordList[i]+"_PROD"
                    word = wordList[i].split('_')
            
            #tags WH questions
            if ((word[0].lower() in symbols and next_word[0].lower() in who and next_word[0].lower() not in ["however","whatever"] and second_next_word[1].upper()=="MD") or
                (word[0].lower() in symbols and next_word[0].lower() in who and next_word[0].lower() not in ["however","whatever"] and (second_next_word[0].lower() in do or second_next_word[0].lower() in have or second_next_word[0].lower() in be)) or
                (word[0].lower() in symbols and second_next_word[0].lower() in who and second_next_word[0].lower() not in ["however","whatever"] and third_next_word[1].upper() in be)):
                wordList[i+1]=wordList[i+1]+"_WHQU"
                next_word = wordList[i+1].split('_')

            #tags sentence relatives
            if(word[0].lower() in symbols and next_word[0].lower()=="which"):
                wordList[i+1]=wordList[i+1]+"_SERE"
                next_word = wordList[i+1].split('_')

            #tags perfect aspects
            if word[0].lower() in have:
                if ((next_word[1].upper() in ["VBD","VBN"]) or
                    (next_word[1].upper() in ["RB","XX0"] and second_next_word[1].upper() in ["VBD","VBN"]) or
                    (next_word[1].upper() in ["RB","XX0"] and second_next_word[1].upper() in ["RB","XX0"] and third_next_word[1].upper() in ["VBD","VBN"]) or
                    (next_word[1].upper() in ["NN","NNP","PRP"] and second_next_word[1].upper() in ["VBD","VBN"]) or
                    (next_word[1].upper() == "XX0" and second_next_word[1].upper() in ["NN","NNP","PRP"] and third_next_word[1].upper() in ["VBN","VBD"])):
                    wordList[i]=wordList[i]+"_PEAS"
                    word = wordList[i].split('_')

            #tags passives
            if word[0].lower() in be:
                if((next_word[1].upper() in ["VBD","VBN"] and second_next_word[0].lower()=="by")  or
                    (next_word[1].upper() in ["RB","XX0"] and second_next_word[1].upper() in ["VBD","VBN"] and third_next_word[0].lower()=="by") or
                    (next_word[1].upper() in ["RB","XX0"] and second_next_word[1].upper() in ["RB","XX0"] and third_next_word[1].upper() in ["VBD","VBN"] and fourth_next_word[0].lower()=="by") or
                    (next_word[1].upper() =="XX0" and second_next_word[1].upper() in ["NN","NNP","PRP"] and third_next_word[1].upper() in ["VBD","VBN"] and fourth_next_word[0].lower()=="by") or
                    (next_word[1].upper() in ["NN","NNP","PRP"] and second_next_word[1].upper() in ["VBD","VBN"] and third_next_word[0].lower()=="by")):
                    wordList[i] = wordList[i]+"_PASS" 
                    word = wordList[i].split('_') 

            #tags "by passives"
            if word[0].lower() in be:
                if ((next_word[1].upper() in ["VBD","VBN"] and second_next_word[0].lower() =="by") or
                    (next_word[1].upper() in ["RB","XX0"] and second_next_word[1].upper() in ["VBD","VBN"] and third_next_word[0].lower()=="by") or
                    (next_word[1].upper() in ["RB","XX0"] and second_next_word[1].upper() in ["RB","XX0"] and third_next_word[1].upper() in ["VBD","VBN"] and fourth_next_word[0].lower()=="by") or
                    (next_word[1].upper() in ["NN","NNP","PRP"] and second_next_word[1].upper() in ["VBD","VBN"] and third_next_word[0].lower()=="by") or
                    (next_word[1].upper() == "XX0" and second_next_word[1].upper() in ["NN","NNP","PRP"] and third_next_word[1].upper() in ["VBD","VBN"] and fourth_next_word[0].lower()=="by")):
                    wordList[i]=wordList[i]+"_BYPA"
                    word = wordList[i].split('_')

            #tags be as main verb
            if((second_previous_word[1].upper()!="EX" and previous_word[1].upper()!="EX" and word[0].lower() in be and next_word[1].upper() in ["CD","DT","PDT","PRPS","PRP","JJ","PRED","PIN","QUAN"]) or
                (second_previous_word[1].upper()!="EX" and previous_word[1].upper()!="EX" and word[0].lower() in be and next_word[1].upper() in ["RB","XX0"] and second_next_word[1].upper() in ["CD","DT","PDT","PRPS","PRP","JJ","PRED","PIN","QUAN"])):
                wordList[i] = wordList[i]+"_BEMA"
                word = wordList[i].split('_')

            #tags wh clauses
            if(word[0].lower() in public or word[0].lower() in private or word[0].lower() in suasive) and (next_word[0].lower() in wp or next_word[0].lower() in who) and (second_next_word[0].lower() in do or second_next_word[0].lower() in be or second_next_word[0].lower() in have or second_next_word[1].upper() =="MD"): 
                wordList[i+1]=wordList[i+1]+"_WHCL"
                next_word = wordList[i+1].split('_')

            #tags pied-piping relative clauses
            if word[1].upper()=="PIN" and next_word[0].lower() in ["who","whom","whose","which"]:
                wordList[i+1]=wordList[i+1]+"_PIRE"
                next_word = wordList[i+1].split('_')

            #tags stranded preposisitons
            if word[1].upper()=="PIN" and next_word[0].lower()!="besides" and next_word[0].lower() in [",","."]:
                wordList[i] = wordList[i]+"_STPR"
                word = wordList[i].split('_')

            #tags split infinitives
            if ((word[0].lower()=="to" and next_word[1].upper() in ["RB","AMPLIF","DOWNTON"] and next_word[0].lower() in ["just","really","most","more"] and second_next_word[1].upper() in v) or
                (word[0].lower()=="to" and next_word[1].upper() in ["RB","AMPLIF","DOWNTON"] and next_word[0].lower() in ["just","really","most","more"] and second_next_word[1].upper() in ["RB","AMPLIF","DOWNTON"] and third_next_word[1].upper() in v)):
                wordList[i] = wordList[i]+"_SPIN"
                word = wordList[i].split('_')

            #tags split auxiliaries
            if(((word[0].lower() in do or word[0].lower()in have or word[0].lower() in be) and word[1].upper()=="MD" and (next_word[1].upper() in ["RB","AMPLIF","DOWNTON"]) and (next_word[0].lower() in ["just","really","most","more"]) and second_next_word[1].upper() in v) or
                ((word[0].lower() in do or word[0].lower()in have or word[0].lower() in be) and word[1].upper()=="MD" and (next_word[1].upper() in ["RB","AMPLIF","DOWNTON"]) and (next_word[0].lower() in ["just","really","most","more"]) and second_next_word[1].upper()=="RB" and third_next_word[1].upper() in v)):
                wordList[i] = wordList[i]+"_SPAU"
                word = wordList[i].split('_')

            #tags synthetic negation
            if((word[0].lower()=="no" and next_word[1].upper() in ["JJ","PRED","NN","NNP"]) or
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
            if word[0].lower() in placeABV and word[1].upper()!="NNP":
                wordList[i] = word[0].lower()+"_PLACE"
                word = wordList[i].split('_')
                
            #tags 'that' verb complement
            if((previous_word[0].lower() in ["and","nor","but","or","also"] or previous_word[1].upper() in symbols )and word[0].lower()=="that" and (next_word[0].lower()=="there" or next_word[1].upper() in ["DT","QUAN","CD","PRP","NNS","NNP"])):
                wordList[i] = word[0].lower()+"_THVC"
                word = wordList[i].split('_')
            
            if((previous_word[0].lower() in public or previous_word[0].lower() in private or previous_word[0].lower() in suasive or (previous_word[0].lower() in ["seem","seems","seemed","seeming","appear","appears","appeared","appearing"] and previous_word[1].upper() in v)) and word[0].lower()=="that" and (next_word[0].lower() in do or next_word[0].lower() in be or next_word[0].lower() in have) or next_word[1].upper() in v or next_word[1].upper()=="MD" or next_word[0].lower()=="and"):
                wordList[i] = word[0].lower()+"_THVC"
                word = wordList[i].split('_')

            if((fourth_previous_word[0] in public or fourth_previous_word[0] in private or fourth_previous_word[0] in suasive) and third_previous_word[1].upper()=="PIN" and second_previous_word[1].upper() in nn and second_previous_word[1].upper() in nn and word[0].lower() =="that"):
                wordList[i] = word[0].lower()+"_THVC"
                word = wordList[i].split('_')

            if((fifth_previous_word[0] in public or fifth_previous_word[0] in private or fifth_previous_word[0] in suasive ) and fourth_previous_word[1].upper()=="PIN" and third_previous_word[1].upper() in nn and second_previous_word[1].upper() in nn and second_previous_word[1].upper() in nn and word[0].lower() =="that"):
                wordList[i] = word[0].lower()+"_THVC"
                word = wordList[i].split('_')
            if((sixth_previous_word[0] in public or sixth_previous_word[0] in private or sixth_previous_word[0] in suasive ) and fifth_previous_word[1].upper()=="PIN" and fourth_previous_word[1].upper() in nn and third_previous_word[1].upper() in nn and second_previous_word[1].upper() in nn and second_previous_word[1].upper() in nn and word[0].lower() =="that"):
                wordList[i] = word[0].lower()+"_THVC"
                word = wordList[i].split('_')

            #tags 'that' adjective complementss
            if previous_word[1].upper() in ["JJ","PRED"] and word[0].lower()=="that":
                wordList[i] = wordList[i]+"_THAC"
                word = wordList[i].split('_')
            
            #tags present participial clauses
            if previous_word[1].upper() in symbols and word[1].upper() =="VBG" and (next_word[1].upper() in ["PIN","DT","QUAN","CD","WPs","PRP","RB"] or next_word[0].lower() in wp or next_word[0].lower() in who):
                wordList[i] = wordList[i]+"_PRESP"
                word = wordList[i].split('_')

            #tags past participial clauses
            if previous_word[1].upper() in symbols and word[1].upper() =="VBN" and next_word[1].upper() in ["PIN","RB"]:
                wordList[i] = wordList[i]+"_PASTP"
                word = wordList[i].split('_')

            #tags past participial WHIZ deletion relatives
            if (previous_word[1].upper() in nn or previous_word[1].upper()=="QUPR") and word[1].upper() =="VBN" and (next_word[1].upper() in ["PIN","RB"] or next_word[0].lower() in be):
                wordList[i] = wordList[i]+"_WZPAST"
                word = wordList[i].split('_')

            #tags present participial WHIZ deletion relatives
            if previous_word[1].upper() in nn and word[1].upper()=="VBG":
                wordList[i] = wordList[i]+"_WZPRES"
                word = wordList[i].split('_')

            #tags "that" relative clauses on subject position
            if ((previous_word[1].upper() in nn and word[0].lower()=="that" and (next_word[1].upper() in v or next_word[1].upper()=="MD" or next_word[0].lower() in do or next_word[0].lower() in be or next_word[0].lower() in have)) or
                (previous_word[1].upper() in nn and word[0].lower()=="that" and next_word[1].upper() in ["RB","XX0"] and (second_next_word[1].upper() in v or second_next_word[1].upper()=="MD" or second_next_word[0].lower() in do or second_next_word[0].lower() in be or second_next_word[0].lower() in have)) or
                (previous_word[1].upper() in nn and word[0].lower()=="that" and next_word[1].upper() in ["RB","XX0"] and second_next_word[1].upper() in ["RB","XX0"] and (third_next_word[1].upper() in v or third_next_word[1].upper()=="MD" or third_next_word[0].lower() in do or third_next_word[0].lower() in be or third_next_word[0].lower() in have))):
                wordList[i] = word[0].lower()+"_TSUB"
                word = wordList[i].split('_')

            #tags "that" relative clauses on object positionW
            if((previous_word[1].upper() in nn and word[0].lower() =="that" and (next_word[0].lower() in ["it","i","we","he","she","they"] or next_word[1].upper() in ["DT","QUAN","CD","JJ","NNS","NNP","PRPS"]))or
                (previous_word[1].upper() in nn and word[0].lower()=="that" and next_word[1].upper() in nn and second_next_word[1].upper()=="POS")):
                wordList[i] = word[0].lower()+"_TOBJ"
                word = wordList[i].split('_')

            #tags WH relative clauses on subject position
            if((third_previous_word[0].lower() not in narrative and previous_word[1].upper() in nn and word in wp and(next_word[0].lower() in do or next_word[0].lower() in be or next_word[0].lower() in have or next_word[1].upper() in v or next_word=="MD")) or
                (third_previous_word[0].lower() not in narrative and previous_word[1].upper() in nn and word in wp and next_word[1].upper() in ["RB","XX0"] and(second_next_word[0].lower() in do or second_next_word[0].lower() in be or second_next_word[0].lower() in have or second_next_word[1].upper() in v or second_next_word=="MD")) or
                (third_previous_word[0].lower() not in narrative and previous_word[1].upper() in nn and word in wp and next_word[1].upper() in ["RB","XX0"] and second_next_word[1].upper() in ["RB","XX0"] and (third_next_word[0].lower() in do or third_next_word[0].lower() in be or third_next_word[0].lower() in have or third_next_word[1].upper() in v or third_next_word=="MD"))):
                wordList[i] = wordList[i]+"_WHSUB"
                word = wordList[i].split('_')

            #tags WH relative clauses on object position
            if(third_previous_word[0].lower() not in narrative and previous_word[1].upper() in nn and word in wp and(next_word[0].lower() in do or next_word[0].lower() in be or next_word[0].lower() in have or next_word[1].upper() in v or next_word in ["MD","RB","XX0"])):
                wordList[i] = wordList[i]+"_WHOBJ"
                word = wordList[i].split('_')

            #tags hedges
            if word[0].lower()=="maybe":
                wordList[i]= word[0].lower()+"_HDG"
                word = wordList[i].split('_')
            if((word[0].lower()=="at" and next_word[0].lower()=="about") or
                (word[0].lower()=="something" and next_word[0].lower()=="like")):
                wordList[i]= word[0].lower()+"_HDG"
                wordList[i+1]= next_word[0].lower()+"_NULL"
                word = wordList[i].split('_')
                next_word = wordList[i+1].split('_')
            if word[0].lower()=="more" and next_word[0].lower()=="or" and second_next_word[0].lower()=="less":
                wordList[i]= word[0].lower()+"_HDG"
                wordList[i+1]= next_word[0].lower()+"_NULL"
                wordList[i+2]= second_next_word[0].lower()+"_NULL"
                word = wordList[i].split('_')
                next_word = wordList[i+1].split('_')
                second_next_word = wordList[i+2].split('_')
            if (((second_previous_word[1].upper() in ["DT","QUAN","CD","JJ","PRED","PRPS"] or second_previous_word[0].lower() in who) and previous_word[0].lower()=="sort" and word[0].lower()=="of")or
                ((second_previous_word[1].upper() in ["DT","QUAN","CD","JJ","PRED","PRPS"] or second_previous_word[0].lower() in who) and previous_word[0].lower()=="kind" and word[0].lower()=="of")):
                wordList[i]= word[0].lower()+"_HDG"
                wordList[i-1]= previous_word[0].lower()+"_NULL"
                word = wordList[i].split('_')
                previous_word = wordList[i-1].split('_')

            #tags discourse particles
            if previous_word[1].upper() in symbols and word[0].lower() in ["well","now","anyhow","anyways"]:
                wordList[i] = word[0].lower()+"_DPAR"
                word = wordList[i].split('_')


        for i in range(len(wordList)):
            word = wordList[i].split('_')
            if i<len(wordList)-1:
                next_word = wordList[i+1].split('_')
            else:
                next_word = ['','NULL']
            #tags demonstrative pronouns
            if ((word[0].lower() in ["that","this","these","those"] and word[1].upper()!="NULL" and (next_word[0].lower() in do or next_word[0].lower() in be or next_word[0].lower() in have or next_word[0].lower() in wp or next_word[1].upper() in v or next_word[1].upper() =="MD" or next_word[0].lower()=="and" or next_word[1].upper() in symbols) and word[1].upper() not in ["TOBJ","TSUB","THAC","THVC"]) or
                (word[0].lower()=="that" and next_word[0].lower() in ["'s","is"])):
                wordList[i] = word[0].lower()+"_DEMP"
                word = wordList[i].split('_')

        for i in range(len(wordList)):
            word = wordList[i].split('_')
            if i<len(wordList)-1:
                next_word = wordList[i+1].split('_')
            else:
                next_word = ['','NULL']
            #tags demonstratives
            if word[0].lower() in ["that","this","these","those"] and word[1].upper() not in ["DEMP","TOBJ","TSUB","THAC","THVC","NULL"]:
                wordList[i] = word[0].lower()+"_DEMO"
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
            if (((word[0].lower() in public or word[0].lower() in private or word[0].lower() in suasive) and (next_word[0].lower() in ["i","we","she","he","they"] or next_word[1].upper()=="DEMP")) or
                ((word[0].lower() in public or word[0].lower() in private or word[0].lower() in suasive) and(next_word[1].upper() in ["PRP"] or next_word[1].upper() in nn) and (second_next_word[0].lower() in do or second_next_word[0].lower() in have or second_next_word[0].lower() in be or second_next_word[1].upper() in v or second_next_word[1].upper()=="MD")) or
                ((word[0].lower() in public or word[0].lower() in private or word[0].lower() in suasive) and next_word[1].upper() in ["JJ","PRED","RB","DT","QUAN","CD","PRPS"] and second_next_word[1].upper() in nn and (third_next_word[0].lower() in do or third_next_word[0].lower() in have or third_next_word[0].lower() in be or third_next_word[1].upper() in v or third_next_word[1].upper()=="MD")) or
                ((word[0].lower() in public or word[0].lower() in private or word[0].lower() in suasive) and next_word[1].upper() in ["JJ","PRED","RB","DT","QUAN","CD","PRPS"] and second_next_word[1].upper() in ["JJ","PRED"] and third_next_word[1].upper() in nn and (fourth_next_word[0].lower() in do or fourth_next_word[0].lower() in have or fourth_next_word[0].lower() in be or fourth_next_word[1].upper() in v or fourth_next_word[1].upper()=="MD"))):
                wordList[i] = wordList[i]+"_THATD"
                word = wordList[i].split('_')

        for i in range(len(wordList)):
            word = wordList[i].split('_')
            if i<len(wordList)-1:
                next_word = wordList[i+1].split('_')
            else:
                next_word = ['','NULL']
            #tags independent clause coordination
            if ((previous_word[1].upper()=="," and word[0].lower()=="and" and (next_word[0].lower() in ["it","so","then","you","u","we","he","she","they"] or next_word[1].upper()=="DEMP")) or
                (previous_word[1].upper()=="," and word[0].lower()=="and" and next_word[0].lower()=="there" and second_next_word[0].lower() in be) or
                (previous_word[1].upper() in symbols and word[0].lower()=="and") or
                (word[0].lower()=="and" and (next_word[0].lower() in wp or next_word[0].lower() in who or next_word[0].lower() in ["because","although","though","tho","if","unless"] or next_word[1].upper() in ["OSUB","DPAR","CONJ"]))):
                wordList[i] = word[0].lower()+"_ANDC"
                word = wordList[i].split('_')

        for i in range(len(wordList)):
            word = wordList[i].split('_')
            #basic tags
            if word[0].lower() in ["absolutely","altogether","completely","enormously","entirely","extremely","fully","greatly","highly","intensely","perfectly","strongly","thoroughly","totally","utterly","very"]:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_AMP"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if word[0].lower() in ["almost","barely","hardly","merely","mildly","nearly","only","partially","partly","practically","scarcely","slightly","somewhat"]:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_DWNT"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if ("tion"in word[0].lower() or "ment" in word[0].lower() or "ness" in word[0].lower() or "nesses" in word[0].lower() or "ity" in word[0].lower() or "ities" in word[0].lower()) and word[1].upper() in nn:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_NOMZ"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if ("ing" in word[0].lower() and word[1].upper() in nn) or ("ings" in word[0].lower() and word[1].upper() in nn):
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_GER"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if word[1].upper() in nn:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_NN"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if word[1].upper() in ["JJS","JJR"]:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_JJ"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if word[1].upper() in ["RBS","RBR","WRB"]:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_RB"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if word[1].upper() in ["VBP","VBZ"]:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_VPRT"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if word[0].lower() in ["I","me","we","us","my","our","myself","ourselves"]:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_FPP1"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if word[0].lower() in ["you","your","yourself","yourselves","thy","thee","thyself","thou"]:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_SPP2"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if word[0].lower() in ["she","he","they","her","his","them","him","their","himself","herself","themselves"]:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_TPP3"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if word[0].lower() in ["it","its","itself"]:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_PIT"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if word[0].lower() in ["because"]:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_CAUS"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if word[0].lower() in ["although","though","tho"]:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_CONC"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if word[0].lower() in ["if","unless"]:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_COND"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if (word[0].lower() in ["can","may","might","could"]) or ("ca" in word[0].lower() and word[1].upper()=="MD"):
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_POMD"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if word[0].lower() in ["ought","should","must"]:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_NEMD"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if (word[0].lower() in ["would","shall"]) or (("will" in word[0].lower() or "ll" in word[0].lower() or "wo" in word[0].lower() or "sha" in word[0].lower() or "'d" in word[0].lower()) and word[1].upper()=="MD"):
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_PRMD"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if word[0].lower() in public:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_PUBV"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if word[0].lower() in private:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_PRIV"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if word[0].lower() in suasive:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_SUAV"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if word[0].lower() in ["seem","seems","seemed","seeming","appear","appears","appeared","appearing"] and word[1].upper() in v:
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_SMP"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

            if (word[0].lower() in ["\'ll","\'d"] or ("n\'t" in word[0].lower() and word[1].upper()=="XX0") or ("\'" in word[0].lower() and word[1].upper() in v)):
                for n in range(len(word)):
                    if n==0:
                        wordList[i] = word[0]
                    elif n==1:
                        wordList[i] += "_CONT"
                    else:
                        wordList[i] += "_"+word[n]
                word = wordList[i].split('_')

        return wordList



wordList = folderProcess()
for file in wordList:
    filepath = directory_path+"\\output\\"+file
    with open(filepath,'r') as filecontent:
        data = filecontent.read().replace('\n',' ')
    tagger(data,file)
    break
    