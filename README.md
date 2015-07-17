# submit_cli-automator
This python utility automatically uploads your assignment to tux and will submit the assignment for you with the information you provide

This script uses 2 libraries:

1. [paramiko](http://www.paramiko.org/)
2. [scp for paramiko](https://github.com/jbardin/scp.py) 

##To Setup:
1. Make sure you have [pip installed](https://pip.pypa.io/en/latest/installing.html#install-pip)
2. Download/clone repository
3. cd into the newly cloned/downloaded repository and run `sudo python setup.py install` (sudo is necessary for pip to install the 2 above libraries this script depends on to run)

##Example Usage:

`python submit.py "/path/to/local/work" "/path/to/upload/to/tux"`

The arguments:
The local path can be a file or director
The path where you want it on tux can be directories that don't exist...yet



