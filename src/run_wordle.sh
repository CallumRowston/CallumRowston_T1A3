!/bin/bash
echo "Welcome to PYWORDLE !"
echo "Checking if Python3 is installed..."
if [[ -x "$(command -v python3)" ]]
then
    pyv="$(python3 -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        echo "Python 3 is installed!"
    else
        echo "You don't have Python3 installed. Please go to: https://www.python.org/downloads/ and download and install the latest version, then try again." >&2
        exit
    fi 
fi

echo "Checking for a virtual environment..."
DIR=.venv
if [[ -d "$DIR" ]]
then
    echo "Found virtual environment!"
else
    echo "Virtual environment not found. Setting up a new one..."
    python3 -m venv .venv
fi

source .venv/bin/activate

echo "Checking pip is installed..."
if [[ -x "$(command -v pip)" ]]
then
    echo "pip is installed!"
else
    echo "pip is not installed. Installing pip..."
    python -m ensurepip --upgrade
fi

echo "Installing required packages..."
pip install -r requirements.txt
echo "Success! Starting game..."
python3 wordle_game.py
