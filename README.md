ReSt: The REal STealth MITM Tool
================================

##What?
ReSt is a tool for Stealth MITM attacks, 

##When?
ReSt is released during [NullCon'13](http://www.nullcon.net/) International Security Conference.
It features functionalities of `Stealth MITM` and `Semi Stealth MITM`.

##How?

ReSt is written in `Python` (2.7) relying on `PyQt` for GUI. It's a bi-threaded application which creates a one thread
for network activity and another for the GUI. It uses `scapy' python library for packet crafting.

##Working
To run the software,

* First `download` the tool from the repository (Git Clone/Download ZIP)
* `cd` to the extracted files directory
* `run` the following command in the terminal

>```
$ sudo python ./main.py
```

##License
Please refer to LICENSE.md file in the current directory.
