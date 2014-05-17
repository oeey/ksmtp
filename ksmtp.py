#!/usr/bin/env python

import smtplib
import email.mime.text
import optparse
import os
import sys
import pwd

os.system('logger mail called')

parser = optparse.OptionParser()
parser.add_option(
    '-s', '--subject',
    help='Subject',
    default="")
parser.add_option(
    '-t', '--to',
    help='To',
    dest="send_to",
    default=None)
parser.add_option(
    '-f', '--from',
    help='From',
    dest="send_from",
    default=None)
parser.add_option(
    '-S', '--server',
    help='server',
    default="prime")
(options, args) = parser.parse_args()

def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]

if options.send_to:
    send_to = options.send_to
else:
    if len(args) == 1:
        send_to = args[0]
    else:
        parser.print_help()
        sys.exit(1)

if options.send_from:
    send_from = options.send_from
else:
    username = get_username()
    hostname = os.uname()[1]
    send_from = username + "@" + hostname

msg_text = sys.stdin.read()
msg = email.mime.text.MIMEText(msg_text)

msg['Subject'] = options.subject
msg['From'] = send_from
msg['To'] = send_to

s = smtplib.SMTP(options.server)
s.sendmail(send_from, [send_to], msg.as_string())
s.quit()