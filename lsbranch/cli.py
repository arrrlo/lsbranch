import os
import click
from subprocess import Popen, PIPE


@click.command()
def cli():
	for dirname, dirnames, _ in os.walk('.'):
	    
	    for subdirname in dirnames:
	        git_dir = os.path.join(dirname, subdirname, '.git')
	        if os.path.exists(git_dir):
	            process = Popen(['git', '--git-dir=' + git_dir, 'branch'], stdout=PIPE, stderr=PIPE)
	            stdout, stderr = process.communicate()
	            print '{} ({})'.format(subdirname, stdout.replace('\n','').split('* ')[-1].split(' ')[0])

	    break