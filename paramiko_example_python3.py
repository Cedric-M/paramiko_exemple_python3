import paramiko
k = paramiko.RSAKey.from_private_key_file("/path-to-your-key/privatekey.pem")
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print ("DEBUG: Connecting")
c.connect( hostname = "<add-url-or-ip-address-here>", username = "<add-username-here>", pkey = k )
print ("DEBUG: Connected")
commands = [ "/home/ubuntu/firstscript.sh", "/home/ubuntu/secondscript.sh" ]
for command in commands:
	print ("Executing {}".format( command ))
	stdin , stdout, stderr = c.exec_command(command)
	print (stdout.read().decode('ascii'))
	print("Errors")
	print (stderr.read())
c.close()
