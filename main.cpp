#include <iostream>
#include<fstream>
using namespace std;

//***************************************** Functions **********************************************

void interface()
{
    cout << "************************************************************"
        << "************\n\t\tWelcome to invoice calculation program\n************************************************************************\n";
}
void Savedata (int sum[],int size,int totalsum)
{
    ofstream file;
    file.open("record.txt", ios_base::app);
    file<<"**************************************\n\t\tcalculation date and time \n"<<"\t\t"<<__DATE__<<"\n""\t\t"
    <<__TIME__<<"\n"<<"**************************************\n"<<endl;
    file<<"the total number of invoices:  "<<size<<endl;
    for (int i = 0; i < size; i++)
    {
        file <<"The sum of "<< i+1<<" invoice:  "<< sum[i]<<endl;
    }
    file <<"the total sum of invoices is:  "<< totalsum<<endl;
    file<<endl;
}

//***************************************** Main function **********************************************

int main() {
    interface();

    int number_of_invoices;
    cout << "enter the number of invoices\n";
    cin >> number_of_invoices;
    cout << endl;

    //***********  Creating dynamic arrays ************

    int** invoices = new int* [number_of_invoices];    //2D dynamic array
    int* sum = new int[number_of_invoices];
    int* size_of_invoice = new int[number_of_invoices];
    int totalsum = 0;

    // ***********  buffer optimization **************

    for (int k = 0; k < number_of_invoices; ++k) {
        sum[k] = 0;
        size_of_invoice[k] = 0;
    }

    //******** Getting size of invoices *******************

    for (int i = 0; i < number_of_invoices; ++i) {
        cout << "enter the number of items in the " << i + 1 << " invoice:  ";
        cin >> *(size_of_invoice + i);
        cout << endl;
    }

    // ********** Making 2D array*******************

    for (int i = 0; i < number_of_invoices; i++) {
        for (int j = 0; j < size_of_invoice[i]; ++j) {
            invoices[i] = new int[j];
        }
    }

    //************* Getting data for each item of invoice ******************

    for (int j = 0; j < number_of_invoices; ++j) {
        cout << "\n\n\t\t*************************************\n\t\t\tenter details of  " << j + 1 << " invoice\n\t\t*************************************\n\n";
        for (int i = 0; i < size_of_invoice[j]; ++i) {
            cout << "enter the value of " << i + 1 << " item:  ";
            cin >> *(*(invoices + j) + i);
            cout << endl;
        }
    }

    // ************** Calculating sum of items of each invoice *******************

    for (int i = 0; i < number_of_invoices; ++i) {

        for (int j = 0; j < size_of_invoice[i]; ++j) {
            sum[i] += *(*(invoices + i) + j);
        }
    }

    // ******************* Calculatin grand sum of all invoices ***************************

    for (int i = 0; i < number_of_invoices; ++i) {
        totalsum += sum[i];
    }

    //******************** Displaying sum of each invoice **********************************

    cout << "\n\n\t\t*********************************\n\t\tThe sum of values in the invoices\n\t\t*********************************\n\n";
    for (int l = 0; l < number_of_invoices; ++l) {
        cout << "the sum of items of " << l + 1 << " invoice is:\n" << sum[l] << endl;
        cout << endl;
    }

    //****************** Displaying grand sum *****************************************

    cout << "\n\n\t\t********************************\n\t\t\tThe sum of invoices\n\t\t********************************\n\n";
    cout << "the total sum is:  " << totalsum << endl;
    cout << endl;

    Savedata(sum, number_of_invoices, totalsum);    //Call function to save all data in  a txt file with date and time stamp

    //******************* deleting dynamic arrays to freeup RAM and to avoid memory leakage ****************************

    delete[]size_of_invoice;
    delete[] invoices;
    delete[] sum;
    return 0;
}