from fabric.api import env

#Management ip addresses of hosts in the cluster
host1 = 'root@10.87.66.153'
k8s_master = 'root@10.87.117.243'
k8s_slave1 = 'root@10.87.117.245'
k8s_slave2 = 'root@10.87.117.246'


#External routers if any
#for eg.
ext_routers = [('5b6-mx80-3', '10.87.65.253')]


router_asn = 64512       
public_vn_rtgt = 10003    
public_vn_subnet = '10.87.117.248/29'


#Host from which the fab commands are triggered to install and provision
host_build = 'root@10.87.65.144'


#Role definition of the hosts.
env.roledefs = {
    'all': [host1],
    'cfgm': [host1],
    'control': [host1],
    'compute': [host1],
    'openstack': [host1],
    'collector': [host1],
    'webui': [host1],
    'database': [host1],
    'build': [host_build],
}

#Hostnames
# Deprecated 'all' key from release 3.0; Consider specifying the hostname for each host seperately as below
#env.hostnames = {
#    'all': ['a0s1', 'a0s2', 'a0s3','a0s4', 'a0s5', 'a0s6', 'a0s7', 'a0s8', 'a0s9', 'a0s10','backup_node']
#}
env.hostnames = {
    host1: '5b8s38',
}

env.kubernetes = {
'mode' : 'nested',
'master': k8s_master,
'slaves': [k8s_slave1, k8s_slave2]
}

#Openstack admin password
env.openstack_admin_password = 'B24094A6C5D3'

# Passwords of each host
# for passwordless login's no need to set env.passwords,
# instead populate env.key_filename in testbed.py with public key.
env.passwords = {
    host1: 'c0ntrail123',
    k8s_master: 'c0ntrail123',
    k8s_slave1: 'c0ntrail123',
    k8s_slave2: 'c0ntrail123',
    host_build: 'c0ntrail123',
}

# SSH Public key file path for passwordless logins
# if env.passwords is not specified.
#env.key_filename = '/root/.ssh/id_rsa.pub'

#For reimage purpose
env.ostypes = {
    host1: 'ubuntu',
    k8s_master: 'ubuntu',
    k8s_slave1: 'ubuntu',
    k8s_slave2: 'ubuntu',
}

env.orchestrator='openstack'

