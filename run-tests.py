import django
import sys

from subprocess import call
from pyvirtualdisplay import Display


print "Starting Virtual Display"
display = Display(visible=0, size=(1440, 900))
display.start()


def pretty_assertish(msg, cond):
    sys.stdout.write('%s...' % msg)
    if cond:
        print "Passed"
        return 0
    else:
        print "Failed"
        return 1

errs = 0
errs += pretty_assertish(
    "Checking Version Number",
    django.get_version() == '1.7b4')

omits = ['slim/slim/wsgi.py']
omit = ','.join(omits)
source = 'slim'
call(['coverage', 'run',
      '--omit', omit,
      '--source', 'slim',
      'slim/manage.py', 'test', 'home', 'infoorg', 'tagslim'])
errs += call(['coverage', 'report'])

err = call(['sh', 'pep8.sh'])
if err != 0:
    errs += 1

display.stop()

exit(errs)
