from re import search 

# Search the entier text file to find the lines which <start from mm/dd/yy, hh:mm - >
def messg_starting_point(lines):

    messg_start_point = list()

    i = 0
    
    for line in lines:
        
        if re.search(r'^(\d){1,2}\/(\d){1,2}\/(\d){1,2}\,\s(\d){1,2}\:(\d){1,2}\s\-\s', line):
            messg_start_point.append(i)
        i += 1

    return messg_start_point


# Checks if the message is from system or not.
def is_sys_msg(line):
    if not re.search(r'^(\d){1,2}\/(\d){1,2}\/(\d){1,2}\,\s(\d){1,2}\:(\d){1,2}\s\-\s', line):
        return True
    else:
        return False


# Return the username of the message sender.
def get_user_name(line):
    _split_at_semicolon = line.split(':')
    username = _split_at_semicolon[1]
    return username[5:]

# Get a block of content, this includes the message, username, and time.
def messg_block(lines):
    
    msg_block = list()
    string = ''

    for i in range(len(lines)):
        string += lines[i]
        try:
            if re.search(r'^(\d){1,2}\/(\d){1,2}\/(\d){1,2}\,\s(\d){1,2}\:(\d){1,2}\s\-\s', lines[i + 1]):
                msg_block.append(string)
                string = ''
        except Exception:
            msg_block.append(string)
            string = ''
        
    return msg_block


# Get the content of the user message.
def get_messg(msg_block):

    print(msg_block)

    _split_at_semicolon = msg_block.split(':')
    string = _split_at_semicolon[2:]
    
    
    print(string)
    return string
