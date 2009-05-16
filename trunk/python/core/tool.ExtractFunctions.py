import os

def getFunctions():
    "Lists all functions in all files in current directory and sub-directories."
    
    def checkType(haystack, needle):
        "Check if the line specifies the types of functions to follow."        
        if haystack.find(needle)!=-1:
            print('\t    '+needle+'')

    for (path, dirs, files) in os.walk("."):
        for file in files:
            if (file=='tool.ExtractFunctions.py'): continue
            print(file+':')
            f = open(file, 'rt')
            for line in f:
                for s in ['Modifiers:', 'Callbacks:', 'Accessors:']:
                    checkType(line, s)
                if line[0:3]=='def':
                    # Cut off 'def ', ':', and '\n'
                    print('\t'+line[4:-2])
            f.close()

if __name__=='__main__':
    getFunctions()
