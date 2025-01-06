def cdr_validate(date,time,anumber,bnumber):
    cdrs = []
    with open("ACK_101440A.ACT",'r') as file:
        data = file.readlines()
        for line in data:
            if anumber in line and bnumber in line and date in line and time:
                cdrs.append(line)

    return cdrs

def process_cdrs(cdrs_list):
    for cdr in cdrs_list:
        cdr = cdr.split(",")
        if cdr[0] == 'START':
            date=cdr[5]
            time=cdr[6]
            calling_number=cdr[14]
            called_number=cdr[15]
            incoming_trunk=cdr[28]
            outgoing_trunk=cdr[96]
        elif cdr[0] == 'ATTEMPT':
            date=cdr[5]
            time=cdr[6]
            calling_number=cdr[16]
            called_number=cdr[17]
            incoming_trunk=cdr[30]
            outgoing_trunk=cdr[100]
        elif cdr[0] == 'STOP':
            date=cdr[10]
            time=cdr[11]
            calling_number=cdr[19]
            called_number=cdr[20]
            incoming_trunk=cdr[32]
            outgoing_trunk=cdr[110]
        
        output = {
            'date' : date,
            'time' : time,
            'calling number' : calling_number,
            'called_number' : called_number,
            'incoming_trunk' : incoming_trunk,
            'outgoing_trunk' : outgoing_trunk
        }
        
        return output
    
def counter():
    counter = 0
    with open("ACK_101440A.ACT",'r') as file:
        data = file.readlines()
        for line in data:
            if "IP-TO-IP" in line:
                counter = counter + 1
    
    return counter

# print(counter())
print(process_cdrs(cdr_validate('06/02/2024', '05:44:08.8','962776950050','249121127126')))