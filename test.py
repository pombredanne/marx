from marx.utils import run_long_command


for entry in run_long_command('ping -c 3 google.com'):
    print entry
