#-*- coding: utf-8 -*-

import os

import yaml

from polaris_common import readfile
from polaris_pdns import config
from polaris_pdns.core.polaris import Polaris


__all__ = [ 'main', 'load_configuration' ]


def main():
    """Config must be loaded prior to calling this."""   
    Polaris().run()


def load_configuration():
    """Load configuration from files"""
    ### set config.BASE['INSTALL_PREFIX'] from POLARIS_INSTALL_PREFIX env
    try:
        config.BASE['INSTALL_PREFIX'] = \
                os.environ['POLARIS_INSTALL_PREFIX']
    except KeyError:
        raise Exception('POLARIS_INSTALL_PREFIX env is not set')

    ### optionally load BASE configuration ###
    base_config_file = os.path.join(
        config.BASE['INSTALL_PREFIX'], 'etc', 'polaris-pdns.yaml')
    if os.path.isfile(base_config_file):
        with open(base_config_file) as fp:
            base_config = yaml.load(fp)

        if base_config:
            # validate and set values
            for k in base_config:
                if k not in config.BASE:
                    raise Exception('unknown configuration option "{}"'
                                    .format(k))
                else:
                    config.BASE[k] = base_config[k]

    ### optionally load TOPOLOGY_MAP configuration ###
    topology_config_file = os.path.join(
            config.BASE['INSTALL_PREFIX'], 'etc', 'polaris-topology.yaml')
    if os.path.isfile(topology_config_file):
        topology_config = readfile.read_file(topology_config_file)
        if topology_config:
            config.TOPOLOGY_MAP = topology_config
