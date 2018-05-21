# Mexican Broadsides Data Exploration 

This repo contains the notebooks and relevant data for the Mexican Broadsides Collection. The workflow is quite complicated, but generally speaking the goal is to take existing MARC data in our OPAC, Roger, and get that into the Digital Collections  

The exploration comes across the steps organically, but specifically, the steps are:  

* Find the 'bib numbers' for the Roger items with `directory_script.py`. These numbers serve as the unique IDs/primary keys for objects. They are found and produced by scanning the directory structure on a network drive, since every object is contained within a directory named after the bib number.  
* Enter the bare listing of bib numbers into a DAMS Manager tool that takes bib numbers to get Roger MARC data, transform it to MODS, then transforms it to align closer with the DAMS data model, and finally produces a csv of the data.   
* In a separate wokflow, the bib numbers were run in an OCLC tool to get FAST subjects from existing MARC LCSH subjects. I received that data as a csv which needs to be integrated with the data in the previous step. This is done by using both csv sources as dataFrames and merging them along the bib column.  
* Note: at different stages, the existing data is cleaned in OpenRefine. Linked data relies on clean data!  
