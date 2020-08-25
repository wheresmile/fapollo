# -*- coding: utf-8 -*-
from fabric import task


@task
def deploy(c):
    c.local('uname -a')
    with c.cd("/home/ubuntu/code/fapollo"):
        c.run('git fetch')
        c.run('git merge origin/master')
    c.sudo('supervisorctl reload fapollo')



