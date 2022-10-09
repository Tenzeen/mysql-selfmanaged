## mysql-selfmanaged

For this assignment I will be using GCP because I ran out of Azure credits.

Setting up the VM:
1. Name the VM
2. Select a machine configuration that has at least 2 vCPUs. (e-2 medium(2vCPU, 4G memory))
3. Change the boot disk OS from Debian to Ubuntu x86
4. Allow http and https traffic
5. Set firewall access to allow HTTP and HTTPS traffic
6. Leave everything else default and then hit create
7. Everything else should remain default and then hit create.
8. After creating the vm, navigate to VPC network settings
    and then firewall
9. To open up the SSH browser just hit SSH under connect.

10. Hit create a new firewall rule.
    - Name the firewall rule
    - set priority to 1000
    - set direction of traffic to ingress
    - target all instances in the network with a source filter of IPv4 ranges
    - set source IPv4 ranges to 0.0.0.0/0
    - select specified tcp protocols and ports
    - select tcp and enter 3306 for its port
    - hit save
11. To open up the SSH browser just hit SSH under connect.

Setting up the OS image:
1. sudo apt-get update
2. sudo apt install mysql-server mysql client
    - type y then enter to continue
3. 
 
