# Calcul Mathématique et la programmation en Python

Ce repertoir contient tout le matériel utiliser pour le cours d'introduction au calcul mathematique avec Python et SageMath. 

## Prérequis 
Pour être capable d'executer la majorité des codes dans ce repertoire, vous aurez besoin des logiciel suivant: 

- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- [Sage Math 10.6](https://www.sagemath.org/)
* [Sympy](https://www.sympy.org/en/index.html)
* [Homebrew](https://brew.sh/) package manager for Mac users
* [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install#quick-command-line-install)
* [Pip: gestionaire de packets python](https://pypi.org/project/pip/)

## Installation des prérequis

- Installer conda sur Windows.

```
$ curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o .\miniconda.exe
$ start /wait "" .\miniconda.exe /S
$ del .\miniconda.exe

```

- Installer sur Mac.

```
$ mkdir -p ~/miniconda3
$ curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/miniconda3/miniconda.sh
$ bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
$ rm ~/miniconda3/miniconda.sh

```

- Installer sur Linux (Ubuntu inclus). 

```
$ mkdir -p ~/miniconda3
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
$ bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
$ rm ~/miniconda3/miniconda.sh
```

- Créer notre environement de travail sage. 

``` 
$ conda config --add channels conda-forge 
$ conda create --name sage python=3.11 
$ conda activate sage
$ sage --version 

```

- Installer ``sympy`` dans notre environement sage

```
$ conda activate sage 
$ pip install sympy

```

NB: Pour les utilisateur windows, vous devrez utiliser ce [Link](https://www.sagemath.org/download-windows.html) pour installer sageMath. 

## Organisation du répertoire
```bash
.
├── Codes ## Codes for the 
│   ├── Intro_Python.ipynb
│   ├── Pyscripts
│   ├── sageMath
│   └── sympy_tutorial.ipynb
├── LICENSE
├── README.md
├── Slides
│   ├── CIMPA_Burkina.pdf
│   ├── CIMPA_Burkina.tex
│   └── images
└── thirdpart
    └── miniconda.exe 
```
## Contact
If you have any questions about this class's content or problems running this code, please contact me at [cyrillecardinale@gmail.com](mailto:cyrillecardinale@gmail.com.?subject=[GitHub]%20CART%20Lecture%20Material) 

## References
<a id="1" href="https://docs.sympy.org/latest/tutorials/intro-tutorial/calculus.html#limits">[1] Calculus and Sympy</a> 

<a id ="2" href="https://docs.sympy.org/latest/tutorials/physics/mechanics/index.html">[2] Mecanique classique sur Sympy</a>

