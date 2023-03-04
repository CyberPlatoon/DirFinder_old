import requests
from termcolor import colored



print(colored("""


                                                    
 ___             ___                  _              
(  _`\  _       (  _`\  _            ( )             
| | ) |(_) _ __ | (_(_)(_)  ___     _| |   __   _ __ 
| | | )| |( '__)|  _)  | |/' _ `\ /'_` | /'__`\( '__)
| |_) || || |   | |    | || ( ) |( (_| |(  ___/| |   
(____/'(_)(_)   (_)    (_)(_) (_)`\__,_)`\____)(_)   
=======================================================
=======================================================                                                     

                                         -By Pradeep Kumar
""", 'green'))      




Target = input(colored("  [+]   Enter Your Target {Use http/https} :  ", 'yellow', attrs=['bold']))

print("")

print(colored("  Wordlist Name; small, common, large", 'red', attrs=['bold','dark']))
print("")

wordlist = input(colored("  [+]   Enter Wordlist : ", 'yellow', attrs=['bold']))
print("")
print(colored("  The File Name must end with .txt", 'red', attrs=['bold','dark']))
print("")
Output_File = input(colored("  [+]   Enter Output File Name : ", 'yellow', attrs=['bold']))



print("\n")


Output = open("Output/"+Output_File, "w")
file = open(wordlist+".txt", "r")
file_Ex = open("extensions.txt", "r")


for i in file.readlines():
    url = Target +"/"+ i[0:len(i)-1]
    response = requests.get(url)
    #print("{} and {}".format(url,response.status_code))
    status =response.status_code
    size = response.headers.get('content-length', 0)

    
    if response.status_code==200:
        #print(url+" ===> 200")
        stu200 = url+" ===> 200"
        print(colored(" [+] ", 'green') + stu200)
        Output.write(stu200+"\n")


    
    if response.status_code==403:
        #print(url+" ===> 403")
        stu403 = url+" ===> 403"
        print(colored(" [+] ", 'red') + stu403)
        Output.write(stu403+"\n")


    
print("\n")
print("\n")

print(colored("  [+]   ** This is an Extensions file list like .php, .sql ** ", 'yellow', attrs=['bold','dark']))
print("\n")

#Output = open(Output_File, "w")
#file_Ex = open("ext.txt", "r")

for i in file_Ex.readlines():
    url = Target +"/"+ i[0:len(i)-1]
    response = requests.get(url)
    #print("{} and {}".format(url,response.status_code))
    status =response.status_code
    size = response.headers.get('content-length', 0)

    
    if response.status_code==200:
        #print(url+" ===> 200")
        satatus200 = url+" ===> 200"
        print(colored(" [+] ", 'green') + satatus200)
        Output.write(satatus200+"\n")


    
    if response.status_code==403:
        #print(url+" ===> 403")
        satatus403 = url+" ===> 403"
        print(colored(" [+] ", 'red') + satatus403)
        Output.write(satatus403+"\n")



    
    

#file.close()
#Output.close()



Output.close()
file.close()
file_Ex.close()


