import os

params = ["Sender", "Recipient", "Source Host", "Destination Host", "Message ID", "Export Path"]
param_values = ["", "", "", "", "", ""]
param_enabled = [False, False, False, False, False, False]
param_switches = ["-s", "-r", "-F", "-D", "-i", ">"]

def get_param_values():
    counter = 0
    for paramater in params:
        print(str((counter + 1)) + ". ", paramater + ":", param_values[counter])
        counter += 1

def change_param_value():
    param = int(input("Please enter the Parameter ID e.g. 1 you whish to change: "))
    param = param - 1
    print("Current Value:", param_values[param])
    new_value = input("Please enter the new value: ")
    param_values[param] = new_value
    print("New Value:", param_values[param])
    if new_value != "":
        param_enabled[param] = True
    elif new_value == "":
        param_enabled[param] = False

def run_enquiry():
    command = "/opt/zimbra/libexec/zmmsgtrace"
    counter = 0
    for param in params:
        if param_enabled[counter] == True:
            command = command + " " + param_switches[counter] + " " + param_values[counter]
        counter += 1
        #print(command)
        os.system(command)


def main():
    print("""**************************************************************************************************************
Zimbra Log Exporter Version 0.1
Developed by ayloNet Internal Systems Automation (DLPublicCode@aylo.net)
Available at: https://git.aylo.net/aylo/systems/apps/zimbra-log-retrieve (Internal) & https://git.aylo.net/noauth/zimbra-logging (Public)
**************************************************************************************************************""")
    while 1 == 1:
        get_param_values()
        print("""
        1. Change a Paramter Value
        2. Run
        3. Exit
        """)
        mode = input("Please enter an option: ")

        if int(mode) == 1:
            change_param_value()

        elif int(mode) == 2:
            run_enquiry()

        elif int(mode) == 3:
            quit()

    os.system('cls')
main()
