# ccdetect
A very simple multichannel time-domain correlation detector  

You need all input files to be in SAC format with a single channel per file.  
All channels should have the same sampling rate.  
All template files must have the same number of samples (*NTEMP*) and all target files must have the same number of samples (*NTARG*).  
The program will then loop around the specified template and target pairs and generate a correlation trace for each.  
At present, it only outputs the top trace as a SAC file (with *NTEMP + NTARG - 1* samples) and time-stamp set the same as the
time-stamp for the target files.  

At a later date, I may want to write out the single channel correlation traces and/or perform calculations on them.  
But for now, this should be sufficient just to indicate a detection.  

The program was modified from the *ccdtest* program so there are a lot of redundant variables in the current code.  
These should be cleaned up.  

Simply specify an input file of the form:  
```
FS  2.0    8.0   4   2
FS  4.0   12.0   4   2
WF template/H01_KEV_BHE.sac      target/H02_KEV_BHE.sac 
WF template/H01_KEV_BHN.sac      target/H02_KEV_BHN.sac 
WF template/H01_KEV_BHZ.sac      target/H02_KEV_BHZ.sac
```
where each line beginning *FS* is a filter specification and every line beginning *WF* is a waveform pair specification.  
For lines labelled FS, the numbers are  

(a) low frequency (Hz)  
(b) high frequency (Hz)  
(c) order (integer)  
(d) number of passes (see XAPIIR documentation for all these parameters)  

You then execute the program with a short script, e.g.  
```
#!/bin/sh
icc=2
./ccdetect $icc < ccdetect.input
```
where icc can take the values 1, 2, 3, or 4:  
```
icc = 1    -->   CC
icc = 2    -->   CC * | CC |
icc = 3    -->   PCC
icc = 4    -->   PCC * | PCC |
```
