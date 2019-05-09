####################################################################################

#Welcome
print('\n')
print("*** Welcome to the Financial Report Machine - Python Edition *** ")
enter = raw_input("Press Enter to continue... ")

#Get date
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
print("Got it. Now, let's gather information about your assets. ")
enter = raw_input("Press Enter to continue... ")
asset1Name = raw_input("What is the name of the asset? ")
with open('report.txt', 'a') as file:
    file.write(str(asset1Name))
    file.write(": ")

asset1Value = input("What is the value of the asset? ")
with open('report.txt', 'a') as file:
    file.write(str(asset1Value))
    file.write('\n')

####################################################################################

#Liability header
with open('report.txt', 'a') as file:
    file.write('\n')
    file.write("***LIABILITIES***")
    file.write('\n')

#Get liability information
print("Got it. Now, let's gather information about your liabilities. ")
enter = raw_input("Press Enter to continue... ")
liability1Name = raw_input("What is the name of the liabilities? ")
with open('report.txt', 'a') as file:
    file.write(str(liability1Name))
    file.write(": ")

liability1Value = input("What is the value of the liabilities? ")
with open('report.txt', 'a') as file:
    file.write(str(liability1Value))
    file.write('\n')

####################################################################################

#Net worth header
with open('report.txt', 'a') as file:
    file.write('\n')
    file.write("***NET WORTH***")
    file.write('\n')

netWorth = asset1Value - liability1Value

with open('report.txt', 'a') as file:
    
    file.write("Total Assets: ")
    file.write(str(asset1Value))
    file.write('\n')

    file.write("Total Liabilities: ")
    file.write(str(liability1Value))
    file.write('\n')

    file.write('\n')
    file.write("Net Worth: ")
    file.write(str(netWorth))
    file.write('\n')

####################################################################################

#Exit program
enter = raw_input("Press Enter to terminate the program... ")

