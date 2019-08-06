#Importing
from datetime import datetime

#FUNCTIONS###################################################################################

#Make header function
def makeHeader(arg):
    with open(currentDate, 'a') as file:
        file.write('\n')
        file.write("***" + arg + "***")
        file.write('\n')

#Write totals function
def writeTotal(label, variable):
    file.write(label + ": ")
    file.write(str(variable))
    file.write('\n')

####################################################################################

#Welcome
print('\n')
print("*****************************************************************")
print("*** Welcome to the Financial Report Machine - Python Edition *** ")
print("*****************************************************************")
print('\n')
enter = raw_input("Press Enter to continue... ")

#Get date, write to file
print('\n')
currentDate = datetime.now().strftime('%Y-%m-%d')
with open(currentDate, 'w') as file:
    file.write('\n')
    file.write(currentDate)
    file.write('\n')

####################################################################################

#Asset header
makeHeader("ASSETS")

#Get asset information
enter = raw_input("Let's begin gather information about your assets. Press Enter to continue... ")
print('\n')

#Confirm need to add asset, set accum to zero, test for 'no'
enter = raw_input("Would you like to add an asset? Press Enter to do so, or type 'no' and press Enter to continue. ")
print('\n')
assetAccum = 0
while enter != "no":
    
    #Ask for asset name until value provided
    assetName = raw_input("What is the name of the asset? ")
    while assetName == '':
        assetName = raw_input("What is the name of the asset? ")
    with open(currentDate, 'a') as file:
        file.write(str(assetName))
        file.write(": ")

    #Initialize asset value at zero, ask for correct value
    assetValue = 0
    while assetValue == '' or assetValue == 0:
        assetValue = input("What is the value of the asset? ")
    assetAccum = assetAccum + assetValue
    with open(currentDate, 'a') as file:
        file.write(str(assetValue))
        file.write('\n')
    print('\n')

    #Determine if exit loop
    enter = raw_input("Would you like to add another asset? Press Enter to do so, or type 'no' and press Enter to continue. ")
    print('\n')

####################################################################################

#Liability header
makeHeader("LIABILITIES")

#Get liability information
enter = raw_input("Ok. Now, let's gather information about your liabilities. Press Enter to continue... ")
print('\n')

#Confirm need to add liability, set accum to zero, test for 'no'
enter = raw_input("Would you like to add a liability? Press Enter to do so, or type 'no' and press Enter to continue. ")
print('\n')
liabilityAccum = 0
while enter != "no":
    
    #Ask for liabililty name until a value is provided
    liabilityName = raw_input("What is the name of the liability? ")
    while liabilityName == '':
        liabilityName = raw_input("What is the name of the liability? ")
    with open(currentDate, 'a') as file:
        file.write(str(liabilityName))
        file.write(": ")
    
    #Ask for value of liability
    liabilityValue = input("What is the value of the liability? ")
    liabilityAccum = liabilityAccum + liabilityValue
    with open(currentDate, 'a') as file:
        file.write(str(liabilityValue))
        file.write('\n')
    print('\n')

    #Determine if exit loop
    enter = raw_input("Would you like to add another liability? Press Enter to do so, or type 'no' and press Enter to continue. ")
    print('\n')

####################################################################################

#Net worth header
makeHeader("NET WORTH")

#Calculate net worth
netWorth = assetAccum - liabilityAccum

#Write totals and net worth to file
with open(currentDate, 'a') as file:
    writeTotal("Total Assets", assetAccum)
    writeTotal("Total Liabilities", liabilityAccum)
    writeTotal("Net Worth", netWorth)

####################################################################################

#Exit program
print("Your total assets are " + str(assetAccum))
print("Your total liabilities are " + str(liabilityAccum))
print("Your net worth is " + str(netWorth))
print('\n')
enter = raw_input("A report has been generated using the information provided. Press Enter to terminate the program... ")
print('\n')
print("*****************************************************************")

