import datetime

#                      function for user interference

def interface():
    print("************************************************************"
         "************\n\t\tWelcome to invoice calculation program\n************************************************************************\n")

#                   Function to keep the record of the data

def saveData(sumData, totalSum, numberOfinvoice):
    file=open("record.txt","a")
    curTime = datetime.datetime.now()
    file.write(f"****************************************************\n\t\t\t{curTime}\n****************************************************\n\n")
    for i in range(numberOfinvoice):
        file.write(f"The sum of {i+1} invoice:\t{sumData[i]} \n")

    file.write(f" the total sum of  {numberOfinvoice}  invoices is:\t {totalSum} \n")

interface()

#                       Declaring required variables and arrays

numberOfinvoice=int(input("Enter the number of invoices:\t"))
sum=[None]*numberOfinvoice
invoice=[[None]]*numberOfinvoice
numberOfitems=[None]*numberOfinvoice
sizeOfinvoices=[None]*numberOfinvoice
totalSum=0

#                       initialize by initial values to assist calculation

for i in range(numberOfinvoice):
    numberOfitems[i] = int(input("enter the number of items:\t"))
    invoice[i] = [None] * numberOfitems[i]
    sum[i]=0.0

#                       Calculating values

for i in range(numberOfinvoice):
    print("****************************************************\n\t\t\tenter details of  ", i + 1, ""
          " invoice\n****************************************************\n\n")

    for j in range(numberOfitems[i]):
        print("Enter the details of ", j+1, " item of invoice", i+1, "\n")
        pricePerfoot = float(input("\nEnter the price of per foot of the item:\t"))
        quantity = float(input("\nEnter the quantity of the item:\t"))
        foot = float(input("\nEnter the total lenght in foots:\t"))
        percentage= float(input("\nEnter the deduct percentage in the item:\t"))
        pricePerfoot = (pricePerfoot*quantity*foot)-((pricePerfoot*quantity*foot)*(percentage/100))
        invoice[i][j]=pricePerfoot
        print("Value:\t", invoice[i][j],"\n\n")

#                       Calculating sum of each invoice

for i in range(numberOfinvoice):
    for j in range(numberOfitems[i]):
        sum[i]= float(sum[i] + invoice[i][j])

#                       Calculating total sum of all invoices

for i in range(numberOfinvoice):
    totalSum= float(totalSum + sum[i])

print("\n\n\t\t*********************************\n\t\t"
      "The sum of values in the invoices\n\t\t*********"
      "************************\n\n")

for i in range(numberOfinvoice):
    print("the sum of items of ", i + 1, " invoice is:\n", sum[i])
print("Total sum of all invoices",totalSum)

#                       At last save all data

saveData(sum,totalSum,numberOfinvoice)