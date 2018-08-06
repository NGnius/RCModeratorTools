'''CLI arguments should be provided in the following order:
<output log file> <profile picture folder>'''

import requests, re, sys, os
from os.path import join

args = sys.argv # list of str; arguments from CLI
# NOTE: first item in args is the filename

USERNAME_PFP_URL = r'http://images-pull.freejam.netdna-cdn.com/customavatar/Live/'
CLAN_PFP_URL = r'http://images-pull.freejam.netdna-cdn.com/clanavatar/Live/'

def get_usernames(contents):
    '''(list of str) -> set of str
    Extracts usernames from file contents, line by line
    Returns a set of usernames'''
    usernames = set()
    for line in contents:
        regexed = re.search(r"Player\s\'(\w+)\'", line, re.I)
        if regexed != None:
            usernames.add(regexed.group(1))
    return usernames

def save_usernames(usernames, filename=r'./usernames.txt', append=True):
    '''(set, str, bool) -> None
    Saves usernames to file; one per line'''

    if append:
        try:
            with open(filename, 'r') as file:
                file_contents = file.read()
        except FileNotFoundError:
            file_contents = ''
    else:
        file_contents = ''

    for username in usernames:
        if username+'\n' not in file_contents:
            file_contents+=username+'\n'

    with open(filename, 'w') as file:
        file.write(file_contents)

def get_PFPs(usernames):
    '''(set of str) -> dict str:byte
    Gets every username's profile picture (PFP) from the interwebz
    Returns dict associating username to PFP'''

    result = dict()
    for username in usernames:
        image_req = requests.get(USERNAME_PFP_URL+username)
        if image_req.status_code != 200:
            if image_req.status_code != 404: # non-custom avatars will give a 404, but other errors might be important
                print('Failed to load %s profile picture,' % username, 'error: %s' % image_req.status_code)
        else:
            result[username] = image_req.content

    return result

def save_PFPs(images, folder=None, ext='jpg'):
    '''(dict str:byte, str, str) -> None
    Write every image to file, with filename <images key>.<ext>'''
    if folder==None or not isinstance(folder, str):
        folder = r'./PFPs'
    if not os.path.exists(folder):
        os.makedirs(folder)

    for username in images:
        with open(join(folder,username+'.'+ext), 'wb') as file:
            file.write(images[username])


# start of actual stuff
with open(args[1], 'r') as file:
    file_contents = file.readlines() # list of str; lines of the file

print('Extracting usernames...')
players = get_usernames(file_contents)
save_usernames(players) # save usernames extracted from output file

print('Downloading profile pictures...')
PFPs = get_PFPs(players)
if len(args)<3:
    args.append(None)
save_PFPs(PFPs, folder=args[2]) # save profile pictures of all usernames to files
