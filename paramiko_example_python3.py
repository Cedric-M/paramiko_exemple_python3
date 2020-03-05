import paramiko

#Variables:
ssh_hostname='<add-url-or-ip-address-here>'
ssh_username='<add-username-here>'

private_key = paramiko.RSAKey.from_private_key_file("/path-to-your-key/privatekey.pem")
sshclient = paramiko.SSHClient()
sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print ("DEBUG: Connecting")
sshclient.connect(hostname = ssh_hostname, username = ssh_username, pkey = private_key)
print ("DEBUG: Connected")
commands = [ "/home/ubuntu/firstscript.sh", "/home/ubuntu/secondscript.sh" ]
for command in commands:
	print (f"Executing {command}")
	stdin , stdout, stderr = sshclient.exec_command(command)
	print (stdout.read().decode('ascii'))
	print("Errors")
	print (stderr.read())
sshclient.close()
