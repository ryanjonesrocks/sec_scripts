unparsed_file = open('unparsed.txt', 'r') 
parsedfile = open('parsed.txt', 'w') 
Lines = unparsed_file.readlines() 

# Strips the newline character 
for line in Lines: 
    temp_split = line.split()
    
    unparsed_port = temp_split[3]
    port = unparsed_port.replace('/tcp', '')
    
    ip = temp_split[5]
    
    # For every port try both HTTP and HTTPS
    #HTTP
    if port == "443" or port == "80":
    	http_formatted_line = ("http://" + ip)
    else:
        http_formatted_line = ("http://" + ip + ":" + port)

    #HTTPS
    if port == "443" or port == "80":
    	https_formatted_line = ("https://" + ip)
    else:
        https_formatted_line = ("https://" + ip + ":" + port)

    #Output
    parsedfile.writelines(http_formatted_line)
    parsedfile.writelines("\n")
    parsedfile.writelines(https_formatted_line)
    parsedfile.writelines("\n")
