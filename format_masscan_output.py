unparsed_file = open('input.txt', 'r') 
parsedfile = open('output.txt', 'w') 
Lines = unparsed_file.readlines() 

# Strips the newline character 
for line in Lines: 
    temp_split = line.split()
    if temp_split[1] == "443":
    	formatted_line = ("https://" + temp_split[0])
    else:
    	formatted_line = (temp_split[0]+":"+temp_split[1])
    
    parsedfile.writelines(formatted_line)
    parsedfile.writelines("\n")
