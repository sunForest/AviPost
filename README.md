# AviPost

[![Circle CI](https://circleci.com/gh/sunForest/AviPost.svg?style=shield)](https://circleci.com/gh/sunForest/AviPost)[![Coverage Status](https://coveralls.io/repos/sunForest/AviPost/badge.svg?branch=master)](https://coveralls.io/r/sunForest/AviPost?branch=master)


## Build Instruction for Development
------in progress------

1. install PostgreSQL, python (2.7 or 3.4), git and pip 
2. install virtualenv  
  ```
  sudo pip install virtualenv
  ```
3. create an isolated python environment  
  `virtualenv [dirName]`   
  `source [dirName]/bin/activate`     
4. glone the git repository   
  `cd [dirName]`   
  `git clone https://github.com/sunForest/AviPost.git` 
  `cd AviPost`
5. install python dependencies
  `pip install requirements/dev.txt`  
6. create your own setting file and change the database config (e.g. avipost/settings/dev_ssen.py). There are two ways to use your own setting file:
  * change the `DJANGO_SETTINGS_MODULE` value in manage.py (but don't commit it back to the repo)
  * add `--settings=avipost.settings.dev_xx` to all the python manage.py commands
7. create tables in your database  
  `python manage.py migrate`

