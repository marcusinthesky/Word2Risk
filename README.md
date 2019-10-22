# UCTFinanceHonsProject

## Introduction
### Topic
This project aims to investigate the use of natural language in stock market prediction.  Stock analysts rely on a mosaic of information when analysing the stock market, this can include historic data on stock prices, news articules, financial statements and even social media platforms.  
  
  
### Contributions
We would like to thank 

## Setup
### Anaconda
Anaconda is used as the python package manager in this project.  Anaconda is a popular tool used in data science, with extensive documentation.  
[Anaconda Documentaton](https://conda.io/docs/user-guide/index.html)  
  
A YAML file is used to specify the packages used in this project and can be found in main directory.  
  
  
### JupyterLab
The project was made in JupyterLab, using an Ipython Notebook.  This allows for python code and markup[markdown] (https://daringfireball.net/projects/markdown/basics) codechunks, in python which can be exported to a range of formats including latex and html.  
[Jupyterlab Documentation](http://jupyterlab-tutorial.readthedocs.io/en/latest/)  
  
  
## Python
[Python](https://www.python.org/) is an open-source interpreted programming language which supports a number of different programming paradigms.  This project makes use of Python 3.6, a version of the language.  
  
  
### HPC
We would like to thank the University of Cape Town's High Performance Computing Centre for their gracious use of their fascilities.  For a more information visit their [website](http://hpc.uct.ac.za/).  
  
For more help on their documentation visit their help page or [this cheatsheet of useful commands](https://docs.loni.org/wiki/Useful_PBS_Commands).  

To start an interactive job:
```
qsub -I -l nodes=1:ppn=4:series600
```

In order to setup jupyterlab on the HPC, forwarding is used, as shown by [Iowa University](https://wiki.uiowa.edu/display/hpcdocs/Jupyter+notebook), using:
From inside the cluster  
```bash
module load python/anaconda-python-3.4
source activate hpc_GWRMAR002_36
jupyter lab --no-browser --port=8889 & ssh -R8888:localhost:8889 hex.uct.ac.za
```
  
Then from local machine  
```bash
ssh -L 8889:localhost:8888 USERNAME@hex.uct.ac.za
```





  
  
### 

