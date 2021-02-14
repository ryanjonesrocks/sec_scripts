unparsed_file = open('unparsed.txt', 'r') 
parsedfile = open('parsed.txt', 'w') 
Lines = unparsed_file.readlines() 

# Strips the newline character 
for line in Lines: 
    temp_split = line.split()
    # For every port try both HTTP and HTTPS
    
    #HTTP
    if temp_split[1] == "443" || temp_split[1] == "80":
    	http_formatted_line = ("http://" + temp_split[0])
    else:
        http_formatted_line = ("http://" + temp_split[0] + ":" + temp_split[1])


    #HTTPS
    if temp_split[1] == "443" || temp_split[1] == "80":
    	https_formatted_line = ("https://" + temp_split[0])
    else:
        https_formatted_line = ("https://" + temp_split[0] + ":" + temp_split[1])

    
    #Output
    parsedfile.writelines(http_formatted_line)
    parsedfile.writelines("\n")
    parsedfile.writelines(https_formatted_line)
    parsedfile.writelines("\n")
