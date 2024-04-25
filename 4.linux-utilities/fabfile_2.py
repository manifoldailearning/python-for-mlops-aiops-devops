from fabric import Connection
try:
    print("Connecting to server")
    conn = Connection(
        host="ec2-54-242-159-63.compute-1.amazonaws.com",
        user="ec2-user",
        connect_kwargs={
            "key_filename": "fabric-demo-key.pem",
        }
    )
    print("Successfully connected")
    conn.run("mkdir demo")
    conn.put('fabfile.py')
    print("Deployment was successful")
except Exception as e:
    print("Deployment was unsuccessful.\nError:\n")
    print(e)