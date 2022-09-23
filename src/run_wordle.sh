#!/bin/bash
echo "Welcome to PYWORDLE !"
echo "Checking if Python3 is installed..."
if [[ -x "$(command -v python)" ]]
then
    pyversion="$(python3 -V 2>&1)"
    if [[ $pyversion == "Python 3"* ]]
    then
        echo "Python 3 is installed!"
        echo "Checking pip is installed..."
        if [[ -x "$(command -v pip)" ]]
        then
            echo "pip is installed!"
            echo "Installing required packages..."
            pip install -r requirements.txt
        fi
    else
        echo "You've got the wrong version of Python. Please update by going to: https://www.python.org/downloads/ and downloading and installing the latest version." >&2
    fi 
else
    echo "You don't have Python installed. Please go to: https://www.python.org/downloads/ and download and install the latest version." >&2
fi
