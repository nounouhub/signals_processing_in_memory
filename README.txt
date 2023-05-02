Description:
===================


please excute the  following command line to run the project:

main.py [signals.csv file full path] [keywords.csv file full path]

You have to indicate the full  paths  and  and files should be in csv format.
Files shouldn't be modified at any case . So, the algorithm checks if the digests for the provided files is correcexactelty the same as the original one.

According to the user input:
1- You can  get all signals.
2- You can get a specefic signal According to his node_id. 
3- tap q to quit the program.
Note : data are processed and retreived from memory.
In the next iteration we'll put  the data file  in Mysql Database and create and API to get data from signals table.