__author__ = 'Cheech Wife'

class Code(object):
    def __init__(self):
        # self.checkfile = open("Check.txt", 'r')
        # self.hackFile = open(outputFile, "w")
        self.dest = ''
        self.comp = ''
        self.jump = ''
        self.aInst = ''
        # self.binaryTranslation = '111'+ self.aInst + self.comp + self.dest + self.jump

    def compA(self, line):
        if 'M' in line:
            self.aInst = '1111'
            if line == 'M':
                self.comp = '110000'
            elif line == '!M':
                self.comp = '110001'
            elif line == '-M':
                self.comp = '110011'
            elif line == 'M+1':
                self.comp = '110111'
            elif line == 'M-1':
                self.comp = '110010'
            elif line == 'D+M':
                self.comp = '000010'
            elif line == 'D-M':
                self.comp = '010011'
            elif line == 'M-D':
                self.comp = '000111'
            elif line == 'D&M:':
                self.comp = '000000'
            elif line == 'D|M':
                self.comp = '010101'
            return (self.aInst+self.comp)
        else:
            self.aInst = '1110'
            self.comp = self.Comp(line)
            return (self.aInst+self.comp)

    def Dest(self, line):
        if line == 'D':
            self.dest = '010'
        elif line == 'M':
            self.dest = '001'
        elif line == 'MD':
            self.dest = '011'
        elif line == 'A':
            self.dest = '100'
        elif line == 'AD':
            self.dest = '110'
        elif line == 'AM':
            self.dest = '101'
        elif line == 'AMD':
            self.dest = '111'
        elif line == 'null':
            self.dest = '000'
        return (self.dest)

    def Comp(self, line):
        if line == '0':
            self.comp = '101010'
        elif line == '1':
            self.comp = '111111'
        elif line == '-1':
            self.comp = '111010'
        elif line == 'D':
            self.comp = '001100'
        elif line == 'A':
            self.comp = '110000'
        elif line == '!D':
            self.comp = '001101'
        elif line == '!A':
            self.comp = '110001'
        elif line == '-D':
            self.comp = '001111'
        elif line == '-A':
            self.comp = '110011'
        elif line == 'D+1':
            self.comp = '011111'
        elif line == 'A+1':
            self.comp = '110111'
        elif line == 'D-1':
            self.comp = '00110'
        elif line == 'A-1':
            self.comp = '110010'
        elif line == 'D+A':
            self.comp = '000010'
        elif line == 'D-A':
            self.comp = '010011'
        elif line == 'A-D':
            self.comp = '000111'
        elif line == 'D&A':
            self.comp = '000000'
        elif line == 'D|A':
            self.comp = '010101'
        else:
            print ('ERROR')
        return (self.comp)

    def Jump(self, line):
        if line =='JGT':
           self.jump = '001'
        elif line == 'JEQ':
           self.jump = '010'
        elif line == 'JGE':
           self.jump = '011'
        elif line == 'JLT':
           self.jump = '100'
        elif line == 'JNE':
           self.jump = '101'
        elif line == 'JLE':
           self.jump = '110'
        elif line == 'JMP':
           self.jump = '111'
        else:
           print ('ERROR')
        return self.jump