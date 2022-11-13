# Data appendix
All files from /AnalysisData/ are described here.

##  pew.csv
This file contains part of information extracted from original data. Only info about confessed religion and range of annual income are kept.
For each there is one appropriate column, sorted by confessed religion.  
\
Variables:
- reltrad - categorical variable; confessed religion by each participant. 30508 tagged observation + 5048 tagged as unaffiliated. 
- income - categorical variable; annual income of each participant, declared as a range. 29435 tagged answers+ 6121 missing (participants refused answer)

**Details (categories, frequency table and bar charts)** are available in **/CommandFiles/lab2.ipynb**

## pew_cum.csv
This file contains cumulated information from pew.csv. Each pair (religion, income) has additional variable 'counts', so
at all it does not include any new information in comparison to 'pew.csv'
