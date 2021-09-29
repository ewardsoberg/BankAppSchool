<center><h1>BankAppSchool</h1></center>
<!-- TABLE OF CONTENTS -->

<!--ts-->
## Table of Contents ##
* [Background](#background)
* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Made by](#made-by)
<!--te-->

## Background ##
School assignment. Create a simple bank application using python classes, and then do the same without classes.

<!-- ABOUT THE PROJECT -->
## About The Project
The project Builds a Mysql database with sqlalchemy using orm. The MySQL part is built on a Multilayered structure (UI, BL, DATA) Where the user communicates with UI.

### Built With
* [sqlalchemy](https://www.sqlalchemy.org/)

<!-- GETTING STARTED -->
## Getting Started

Follow the [installation](#installation) to get started

### Prerequisites

* Python 3+
* Docker
* Docker-compose

### Installation

1. Clone the repo
```sh
git clone https://github.com/ewardsoberg/BankAppSchool.git
```
2. Install requirements
```sh
pip install requirements.txt 
```
3. start docker containers
```sh
docker-compose up
```
4. run init_db() in app/MySQL/db/data_generator/generate_data_models.py
5. run populate_database() in app/MySQL/db/data_generator/generate_data_models.py
6. Done


<!-- USAGE EXAMPLES -->
## Made by
Måns Ewards Öberg
