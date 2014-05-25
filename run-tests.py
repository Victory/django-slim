import django
import sys


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

exit(errs)
