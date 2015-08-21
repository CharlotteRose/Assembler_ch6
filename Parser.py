__author__ = 'Cheech Wife'
import symbolTable
import Code

#   Parser API:
#   Remove whitespace and comments
#   Get,read line
#   Evaluate line information ( A, C commands)
#   Based on command type returns symbol name for A, dest for C

class Parser(object):
    def __init__(self, inputFile, outputFile):
        self.asmFile = open(inputFile, "r")
        self.checkIt = open("Check.txt", "w")
        self.hackFile = open(outputFile,'w')
        self.newTable = symbolTable.SymbolTable()
        self.newTable.__init__()
        self.translation = Code.Code()
        self.translation.__init__()

    def __del__(self):
        print ('end')

    def advanceInFile(self):
        varMemLocation = 16
        asmInstructions = self.asmFile.readline()
        while asmInstructions:
            cIndex = asmInstructions.find("/") #finds all instances of comment identifiers
            asmInstructions = asmInstructions[:cIndex] #finds the comment indicator
            asmInstructions = asmInstructions.strip() + "\n"
            command = self.commandType(asmInstructions)
            if command == 'A_Command':
                if (self.newTable.checkTable(self.symbol(asmInstructions))):
                #print (self.newTable.getAddress(asmInstructions))
                # aInstr = self.newTable.getAddress(self.symbol(asmInstructions))
                # print(aInstr, 'what a gonna be')
                    self.checkIt.writelines(self.newTable.getAddress(self.symbol(asmInstructions))+'\n')
                else:
                    self.newTable.addEntry(self.symbol(asmInstructions), varMemLocation)
                    varMemLocation = varMemLocation+1
                    self.checkIt.writelines(self.newTable.getAddress(self.symbol(asmInstructions))+'\n')
            elif command == 'comp':
                comp = self.translation.compA(self.comp(asmInstructions))
                dest = self.translation.Dest(self.destC(asmInstructions))
                jump = '000'
                # print (comp, 'COMP IS')
                # print(dest, 'DEST IS')
                writeToFile = comp+dest+jump
                self.checkIt.writelines(writeToFile+'\n')
            elif command == 'jump':
                comp = self.translation.compA(self.comp(asmInstructions))
                dest = '000'
                jump = self.translation.Jump(self.jump(asmInstructions))
                writeToFile = comp+dest+jump
                self.checkIt.writelines(writeToFile+'\n')
            else:
                print ('Error')
            asmInstructions = self.asmFile.readline()

    def commandType(self, line):
        if '@' in line:
            # print ('a Instr')
            return ('A_Command')
        elif '=' in line:
            # print ('c instr')
            return ('comp')
        elif ';' in line:
            # print ('c instr')
            return ('jump')
        elif line == '' or line == '\n' or '(' in line:
            print ('empty')
            return 0
        else:
            print ('Error')
            return 0

    def symbol(self, line):
        #return m_string.replace("i", "")
        symbol = line.replace('@', '')
        symbol = symbol.strip()
        #print ('A SYMBOL', symbol)
        return symbol

    def destC(self, line):
        left = line.find('=')
        # print(line, left, 'rho')
        dest = line[:left]
        # print (dest, 'wip nah nah')
        # print (left, 'blue tick hound beagle')
        return dest

    def destJ(self, line):
        left = line.find(';')
        # print(line, left, 'meeeeeeeeow')
        dest = line[:left]
        # print (dest, 'me too, mushoo')
        return dest

    def comp(self, line):
        right = line.find('=')
        # print (right, line, 'ojonml')
        comp = line[right+1:]
        comp = comp.strip()
        # print (comp, 'COOOOOMP')
        return comp

    def jump(self, line):
        right = line.find(';')
        jump = line[right+1:]
        jump = jump.strip()
        return jump