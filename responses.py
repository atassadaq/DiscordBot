import random
def handleResponse(message) -> str: #-> is for return type
    processedMessage = message.lower()

    if  processedMessage == 'hello':
        return 'Hey there'
    
    if processedMessage == 'roll':
        return str(random.randint(1,6))
    
    if processedMessage =='help':
        return "`this is a help message`"