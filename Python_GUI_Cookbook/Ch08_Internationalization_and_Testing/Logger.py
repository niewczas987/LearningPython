import os, time
from datetime import datetime
from Python_GUI_Cookbook.Ch08_Internationalization_and_Testing.Callbacks import Callbacks

class LogLevel:
    '''Defining log levels'''
    OFF = 0
    MINIMUM = 1
    NORMAL = 2
    DEBUG = 3

class Logger:
    '''Create a test log and write to it.'''
    def __init__(self, oop, fullTestName, logLevel=LogLevel.DEBUG):
        testName = os.path.splitext(os.path.basename(fullTestName))[0]
        logName = testName + '.log'
        logsFolder = 'logs'
        if not os.path.exists(logsFolder):
            os.makedirs(logsFolder, exist_ok=True)

        self.log = os.path.join(logsFolder, logName)
        self.callbacks = Callbacks(oop)
        self.createLog()
        self.loggingLevel = logLevel
        self.startTime = time.perf_counter()

    def createLog(self):
        with open(self.log, mode='w', encoding='utf-8') as logFile:
            logFile.write(self.callbacks.getDateTime() + '\t\t*** STARTING TEST ***\n')
            logFile.close()

    def writeToLog(self, msg='', logLevel=LogLevel.DEBUG):
        #check log level
        if logLevel > self.loggingLevel:
            return
        with open(self.log, mode='a', encoding='utf-8') as logFile:
            msg = str(msg)
            if msg.startswith('\n'):
                msg = msg[1:]
            logFile.write(self.callbacks.getDateTime() + '\t\t' + msg + '\n')
            logFile.close()

    def setLoggingLevel(self, level):
        self.loggingLevel = level