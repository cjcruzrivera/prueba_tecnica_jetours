README
======

The following service allows two functionalities, designed for the Je Tours Technical Test.

Software Requirements
=====================

In order to run this code is necessary to have installed the following packages
* Python + Python Dev 
	* `sudo apt-get install python-setuptools python-dev build-essential`
	* `sudo easy_install pip`
* Flask (`sudo pip install flask`)

Resources
=========

At this time the following resources are available

* *GET* **/ordenar** returns an ordered list in Json format of the numbers received as parameters
	* *GET* **/ordenar?1&3&7&9&10**

* *GET* **/contarMayusculas/\<path\>** returns a message with the amount of capital letters in the file. Or a message indicating the error in the path or the file:
	* *GET* **/contarMayusculas?ruta=c:/Users/Ipinnovatech/Documents/Camilo/Prueba/prueba.txt** 


Installation
============
Change permissions of `app.py` and run from command line `./app.py`.