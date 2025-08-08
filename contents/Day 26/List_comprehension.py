''' LIST COMPREHENSION '''
#LIST COMPREHENSION => to create a new list in one line without using for loops 

#name of new list
#    |      what do you want      previous list you are
#    |  this new outcome to be    iterating through 
#    |           |                   |
''' new_list = [new_item for item in list]'''
#                             |
#                      usually anything like: for n in list 
#                      n will be the case 


''' CONDITIONAL LIST COMPREHENSION '''
#name of new list
#    |      what do you want      previous list you are
#    |  this new outcome to be    iterating through 
#    |           |                    |       the condition you will put
#    |           |                    |        |
''' new_list = [new_item for item in list if test]'''
#                             |
#                      usually anything like: for n in list 
#                      n will be the case 