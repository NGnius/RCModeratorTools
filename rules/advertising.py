'''advertising.py is a rule for finding usernames containing urls, which is considered advertising'''

URL_ENDERS = ['com', 'net', 'org']

def matches(username):
    '''(str) -> bool
    Returns whether username breaks this rule (advertising in username)'''
    if '.' in username:
        if 'csgo' in username.lower(): # for the very special csgo trading companies with their special advertising strategies, I have a very special solution
            return True
        elif contains_url_end(username):
            return True
    else:
        return False

def contains_url_end(username):
    dot_index = username.index('.')
    user_end = username[dot_index+1:].lower()
    len_past_dot = len(user_end)
    for ender in URL_ENDERS:
        if len(ender)<=len_past_dot and ender==user_end[:len(ender)]:
            return True
    return False
