####################################################################################

#Welcome
print('\n')
print("*** Welcome to the Financial Report Machine - Python Edition *** ")
print('\n')
enter = raw_input("Press Enter to continue... ")

#Get date
print('\n')
enteredDate = raw_input("What is today's date? ")
with open('report.txt', 'a') as file:
    file.write('\n')
    file.write(enteredDate)
    file.write('\n')

####################################################################################

#Asset header
with open('report.txt', 'a') as file:
    file.write('\n')
    file.write("***ASSETS***")
    file.write('\n')

#Get asset information
print('\n')
enter = raw_input("Got it. Now, let's gather information about your assets. Press Enter to continue... ")

enter = raw_input("Would you like to add an asset? Press Enter to do so, or type 'next' and press Enter to continue. ")
print('\n')

assetAccum = 0
while enter != "next":
    assetName = raw_input("What is the name of the asset? ")
    with open('report.txt', 'a') as file:
        file.write(str(assetName))
        file.write(": ")
    assetValue = input("What is the value of the asset? ")
    assetAccum = assetAccum + assetValue
    with open('report.txt', 'a') as file:
        file.write(str(assetValue))
        file.write('\n')
    enter = raw_input("Would you like to add another asset? Press Enter to do so, or type 'next' and press Enter to continue. ")
    print('\n')

####################################################################################

#Liability header
with open('report.txt', 'a') as file:
    file.write('\n')
    file.write("***LIABILITIES***")
    file.write('\n')

#Get liability information
print('\n')
enter = raw_input("Ok. Now, let's gather information about your liabilities. Press Enter to continue... ")

enter = raw_input("Would you like to add a liability? Press Enter to do so, or type 'next' and press Enter to continue. ")
print('\n')

liabilityAccum = 0
while enter != "next":
    liabilityName = raw_input("What is the name of the liability? ")
    with open('report.txt', 'a') as file:
        file.write(str(liabilityName))
        file.write(": ")
    liabilityValue = input("What is the value of the liability? ")
    liabilityAccum = liabilityAccum + liabilityValue
    with open('report.txt', 'a') as file:
        file.write(str(liabilityValue))
        file.write('\n')
    enter = raw_input("Would you like to add another liability? Press Enter to do so, or type 'next' and press Enter to continue. ")
    print('\n')

####################################################################################

#Net worth header
with open('report.txt', 'a') as file:
    file.write('\n')
    file.write("***NET WORTH***")
    file.write('\n')

netWorth = assetAccum - liabilityAccum

with open('report.txt', 'a') as file:
    
    file.write("Total Assets: ")
    file.write(str(assetAccum))
    file.write('\n')

    file.write("Total Liabilities: ")
    file.write(str(liabilityAccum))
    file.write('\n')

    file.write("Net Worth: ")
    file.write(str(netWorth))
    file.write('\n')

####################################################################################

#Exit program
print("Your total assets are " + str(assetAccum))
print("Your total liabilities are " + str(liabilityAccum))
print("Your net worth is " + str(netWorth))
print('\n')
enter = raw_input("A report has been generated using the information provided. Press Enter to terminate the program... ")

