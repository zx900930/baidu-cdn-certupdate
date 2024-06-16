# baidu-cdn-certupdate

Baidu cdn certificates auto update script

## Description

A python script that push ssl certificates to baidu cdn automatically.

## Installation

- Install python3: [https://wiki.python.org/moin/BeginnersGuide/Download](https://wiki.python.org/moin/BeginnersGuide/Download)
- Clone this project: `git clone https://github.com/zx900930/baidu-cdn-certupdate.git`
- Get into the project folder `cd baidu-cdn-certupdate`
- Install dependencies: `pip install -r requirements.txt`
- Edit enviroment variables: `mv example.env .env`

## Usage

### Using default .env file

`python3 baiducertificates.py`

### To use the script with an alternative .env file, run the following command in the terminal:

`python3 baiducertificates.py path/to/alternative.env`

## Support

Please use the issue tracker.

## Roadmap

- Docker images
- Cronjobs

## Contributing

Welcome to contribute to this project.

## License

GNU General Public License v3.0
