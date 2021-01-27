from re import search, finditer

class splitter:

    # Outputs a list of blocks of strings that contain meta data and the message
    def getMessageBlock(lines):
        file = open('test.txt', 'w')
        messageBlock = list()
        string = ''
        for i in range(len(lines)):
            string += lines[i]
            try:
                if search(r'^(\d){1,2}\/(\d){1,2}\/(\d){1,2}\,\s(\d){1,2}\:(\d){1,2}\s\-\s', lines[i + 1]):
                    file.write(string)
                    messageBlock.append(string)
                    string = ''
            except Exception:
                file.write(string)
                messageBlock.append(string)
                string = ''
        return messageBlock
    
    # Checks if it is sent by system or not
    def isSysMessage(messageBlock):
        line = messageBlock.splitlines()[0]
        if not search(r'^(\d){1,2}\/(\d){1,2}\/(\d){1,2}\,\s(\d){1,2}\:(\d){1,2}\s\-\s(\w)*\:', line):
            return True
        else:
            return False
    
    # Get the username of the sender, "_" means "you"
    def getusername(messageBlock):
        line = messageBlock.splitlines()[0]
        _splitAtSemicolon = line.split(':')
        _splitAtSpace = _splitAtSemicolon[1]
        userName = _splitAtSpace[5:]
        return str(userName)
    
    # Get the message part of the user message
    def getMessage(messageBlock):
        _splitAtSemicolon = messageBlock.split(':')
        message = _splitAtSemicolon[2:]
        return str(message)

    # Get the message part of the system message
    def getSysMessage(messageBlock):
        _splitAtSpace = messageBlock.split(' ')
        message = _splitAtSpace[3:]
        return ' '.join(message)
