# django_peliculas

## Prerequisites

```
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8
sudo apt install virtualenv

```

## step 1
Create virtual env for python, execute in terminal next commands:


```
mkdir ~/python-environments && cd ~/python-environments
virtualenv --python=python3 env
source env/bin/activate

```


## step 2
Enter the root folder of this repository and execute 
next command in terminal for install modules python

```
pip install -r requirements.txt

```


## step 3
Open directory 'drupMovieStore' enter in the folder and open terminal for execute next commands

```
source ~/python-environments/env/bin/activate
python manage.py makemigrations app
python manage.py migrate
python manage.py runserver

```

## step 4
Open navigator http://127.0.0.1:8000/init