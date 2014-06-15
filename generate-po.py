from subprocess import call

cmd = [
    'django-admin.py',
    'makemessages',
    '-l',
    'en-us',
    '-i',
    'pyenv/*']
call(cmd)

cmd += [
    '-d',
    'djangojs']

call(cmd)
