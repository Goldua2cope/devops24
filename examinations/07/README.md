# Examination 7 - MariaDB installation

To make a dynamic web site, many use an SQL server to store the data for the web site.

[MariaDB](https://mariadb.org/) is an open-source relational SQL database that is good
to use for our purposes.

We can use a similar strategy as with the _nginx_ web server to install this
software onto the correct host(s). Create the playbook `07-mariadb.yml` with this content:

    ---
    - hosts: db
      become: true
      tasks:
        - name: Ensure MariaDB-server is installed.
          ansible.builtin.package:
            name: mariadb-server
            state: present

# QUESTION A

Make similar changes to this playbook that we did for the _nginx_ server, so that
the `mariadb` service starts automatically at boot, and is started when the playbook
is run.

# QUESTION B

When you have run the playbook above successfully, how can you verify that the `mariadb`
service is started and is running?

#### Answer:
> After starting the service I gather information about services with the service_facts module and print out the state of mariadb.service with the debug module

# BONUS QUESTION

How many different ways can use come up with to verify that the `mariadb` service is running?

#### Answer:
  1. Within the ansible playbook I can use the service_facts module with the debug module to print out the gathered service state
  2. In the terminal we can write "ansible db -m command -a "systemctl is-active mariadb"
  3.  We can also check inside the VM with systemctl status mariadb or sudo mysql 

