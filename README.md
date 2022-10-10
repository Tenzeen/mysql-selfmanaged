### mysql-selfmanaged

##For this assignment I will be using GCP because I ran out of Azure credits.

## Setting up the VM:
1. Name the VM
2. Select a machine configuration that has at least 2 vCPUs. (e-2 medium(2vCPU, 4G memory))
3. Change the boot disk OS from Debian to Ubuntu x86
4. Allow http and https traffic
5. Set firewall access to allow HTTP and HTTPS traffic
6. Leave everything else default and then hit create
7. Everything else should remain default and then hit create.
8. To open up the SSH browser just hit SSH under connect.

## Setting up configuration settings
1. After creating the vm, navigate to VPC network settings in GCP
    and then hit firewall
    - Name the firewall rule
    - set priority to 1000
    - set direction of traffic to ingress
    - target all instances in the network with a source filter of IPv4 ranges
    - set source IPv4 ranges to 0.0.0.0/0
    - select specified tcp protocols and ports
    - select tcp and enter 3306 for its port
    - hit save
2. Open the SSH browser
    - type: 'sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf' and then hit enter
    - go down to bind-address, delete the existing IP address, and then type 0.0.0.0 
        ***take on the ip of the virtual machine***
    - type: sudo /etc/init.d/mysql restart
        ***restart mysql to make sure changes are in effect***

## Setting up the OS image:
1. ```sudo apt-get update```
2. sudo apt install mysql-server mysql client
    - type y then enter to continue
3. sudo mysql #to enter the mysql server
4. create user 'username'@'%' identified by 'password';   
        ***to create a user on mysql***
6. grant all privileges on. to 'dba'@'%' with grant option; 
        ***to give the user privileges***
8. mysql -u user -p; 
        ***log into user on mysql***
10. create database db1; 
        ***to create an empty database within mysql server***
12. use db1; 

        ***to select the database***
14. create table table1;
 
        ***to create a table in the selected database***

 
