# Python Tutorials
This repository has the Python scripts I had created while learning/developing program in Python.


## Useful Comamnds
Below are some of the useful commands in Python

##### install pip if not already installed
sudo apt-get install python-pip

##### Upgrade your pip
python -m pip install --upgrade pip

##### view the modules installed in python
python -m Twisted # will give error for not existing modules
python -c "import <module>" # Error will be thrown if module is not installed

##### View all the modules installed
pip freeze
pip list

##### search a module to install
pip search <module>


##### install a python module
sudo apt-get install python-pysftp
python -c 'import pkgutil; print(1 if pkgutil.find_loader("pysftp) else 0)'
pip install pysftp

##### uninstall a module
pip uninstall twisted

##### To install a module downloaded, package should be unzipped if it is zipped
python setup.py install
pip install *.whl

## Reference
[CodingBat](https://codingbat.com/python)