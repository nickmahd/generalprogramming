import os
import time
import numpy

os.chdir(os.path.dirname(os.path.abspath(__file__)))

DRY_RUN     = 0
WIPE_LOGS   = 0
WIPE_DATA   = 0
QUICK_RUN   = 0
LOG_LEVEL   = "INFO"

TIMEOUT_SECS   = 10
POST_GET_LIMIT = 5


POST_PICKUPS = [60 ** (QUICK_RUN ^ 1) * x for x in [1/12, 1/6, 1/3, 1/2, 3/4, 1,
                                                    2, 5, 10, 15, 24,
                                                    30, 36, 42, 48, 60, 72]]  # Minutes/hours

DATAFILE = os.path.abspath('../data/data.csv')
LOGFILE  = os.path.abspath('../data/log.log')

SUBREDDIT = 'pics'  # TODO: multiple subreddits

CLIENT_ID     = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
PASSWORD      = os.environ['BOT_PASSWORD']
USERNAME      = os.environ['BOT_USERNAME']
USER_AGENT    = os.environ['USER_AGENT']

TIMEOUTS = [2, 5, 10, 15, 20, 30, 60]

ATTR   = ['id',
          'num_comments',
          'title',
          'selftext',
          'author',
          'created_utc',
          'score',
          'upvote_ratio',
          'edited',
          'stickied',
          'locked'
          ]

S_ATTR = ['active_user_count',
          'subscribers'
          ]

# ----------------------------------------------------- #

if not os.path.isdir("../data"):
    os.mkdir("../data")

if (not os.path.isfile(LOGFILE)) or WIPE_LOGS:
    open(LOGFILE, 'w+').close()

if (not os.path.isfile(DATAFILE)) or WIPE_DATA:
    open(DATAFILE, 'w+').close()

if os.path.getsize("../data/log.log") != 0:
    logname = '../data/log-' + str(int(time.time())) + '.log'
    open(logname, 'a').close()
    LOGFILE = os.path.abspath('../data/' + logname)

if os.path.getsize("../data/data.csv") != 0:
    logname = '../data/data-' + str(int(time.time())) + '.csv'
    open(logname, 'a').close()
    DATAFILE = os.path.abspath('../data/' + logname)
