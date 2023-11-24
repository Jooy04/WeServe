# WeServe ETL 
__WeServe is a call service agency that outsources customer service personnels to several companies.
    These agents are located in one call center. They receive calls from customers, and make calls to 
	customers, in order to listen to complaints, and get feedback of products and services they have 
 	purchased from varying companies.These calls are recorded in the *call log* sheet, with some 
 	extra details saved in the *call details* sheet.__

    
## PROJECT DESCRIPTION

The customer service managers would like to understand the activities of these call agents better. 
	Hence, this project seeks to achieve that through ETL (Extract-Transform-Load) process which involves 
	reading the dataset, cleaning and transforming the dataset 
 	to the desired form, model a datawarehouse which aids with the business KPI measurements and analysis.


## TOOLS 
    1. Python
    2. Pandas
    3. DrawSQL.io
    4. vscode



## PROCESS
 __Extraction__
 
        The call detail and call log sheets were provided in .csv format. The csv files are then read
		into a pandas dataframe in a python Jupyter notebook.
        Also created a copy of both extracted files to aid easy revert and recovery in case of errors.

 __Cleaning and Transformation__
 
        The dataset was cleaning using pandas and python. The following cleaning and transformations were done in the column
		
            1. Merging the dataframes both extracted files on similar columns
                - converted the columns(callID and id) to the same datatypes(int)
                - merged dataframes on both columns using pandas merge
            2. cleaned the inconsistencies in string columns
                -established consistency in callType, status columns
                - 
            3. Filling NaN values
                - In a case where a call was not assigned to an agent, the customer manager advised we adopt the agentID who answered the call. 
                - Filling the datetime and timestamps. 

**Datawarehouse Modelling**

        The transformed dataset will be loaded into a datawarehouse for analysis. inorder to accomplish this, 
        I modelled a star datawarehouse schema based on the transformed data.
        



## DATAWAREHOUSE SCHEMA

WeServe DW Modelling

![DW star modelling](https://github.com/Jooy04/WeServe/blob/871890e928233d58eb925c89715be643eb4b7cb6/WeServe%20DW%20Modelling.PNG)





## KPI RESULTS

