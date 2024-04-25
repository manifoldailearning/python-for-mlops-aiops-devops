from fabric import task

@task
def hello(c):
    c.run("hostname")  # Run a command on the remote server
