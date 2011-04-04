Introduction
============

`cmdline_tweet` is a simple Python application that allows you to send messages
to a Twitter account from the command line. It extends on the examples from
Jeff Miller's [tutorial on the subject][1] by improving reusability since the
same tool handles both authorization and tweeting.

This tool allows you to create command-line programs tied to a single Twitter
account with all the authorization, etc., handled behind the scenes.

Setup
=====

Using `cmdline_tweet` first requires [registering an app with Twitter][2] to
obtain an OAuth consumer key and secret. This is a one-time step, so just open
up `tweet.py` and replace `__CONSUMER_KEY__` and `__CONSUMER_SECRET__` with
your strings and forget about it.

The included `Makefile` may be used to bundle `tweet.py` into a standalone
binary with [PyInstaller][3], and only requires
specifying the paths to PyInstaller and the Python executable on your system.
Having standalone binaries can be helpful when deploying to machines without
Python installed.

Usage
=====

Each script/executable is tied to a single Twitter account, and all it does
is send a tweet on behalf of that account. This can be useful for server logs
or monitoring other automated processes. Or, simply issuing tweets without
leaving the comfort of the shell environment.

When first run, the program checks for a configuration file with the same name
and path as itself. For instance, if the script was `/path/to/tweet.py`, then
it would look for `/path/to/tweet.py.cfg`. If that file is invalid or can't be
found, then the program opens up a browser window for you to authorize it with
your Twitter credentials. Once that step is complete, tweeting is as simple as:

    ./tweet.py "All your base are belong to us"

If everything succeeds, the tweet will be posted and the script exits with no
output. If there was an error (e.g. repeat tweet, network failure), it will be
printed to standard output. Deleting the `.cfg` file or renaming the executable
will re-trigger the setup process. This makes it possible to have several
scripts which tweet to different accounts live side-by-side without conflict.

If you'll be using the script in a headless/server environment, you'll want to
copy the `.cfg` file from another machine with web browsing capabilities.

Dependencies
============

- Python >= 2.7 (only minor changes required for further compatibility)
- [tweepy][4]

[1]: http://jeffmiller.github.com/2010/05/31/twitter-from-the-command-line-in-python-using-oauth
[2]: http://dev.twitter.com/apps
[3]: http://www.pyinstaller.org/
[4]: https://github.com/joshthecoder/tweepy

TODO
====

Ideas for future improvement:

- Better backwards/forwards compatibility
- Have `Makefile` call `sed` to replace the appropriate, app-specific params?
- Integrate consumer key/secret into config file instead of hard-coding?
- Tweet to multiple accounts with same script/executable? (e.g. `./tweet.py 
  ACCTNAME MESSAGE`)
