# Examination 1 - Understanding SSH and public key authentication

Connect to one of the virtual lab machines through SSH, i.e.

    $ ssh -i deploy_key -l deploy webserver

Study the `.ssh` folder in the home directory of the `deploy` user:

    $ ls -ld ~/.ssh

Look at the contents of the `~/.ssh` directory:

    $ ls -la ~/.ssh/

## QUESTION A

What are the permissions of the `~/.ssh` directory?
    - User owner has read,write and execute permissions. Groups and others have no rights.

Why are the permissions set in such a way?
    - In this directory the user makes custom configurations for its ssh connections. That should not be accessible for other users.

## QUESTION B

What does the file `~/.ssh/authorized_keys` contain?
    - It contains the public keys that are authorized to log into the server as that specific user

## QUESTION C

When logged into one of the VMs, how can you connect to the
other VM without a password? 
    - On the klient side (ie. webserver) we need to create a ssh key-pair and copy the public key to the servers authorized_keys file (user deploy in this case) via the host (use ie. a text editor)
        '''
        ssh-keygen -t ed25519
        cat ~/.ssh/dbserver_key
        '''
    - An ssh-agent will handle the private key and passphrase when establishing a connection
        '''
        ssh-agent
        echo 'eval "$(ssh-agent -s)"' >> ~/.bashrc
        '''

### Hints:

* man ssh-keygen(1)
* ssh-copy-id(1) or use a text editor

## BONUS QUESTION

Can you run a command on a remote host via SSH? How?
    - Yes
    '''
    ssh deploy@192.168.121.179 cat ~/.ssh/authorized_keys
    '''


### Useful commands:
sudo virt net-dhcp-leases vagrant-libvirt
