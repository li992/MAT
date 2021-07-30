import glob,os

# m stands for merged files, f stands for fragments
directory_path = os.getcwd()
mlist_path = os.path.join(directory_path,'mlist.txt')
flist_path = os.path.join(directory_path,'flist.txt')
mfilenames = []
ffilenames = []

if os.path.exists('flist.txt'):
    os.remove(flist_path)
if os.path.exists('mlist.txt'):
    os.remove(mlist_path)


if not os.path.exists('Results'):
    print('Folder \'Results\' not found, no analyzed data found')
else:
    os.chdir(os.path.join(os.getcwd(),'Results'))
    if not os.path.exists('ModifiedTags'):
        out = open(mlist_path,'w')
        out.write('0')
        out.close()
    else:
        os.chdir(os.path.join(os.getcwd(),'ModifiedTags'))
        mfilenames = glob.glob('*.txt')
        out = open(mlist_path,'w')
        for l in mfilenames:
            out.write(l+'\n')
        os.chdir(os.path.join(directory_path,'Results'))
    if not os.path.exists('ModifiedTagsFragment'):
        out = open(flist_path,'w')
        out.write('0')
        out.close()
    else:
        os.chdir(os.path.join(os.getcwd(),'ModifiedTagsFragment'))
        ffilenames = glob.glob('*.txt')
        out = open(flist_path,'w')
        for l in ffilenames:
            out.write(l+'\n')
        os.chdir(os.path.join(directory_path,'Results'))


