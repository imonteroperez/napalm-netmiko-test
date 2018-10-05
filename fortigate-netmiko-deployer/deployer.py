"""
Script to perform a deployment request by means of a third party custom deployer based on napalm
"""
from __future__ import print_function
from netmiko import ConnectHandler

import os


from optparse import OptionParser

__author__ = "Ildefonso Montero Perez"
__version__ = "0.0.1"


def deploy(conf, user, password, host):
    """Deploy a provided conf inside a Fortigate device using netmiko"""

    if not (os.path.exists(conf) and os.path.isfile(conf)):
        msg = 'Missing or invalid config file {0}'.format(conf)
        raise ValueError(msg)

    fortinet = {
        'device_type' : 'fortinet',
        'ip' : host,
        'username' : user,
        'password' : password
    }

    device = ConnectHandler(**fortinet)

    for command in open(conf):
        print(command)
        device.send_command(command)


if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-f", "--file", dest="conf",
                      help="configuration to deploy")
    parser.add_option("-u", "--user", dest="user",
                      help="user to connect with device")
    parser.add_option("-p", "--password", dest="password",
                      help="password to connect with device")
    parser.add_option("-d", "--device", dest="host",
                      help="device where to deploy proposed configuration")

    (options, args) = parser.parse_args()

    if len(options.__dict__) != 4 or options.__dict__['conf'] is None or options.__dict__['user'] is None  or options.__dict__['password'] is None  or options.__dict__['host'] is None:
        parser.print_help()
        exit(-1)
    else:
        deploy(options.conf, options.user, options.password, options.host)