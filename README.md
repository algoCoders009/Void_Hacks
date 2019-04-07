# Void_Hacks
Imhotep is a healthcare analysis app, rudimentarily it discusses the impact of a number of diseases, based on the datasets from open and government sources.


Version 1:
This desktop application gives you an analysis on the whether you have disease or not based on the input set result.  
The application also has a section which displays a threat level of a particular disease all over the country state wise.
This data is beneficial when assigning medical resources to a state and determining their medical needs.

Steps to use the application: 
Run the API by executing the command python api.py in the console.

Flask server will be created which can access the ML Model.

Access the Web UI (Dashboard) and proceed to use.

In the Web UI Page, a prediction model of diabetes is set up which can predict whether a person has or not based on the 
input values.

Alternatively, enter the server sddress http://127.0.0.1/12345 in your browser to access it.
The output will be in the form of binary (0 or 1)

1 - Person has
0 - Person does not have

The Flagged map of a flu breakout and its descriptive analysis can be accessed on the following page :
https://www.google.com/maps/d/u/0/embed?mid=1ECmLbauOoxGxYuTTuEGcHWVICDSaXgML

Important note : The web UI connections have not been defined and may faulter.

