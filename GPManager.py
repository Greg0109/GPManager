#!/usr/bin/env python3
from cryptography.fernet import Fernet
import os
import json
import socket
import sys


folder = '/PATH/TO/GPMANAGER/FOLDER'
if not os.path.exists(folder):
    os.makedirs(folder)
key = ""
keyfile = folder + '/key.txt'
jsonfile = folder + '/database.json'
encryptedDatabase = folder + '/database.json.enc'

def write_key():
    key = Fernet.generate_key()
    return key

def load_key(key):
    if len(key) == 4: # so is file
        if os.path.exists(keyfile):
            with open(keyfile, 'rb') as f:
                key = f.read()
            return key
        else:
            key = load_key(write_key())
            return key
    else:
        return key

def delete_json_database():
    if os.path.exists(jsonfile):
        os.remove(jsonfile)
    if os.path.exists(encryptedDatabase):
        os.remove(encryptedDatabase)

def encrypt(filename, key):
    with open(filename, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(filename + '.enc', 'wb') as f:
        f.write(encrypted)

def decrypt(filename, key):
    with open(filename, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    with open(filename[:-4], 'wb') as f:
        f.write(decrypted)

def encryptMessage(message, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return encrypted

def decryptMessage(message, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(message)
    return decrypted

def create_json_database():
    with open(jsonfile, 'w') as f:
        json.dump({}, f)
    encrypt(jsonfile, load_key(key))
    delete_json_database()

def read_json_database():
    if os.path.exists(encryptedDatabase):
        decrypt(encryptedDatabase, load_key(key))
        with open(jsonfile, 'r') as f:
            delete_json_database()
            return json.load(f)
    else:
        create_json_database()
        return {}

def save_json_database(database):
    if os.path.exists(encryptedDatabase):
        decrypt(encryptedDatabase, load_key(key))
        with open(jsonfile, 'w') as f:
            json.dump(database, f)
    else:
        create_json_database()
        save_json_database(database)
    encrypt(jsonfile, load_key(key))
    delete_json_database()

def add_entry(name, url='Empty', username='Empty', password='Empty'):
    database = read_json_database()
    database[name] = {'url': url, 'username': username, 'password': password}
    with open(jsonfile, 'w') as f:
        json.dump(database, f)
    save_json_database(database)

def delete_entry(name):
    database = read_json_database()
    del database[name]
    with open(jsonfile, 'w') as f:
        json.dump(database, f)
    save_json_database(database)

def get_password(name):
    database = read_json_database()
    return database[name]['password']

def get_url(name):
    database = read_json_database()
    return database[name]['url']

def load_url(name):
    password = get_password(name)
    url = get_url(name)
    os.system('brave ' + url)
    os.system('echo ' + password + ' | xclip -selection clipboard')

def print_names():
    database = read_json_database()
    for name in database:
        print(name)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: GPManager <command>')
        print('\n' + 'Commands:')
        print('create: create database')
        print('trash: delete database')
        print('add <name> <url> <username> <password>: add new entry to database')
        print('load <name>: load url and open it in brave browser')
        print('get <name>: get password for name')
        print('delete <name>: delete entry from database')
        print('print: print all names')
        print('newkey: generate and print new key')
    else:
        key = load_key(sys.argv[-1])

        if sys.argv[1] == 'create':
            create_json_database()
        elif sys.argv[1] == 'trash':
            delete_json_database()
        elif sys.argv[1] == 'add':
            name = sys.argv[2]
            url = sys.argv[3]
            username = sys.argv[4]
            password = sys.argv[5]
            add_entry(name, url, username, password)
        elif sys.argv[1] == 'delete':
            name = sys.argv[2]
            delete_entry(name)
        elif sys.argv[1] == 'load':
            name = sys.argv[2]
            load_url(name)
        elif sys.argv[1] == 'get':
            name = sys.argv[2]
            password = get_password(name)
            print(password)
        elif sys.argv[1] == 'print':
            print_names()
        elif sys.argv[1] == 'newkey':
            write_key()