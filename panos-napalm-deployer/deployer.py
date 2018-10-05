"""
Script to perform a deployment request by means of a third party custom deployer based on napalm
"""
from __future__ import print_function

import os

from napalm_panos.panos import PANOSDriver
from optparse import OptionParser

__author__ = "Ildefonso Montero Perez"
__version__ = "0.0.1"


def deploy(conf, user, password, host, log, output):
    """Deploy a provided conf inside a Palo Alto device"""

    if not (os.path.exists(conf) and os.path.isfile(conf)):
        msg = 'Missing or invalid config file {0}'.format(conf)
        raise ValueError(msg)

    device = PANOSDriver(hostname=host, username=user, password=password)
    device.open()
    device.load_merge_candidate(conf)
    device.commit_config()
    device.close()


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
    parser.add_option("-l", "--log", dest="log",
                      help="log file")
    parser.add_option("-o", "--output", dest="output",
                      help="output file")

    (options, args) = parser.parse_args()

    if len(options.__dict__) != 6 or options.__dict__['conf'] is None or options.__dict__['user'] is None  or options.__dict__['password'] is None  or options.__dict__['host'] is None or options.__dict__['output'] is None or options.__dict__['log'] is None:
        parser.print_help()
        exit(-1)
    else:
        deploy(options.conf, options.user, options.password, options.host, options.log, options.output)