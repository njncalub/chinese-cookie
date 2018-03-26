# chinese-cookie
Fortune cookie generator using [API Star](https://github.com/encode/apistar) and [Angular CLI](https://github.com/angular/angular-cli).

### Requirements
* Python >=3.5.x (For API Star)
* Node >=6.9.x and NPM >=3.x.x (For Angular CLI)

### Recommended
I recommend installing the following version managers to make your life easier:
* [pyenv](https://github.com/pyenv/pyenv)
* [nvm](https://github.com/creationix/nvm)

### Run API Backend
```
# navigate to the api directory
$ cd <project directory>/api

# install the requirements
$ pip install -r ./requirements/local.txt

# create the database tables
$ apistar create_tables

# load the fixtures
$ apistar load_fortunes fixtures/fortunes.txt

# run the server
$ apistar run
```

### Run Web App
```
# navigate to the web directory
$ cd <project directory>/web

# install the requirements
$ npm install

# run the server
$ ng serve
```

### Licensing
MIT. Take, adapt, use. A link back to this repo is appreciated.
