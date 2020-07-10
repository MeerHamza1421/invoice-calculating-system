def interface():
    print("************************************************************"
         "************\n\t\tWelcome to invoice calculation program\n************************************************************************\n")

interface()
numberOfinvoice=int(input("Enter the number of invoices:\t"))
sum=[None]*numberOfinvoice
invoice=[[None]]*numberOfinvoice
numberOfitems=[None]*numberOfinvoice
sizeOfinvoices=[None]*numberOfinvoice
totalSum=0
for i in range(numberOfinvoice):
    numberOfitems[i] = int(input("enter the number of items:\t"))
    invoice[i] = [None] * numberOfitems[i]
    sum[i]=0.0

for i in range(numberOfinvoice):
    print("****************************************************\n\t\t\tenter details of  ", i + 1, ""
          " invoice\n****************************************************\n\n")
    for j in range(numberOfitems[i]):
        print("Enter the item number", j+1, "of invoice", i+1, ":\t", end="")
        temp = input()
        indx1 = temp.index("*")
        indx2=temp.index("-")
        indx3=temp.index("%")

        val1=float(temp[:indx1])*20
        val2=int(temp[indx1+1:indx2])
        val3=int(temp[indx2+1:indx3])
        val1=((val1*val2)-((val1*val2)*(val3/100)))
        invoice[i][j]=val1
        print("Value:\t", invoice[i][j])
for i in range(numberOfinvoice):
    for j in range(numberOfitems[i]):
        sum[i]= float(sum[i] + invoice[i][j])
for i in range(numberOfinvoice):
    totalSum= float(totalSum + sum[i])
print("\n\n\t\t*********************************\n\t\t"
      "The sum of values in the invoices\n\t\t*********"
      "************************\n\n")
for i in range(numberOfinvoice):
    print("the sum of items of ", i + 1, " invoice is:\n", sum[i])
print("Total sum of all invoices",totalSum)