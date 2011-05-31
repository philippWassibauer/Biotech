import os
import socket
import sys

# Settings to configure manually
PORT = 8888
PROC_NAME = 'zweitwelt_gunicorn'
LOGFILE_NAME = 'gunicorn.log'
TIMEOUT = 3600
# The settings get autofetched
IP = '127.0.0.1'
DEPLOYMENT_ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.abspath(os.path.sep.join([DEPLOYMENT_ROOT, '..']))
CPU_CORES = os.sysconf("SC_NPROCESSORS_ONLN")

sys.path.insert(0, os.path.join(SITE_ROOT, "apps"))

# Configuration for gunicorn
# backlog = 2048
bind = '%s:%s' % (IP, PORT)
# daemon = False
# debug = False
# group = None
# keepalive = 2
logfile = os.path.sep.join([DEPLOYMENT_ROOT, 'logs', LOGFILE_NAME])
# loglevel = 'info'
# max_requests = 0
# pidfile = None
# preload_app = False
proc_name = PROC_NAME
# spew = False
timeout = TIMEOUT
# tmp_upload_dir = None
# umask = 0
# user = None
worker_class = 'eventlet'
#worker_connections = 1000
workers = 2 * CPU_CORES + 1