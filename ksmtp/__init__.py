"""
KSMTP - Simple Python SMTP relay replacement for sendmail with SSL authentication


Simple Python SMTP relay replacement for sendmail with SSL authentication

Useful for relaying all email through an account like Gmail, without the
messy configurations of Postfix / Sendmail.

Similar to the 'ssmtp' project, but written in Python

Usage:
  1) pip install ksmtp
  2) edit /etc/ksmtp.conf with your login credentials
  3) (optional) create symlink to ksmtp to replace sendmail
     ln -s `which ksmtp` /usr/sbin/sendmail
  4) send test mail
     ksmtp test@test.com -s "some subject"

"""

