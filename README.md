# ccdetect
A very simple multichannel time-domain correlation detector  

ccdetect v1.0.0 (March 2, 2026) is permanently archived on Zenodo with DOI: 10.5281/zenodo.18835809  
 
[![DOI](https://zenodo.org/badge/1165112440.svg)](https://zenodo.org/doi/10.5281/zenodo.18835809) 

https://doi.org/10.5281/zenodo.18835809  

[![SQAaaS badge shields.io](https://img.shields.io/badge/sqaaas%20software-bronze-e6ae77)](https://api.eu.badgr.io/public/assertions/qd8AzoBVQjKMPJarBej1MA "SQAaaS bronze badge achieved")

[![SQAaaS badge](https://github.com/EOSC-synergy/SQAaaS/raw/master/badges/badges_150x116/badge_software_bronze.png)](https://api.eu.badgr.io/public/assertions/qd8AzoBVQjKMPJarBej1MA "SQAaaS bronze badge achieved")

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



This program requires SAC and uses the XAPIIR library (Harris, 1990).  
This whole library is provided in the single source file XAPIIR.f.    
(The XAPIIR routines are entirely third party software.)  

The basic algorithm is that described by Gibbons and Ringdal (2006).  
I recommend using icc = 2 or icc = 4 for the CC * | CC | versions, for the reasons given by Gibbons (2022).  


References:  

Gibbons, S. J. and Ringdal, F. (2006). The detection of low magnitude seismic events using array-based waveform correlation. *Geophysical Journal International*, **165**, 149– 166. https://doi.org/10.1111/j.1365-246X.2006.02865.x  
Gibbons S. J. (2022). The Optimal Correlation Detector? *Geophysical Journal International*, **228**, Issue 1, 355–365 doi: 10.1093/gji/ggab344  
Harris, David. XAPiir: A recursive digital filtering package, report, September 21, 1990; California.  
(https://digital.library.unt.edu/ark:/67531/metadc1203741/m1/1/: accessed November 5, 2023),  
University of North Texas Libraries, UNT Digital Library,  
https://digital.library.unt.edu; crediting UNT Libraries Government Documents Department.  
