# chinese-cookie
Fortune cookie generator.

### Requirements
* Python 3.5+ (For API Star)

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

### Licensing

MIT. Take, adapt, use. A link back to this repo is appreciated.
