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
    django.get_version() == '1.7b4');


print "Running `home` module tests"
errs = call(['python', 'slim/manage.py', 'test', 'home'])

exit(errs)
