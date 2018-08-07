'''Finds usernames in an output log and gets profile pictures from those usernames

CLI arguments should be provided in the following order:
<output log file>* <bad names output file>
*required'''


import requests, re, sys, traceback, importlib
from os.path import join, isfile
from os import listdir
import process_output_log

args = sys.argv # list of str; arguments from CLI
# NOTE: first item in args is the filename of this script

def load_rules(folder='./rules'):
    '''(str) -> list of modules
    Loads all rules in folder
    Returns list of rules'''
    rules = list()
    for item in listdir(folder):
        if isfile(join(folder, item)):
            module_name = folder.replace('.', '').replace('/', '.').replace('\\', '.').strip('. ') + '.' + item[:-len('.py')]
            rules.append(importlib.import_module(module_name))
    return rules

try:
    rules = load_rules()
except:
    traceback.print_exc() # debug
    rules = None

def find_bad_names(usernames, rules=rules):
    '''(iterable of str [, iterable of modules]) -> list of str
    Checks each username in usernames against some rules
    Returns all usernames which break at least one rule

    NOTE: if ./rules does not exist or does not contain valid rules, you must pass in rules'''
    if rules == None:
        raise ValueError('Rules parameter must be included; default rules not loaded properly')
    rule_breakers = list()
    for username in usernames:
        for rule in rules:
            if rule.matches(username):
                rule_breakers.append(username)
                break

    return rule_breakers



# start of actual stuff
if __name__=='__main__' and len(args)>1:
    # do stuff
    with open(args[1], 'r') as file:
        file_contents = file.readlines() # list of str; lines of the file

    print('Extracting usernames...')
    players = process_output_log.get_usernames(file_contents)
    process_output_log.save_usernames(players) # save usernames extracted from output file

    print('Finding bad names...')
    baddies = find_bad_names(players)
    filename = args[2] if len(args)>2 else './baddies_maybe.txt'
    process_output_log.save_usernames(baddies, filename=filename, append=False)
