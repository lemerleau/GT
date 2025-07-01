# Calcul Mathématique et la programmation en Python

Ce repertoir contient tout le matériel utiliser pour le cours
d'introduction au calcul mathematique avec Python et SageMath.
## Table de matière
  - [Organisation du
    répertoire](#organisation-du-répertoire)
  - [Prérequis](#prérequis)
  - [Installation des
    prérequis](#installation-des-prérequis)
  - [Get started](#get-started)
  - [Contact](#contact)
  - [References](#references)

## Organisation du répertoire

``` bash.
├── codes
│   ├── pyscripts Ce reportoire contient deux scripts python.
│   │   ├── sqrt_hw1.py # TAF: remplacer tous les None dans ce code par des bout de codes qui permettent de faire fonctioner le programe principal. 
│   │   └── sympy_basic.py # Structure simple d'un scripe python qui appele la librarie sympy.
│   ├── sageMath
│   ├── notebooks
│   │   ├── Intro_Python.ipynb # Jupyter notebook pour la partie introductive à python.
│   │   └── sympy_tutorial.ipynb # Jupyter notebook qui contient tous le code utilisé dans le cours d'introduction à sympy.
├── LICENSE
├── README.md
├── slides
│   ├── CIMPA_Burkina.pdf # the fichier pdf presenté en classe.
│   ├── CIMPA_Burkina.tex # le code latex pour generer le fichier pdf.
│   └── images # les images necessaires pour la compilation du code latex.
│       ├── LibrayMUC.png
│       ├── MPI-Logo.pdf
└── thirdpart
    └── miniconda.exe # Le programe executable miniconda pour les ordinateurs 
```

## Prérequis

Pour être capable d'executer la majorité des codes dans ce repertoire,
vous aurez besoin des logiciel suivant:

- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git?adobe_mc=MCMID%3D53435949000300021972311465250106216512%7CMCORGID%3DA8833BC75245AF9E0A490D4D%2540AdobeOrg%7CTS%3D1736698927)
- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- [Sage Math 10.6](https://www.sagemath.org/)
- [Sympy](https://www.sympy.org/en/index.html)
- [Homebrew](https://brew.sh/): Gestionaire de packets pour les utilisateurs Mac.
- [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install#quick-command-line-install)
- [Pip](https://pypi.org/project/pip/): Gestionaire de packets ``Python`` de manière générale. 

## Installation des prérequis

- Installer ``git``: 
	- sur Linux:
	
	```
	$ sudo apt install git-all
	$ git --version
	```
	- sur Windows: telecharger Git sur le lien [GitLink](https://git-scm.com/download/win and the download will start automatically)
	- sur Mac: saisir simplement la commande suivante
	``git --version
	``

- Installer ``conda`` 
	- 	sur Windows:

	```
	$ curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o .\miniconda.exe
	$ start /wait "" .\miniconda.exe /S
	$ del .\miniconda.exe
	
	```

	-  sur Mac:

	```
	$ mkdir -p ~/miniconda3
	$ curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/miniconda3/miniconda.sh
	$ bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
	$ rm ~/miniconda3/miniconda.sh
	
	```

	- Linux (Ubuntu inclus):

	```
	$ mkdir -p ~/miniconda3
	$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
	$ bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
	$ rm ~/miniconda3/miniconda.sh
	```

- Créer notre environnement de travail sage: 

	``` 
	$ conda config --add channels conda-forge 
	$ conda create --name sage python=3.11 
	$ conda activate sage
	$ sage --version 
	
	```

- Installer ``sympy`` dans notre environnement sage

	```
	$ conda activate sage 
	$ pip install sympy
	
	```

- Installer ``jupyter notebook`` et ``ipython``dans notre environement sage

	```
	$ conda activate sage 
	$ pip install ipython
	$ pip install notebook
	$ jupyter notebook
	
	```
- Ajouter notre environnement sage à jupyter: 

	```
	$ python -m ipykernel install --user --name sage --display-name sage
	```

NB: Pour les utilisateur windows, vous devrez utiliser ce [Link](https://www.sagemath.org/download-windows.html) pour installer sageMath. 

## Get started
1. Cloner le repertoire sur votre ordinateur 

	```
	$ git clone https://github.com/lemerleau/GT.git
	$ cd GT
	```
2. Naviger dans votre ``jupyter notebook`` pour ouvrir les fichiers notebook situé dans ``/GT/Codes/<--- ici``. 

## Contact
If you have any questions about this class's content or problems running this code, please contact me at [cyrillecardinale@gmail.com](mailto:cyrillecardinale@gmail.com.?subject=[GitHub]%20CART%20Lecture%20Material) 

## References
<a id="1" href="https://docs.sympy.org/latest/tutorials/intro-tutorial/calculus.html#limits">[1] Calculus and Sympy</a> 

<a id ="2" href="https://docs.sympy.org/latest/tutorials/physics/mechanics/index.html">[2] Mecanique classique sur Sympy</a>

