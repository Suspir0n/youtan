#  Desafio Youtan - ACME

## Description

Youtan gave me a practical challenge for a vacancy I'm participating in, and this challenge consists of creating a screen application with Python, using Django with MVT.

## Starting

To run the project, you will need to install the following programs:

- [Python: Required to create the project](https://www.python.org/downloads/)
- [Docker: Required to create the containers](https://www.docker.com/)
- [VS Code: For project development](https://code.visualstudio.com/)

## ⌨️ Development

Use Gitpod, a free online dev environment for GitHub.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Suspir0n/jobhood.git)

Or use code locally using:
```
$ cd "directory of your choice"
$ git clone https://github.com/Suspir0n/desafio-youtan.git
```

### Construction

To build the django application, execute the commands below:

```
$ pip install -r requirements.txt
```

These are the requirements.txt dependencies:

```
asgiref==3.7.2
Django==4.2.1
python-dotenv==1.0.0
sqlparse==0.4.4
tzdata==2023.3
```

Make these settings so that your Django application works perfectly

use the file Dockerfile

### Run Docker
```
$ docker-compose up --build -d
```

## Run Tests with coverage

```` 
pytest -v --cov --cov-report=term-missing --cov-fail-under=90
````

## Features


## Configuration

To execute the project, it is necessary to use VsCode or an IDE of your preference, so that it identifies the dependencies necessary for execution in the repository. Once the project is imported, it will be possible to test its functionality in real time.

## Contributions

Contributions are always welcome! I hope I have helped someone in need.

## 🔓 License
MIT © [Evandro Silva](https://www.linkedin.com/in/suspir0n/)