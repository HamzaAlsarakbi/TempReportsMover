# Temp Reports Mover
 
## General
[REPOSITORY LINK](https://github.com/HamzaAlsarakbi/TempReportsMover)
### TempReportsMover.py
Moves CMM reports from "Temp Results" folder on "C:/" drive to "Temp Results" in the "Measurement Results" folder on the "H:/" drive

### What consitutes as a CMM report?
- any PDF file in "Temp Results" folder


## Usage
To run the program in the background, double click the `RunSilently.bat` file.
To run the program with the console open, double click the `Run.bat` file.

# Configuration
All paremeters, such as scan interval, source folder and destination folder can be change in the `config.json ` file.
Note: when changing the source or destination directory, make sure you replace all "\" with "/"
For example, the below is unacceptable:
```
C:\Users\quality\documents\hamza\Coding\TempReportsMover
```
Instead do this:
```
C:/Users/quality/documents/hamza/Coding/TempReportsMover
```