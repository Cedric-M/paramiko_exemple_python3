import paramiko

private_key = paramiko.RSAKey.from_private_key_file("/path-to-your-key/privatekey.pem")
sshclient = paramiko.SSHClient()
sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print ("DEBUG: Connecting")
sshclient.connect( hostname = "<add-url-or-ip-address-here>", username = "<add-username-here>", pkey = private_key )
print ("DEBUG: Connected")
commands = [ "/home/ubuntu/firstscript.sh", "/home/ubuntu/secondscript.sh" ]
for command in commands:
	print ("Executing {}".format( command ))
	stdin , stdout, stderr = sshclient.exec_command(command)
	print (stdout.read().decode('ascii'))
	print("Errors")
	print (stderr.read())
sshclient.close()
