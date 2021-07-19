# GPManager

GPManager is a password manager made with python. The idea behind it is to host your password manager yourself, so you control everything about it.

It can be easily used as a backend for a password manager app or just as is.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cryptography. 

```bash
pip3 install cryptography
```
Once that dependency is installed, you can use the script as said in usage
## Usage

```bash
Usage: GPManager <command>

Commands:
create: create database
trash: delete database
add <name> <url> <username> <password>: add new entry to database
load <name>: load url and open it in brave browser
get <name>: get password for name
delete <name>: delete entry from database
print: print all names
newkey: generate and print new key
```

## Author - Greg Rabago

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://gregrabago-portfolio.herokuapp.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/gregrabago)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/greg_0109)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)