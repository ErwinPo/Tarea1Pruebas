def newbebida(input):
    correctedinput = input.replace(" ","") #clears each " " from the input
    parameters = correctedinput.rsplit(",") # splits on each comma
    if len(parameters) < 2 or len(parameters) > 6: return False # checks for number of inputs, one name and at least one size
    if any(i.isdigit() for i in parameters[0]): return False # Checks for numbers in parameter 0
    if len(parameters[0]) > 15 or len(parameters[0]) < 2: return False # Checks for name of size between 2 and 15
    try:
        if int(parameters[1]) not in range(1,49): return False #checks for size of first int
        if(len(parameters)) > 2: #if it has more than 1 size
            for i in range (2,len(parameters)):
                if int(parameters[i]) not in range(1,49) or int(parameters[i]) <= int(parameters[i-1]): return False #checks for order and range of int
    except: return False
    return True