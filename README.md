# chinese-cookie
Fortune cookie generator.

### Requirements
* Python >=3.5.x (For API Star)
* Node >=6.9.x and NPM >=3.x.x (For Angular CLI)

### Run API Backend (Development)
```
cd <project directory>/api

# install the requirements
pip install -r ./requirements/local.txt

# create the database tables
apistar create_tables

# load the fixtures
apistar load_fortunes fixtures/fortunes.txt

# run the server
apistar run
```

### Run Web App (Development)
```
cd <project directory>/web

# install the requirements
npm install

# run the server
ng serve
```

### Licensing

MIT. Take, adapt, use. A link back to this repo is appreciated.
