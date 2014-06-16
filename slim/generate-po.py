from subprocess import call

cmd = [
    'django-admin.py',
    'makemessages',
    '-l',
    'se',
    '-i',
    'pyenv/*']
call(cmd)

cmd += [
    '-d',
    'djangojs']

call(cmd)

call(['django-admin.py', 'compilemessages'])
