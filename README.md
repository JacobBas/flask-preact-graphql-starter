# Flask Preact GraphQL Starter Project
The purpose of this repo is to be used as a starting point for an application that is leveraging Flask, Preact.js, and GraphQL as its tech stack. This project structure is best used whe creating a single page web applications.

## Project structure
The general project structure is given below where this can be expanded apon to create a more complex application.
```
├── app.py
├── _backend
│   ├── _graphql
│   │   ├── __init__.py
│   │   ├── objects.py
│   │   └── schema.py
│   └── __init__.py
├── _database
│   ├── __init__.py
│   └── models.py
├── _frontend
│   ├── index.html
│   └── static
│       └── index.js
├── bash
│   ├── run_dev.sh
│   └── run_prod.sh
├── README.md
└── requirements.txt
```

## How to use
The structure of this project has been built out to separate the Frontend, Backend, and Database fully from each other while giving the framework to allow them to talk.

### Frontend
The frontend for this application is leveraging the Preact.js framework which is a smaller, faster alternative to using React.js. While it does not contain the full extent of React.js functionality, it has enough for most application to run.

We are also using an alternative to JSX called HTM which mimics JSX without the need for a compiler to convert from JSX to JavaScript.

The purpose of using this frontend frame work is to keep the size of the used modules to a minimum while also removing the reliance from Node.js. These requirements have come from personal experience and difficulty of configuring these technologies in a proffesional environment.

### Backend
The backend makes heavy use of Python and the Flask framework. Flask has been choosen since it is lightweight and flexible enough to make powerful applications that configure to the project and developer needs.

GraphQL is used in most cases to communicate between the Database and Front end since it allows for a ton of flexibility once implemented.

### Database
The database for this project is preconfigured as an SQLite database but since we are using the SQLAlchemy module from Python, this can be updated to nearly any other SQL driver.

Not much other configuration should be needed for the database other than changing the location of the database.