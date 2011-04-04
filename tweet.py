#!/usr/bin/env python
"""A simple, reusable command-line twitter client.

Inspired by the example from Jeff Miller at:
http://jeffmiller.github.com/2010/05/31/twitter-from-the-command-line-in-python-using-oauth
    
"""

import os
import sys
import webbrowser
import ConfigParser

import tweepy

CONSUMER_KEY = '__CONSUMER_KEY__'
CONSUMER_SECRET = '__CONSUMER_SECRET__'
CONFIG_FILE = os.path.join(os.path.dirname(__file__), 
                           "{}.cfg".format(sys.argv[0]))

def tweet(message, access_key, access_secret):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    try:
        api.update_status(sys.argv[1])
    except tweepy.error.TweepError as e:
        print e
        sys.exit(1)

def setup():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth_url = auth.get_authorization_url()
    print "Opening Twitter to get user authorization..."
    print auth_url
    webbrowser.open(auth_url)
    
    verifier = raw_input('Verification PIN: ').strip()
    auth.get_access_token(verifier)
    
    config = ConfigParser.RawConfigParser()
    config.add_section('OAuth')
    config.set('OAuth', 'access_key', auth.access_token.key)
    config.set('OAuth', 'access_secret', auth.access_token.secret)
    with open(CONFIG_FILE, 'wb') as f:
        config.write(f)
    
    print "Setup complete."
    print "You may now tweet using: {} MESSAGE\n".format(sys.argv[0])
    

if __name__ == '__main__':
    config = ConfigParser.RawConfigParser()
    config.read(CONFIG_FILE)
    try:
        access_key = config.get('OAuth', 'access_key')
        access_secret = config.get('OAuth', 'access_secret')
    except ConfigParser.Error:
        print "Bad/missing settings file '{}'".format(CONFIG_FILE)
        setup()
        sys.exit()
    if len(sys.argv) > 1:
        tweet(' '.join(sys.argv[1:]), access_key, access_secret)
    else:
        print "usage: {} MESSAGE\n".format(sys.argv[0])
        print "Settings are read from '{}'".format(CONFIG_FILE)
        print "Deleting this file will reset the current configuration"
