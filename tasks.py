import os
from subprocess import call
from invoke import task

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.join(CURR_DIR, 'signal_interpreter_server')
UNIT_TEST_DIR = os.path.join(CURR_DIR, 'tests')
COV_PATH = os.path.join(CURR_DIR, '.coveragerc')

@task
def style(_):
    call(f'pycodestyle {SRC_DIR}', shell=True)


@task
def lint(_):
    call(f'pylint {SRC_DIR}', shell=True)


@task
def unittest(_):
    cmd = f'pytest {UNIT_TEST_DIR} --cov {SRC_DIR} -config{COV_PATH}'
    call(cmd, shell=True)
