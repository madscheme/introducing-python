from fabric.api import local

def iso():
    local('date -u')
