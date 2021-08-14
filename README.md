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
├── bash
│   ├── run_dev.sh
│   └── run_prod.sh
├── _database
│   ├── __init__.py
│   └── models.py
├── _frontend
│   ├── index.html
│   └── static
│       └── index.js
├── README.md
└── requirements.txt
```
