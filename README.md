# DEPRECATED

This repository is deprecated. It was a first pass for a concept which I've since improved upon. It has a serious flaw in the content which badly mistmatches the majority of the readings.

Please head over to https://github.com/n33kos/iChingAPI for a php api version of this service which uses a sqlite API to store the data instead of hardcoding the text which makes mistakes much easier to correct


PhPyChing
=========
PhPyChing is an iChing reading generator written in python and deployed with a simple PHP interface. It currently utilizes the three coin casting method and generates a full reading with changing lines. The text is extracted from Richard Wilhelm’s and Cary F. Baynes’ translations.

### Usage (Web Interface) ###
1. Checkout repository.
2. Copy files to desired web directory (*PyChing.py* is not neccessary for web deployment).
3. Ensure that [Python 2][1] is installed on your webserver.
4. Navigate to web directory.


PyChing
=========
PyChing is an iChing reading generator written in python. It currently utilizes the three coin casting method and generates a full reading with changing lines. The text is extracted from Richard Wilhelm’s and Cary F. Baynes’ translations.

### Usage (Terminal Only) ###
1. Grab *PyChing.py*
2. Ensure that [Python 2][1] is installed on your system.
3. Open terminal and navigate to directory containing *PyChing.py*.
4. To generate a reading enter `./PyChing.py`
You can include a question as the first argument using `./PyChing.py {Question}`


[1]: https://www.python.org/        "Python 2"
