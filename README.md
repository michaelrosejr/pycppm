# pycppm


## Setup

To start using this module, you'll need to copy the *config.yml.sample* to 
*config.yml*. Then edit config.yml with the necessary information for your 
Clearpass server. 

Once the file is created, you'll need to edit the *sampleqry.py* file and change 
*login=0* to 1. This will make the script download a new token. Once downloaded,
you'll need to change this back to *login=0*. In futur versions this should be 
done through a method call but for now, this is the process.


