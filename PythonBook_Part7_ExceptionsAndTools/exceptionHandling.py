class FormatError(Exception):
    logfile = 'formaterror.txt'
    def __init__(self,line,file):
        self.line = line
        self.file = file
    def logerror(self):
        log = open(self.logfile,'a')
        print('Blad w ',self.file,self.line, file = log)

def parser():
    raise FormatError(42, file = 'spam.txt')

try:
    parser()
except FormatError as X:
    print('Błąd w',X.file,X.line)
    X.logerror()    #log error to file
    
