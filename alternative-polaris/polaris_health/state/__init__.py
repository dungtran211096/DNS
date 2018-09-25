# -*- coding: utf-8 -*-

import logging
import time

from polaris_health import Error
from .pool import Pool, PoolMember
from .globalname import GlobalName

__all__ = [ 'State' ]

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.NullHandler())

class State:

    """Health state table 
    
    attributes:
        .pools
        .globalnames
    """    

    def __init__(self, config_obj):
        print('1234555')
        self._from_config_dict(config_obj)

    def to_dist_dict(self):
        """Return a dict representation of self required by Polaris PDNS
        to perform query distribution.

        """
        obj = {}

        # add a timestamp
        obj['timestamp'] = time.time()

        # add pools
        obj['pools'] = {}
        for pool_name in self.pools:
            obj['pools'][pool_name] = self.pools[pool_name].to_dist_dict()

        # add globalnames
        obj['globalnames'] = {}
        for globalname_name in self.globalnames:
            obj['globalnames'][globalname_name] = \
                self.globalnames[globalname_name].to_dist_dict()

        return obj

    def _from_config_dict(self, obj):    
        """Initialize State from a config dict

        args:
            obj: dict, config dict(lb_config)

        """
        print('aaaaaaaaaaaaaa')
        # build pools 
        self.pools = {}
        if 'pools' not in obj or not obj['pools']:
            log_msg = 'configuration must have pools'
            print('1111')
            LOG.error(log_msg)
            raise Error(log_msg)

        for pool_name in obj['pools']:
            print('2222')
            # check if pool with the same name has been defined earlier
            if pool_name in self.pools:
                log_str = 'pool "{}" already exists'.format(pool_name)
                LOG.error(log_str)
                raise Error(log_str)

            self.pools[pool_name] = \
                Pool.from_config_dict(pool_name=pool_name,
                                      obj=obj['pools'][pool_name])

        # build globalnames
        self.globalnames = {}
        if 'globalnames' not in obj or not obj['globalnames']:
            print('33333')
            log_msg = 'configuration must have globalnames'
            LOG.error(log_msg)
            raise Error(log_msg)

        for globalname_name in obj['globalnames']:
                print('4444')
                # check if globalname with the same name 
                # has been defined earlier
                if globalname_name in self.globalnames:
                    log_str = ('globalname "{}" already exists'
                               .format(globalname_name))
                    LOG.Error(log_msg)
                    raise Error(log_msg)    

                # check if the referenced pool exists
                if 'pool' not in obj['globalnames'][globalname_name]:
                    log_msg = ('"{}" is missing a mandatory parameter "pool"'
                               .format(globalname_name))
                    LOG.error(log_msg)
                    raise Error(log_msg)
                else:      
                    pool_name = obj['globalnames'][globalname_name]['pool']

                if pool_name not in self.pools:
                    log_msg = ('globalname "{}" references unknown pool "{}"'.
                               format(globalname_name, pool_name))
                    LOG.error(log_msg)
                    raise Error(log_msg)

                self.globalnames[globalname_name] = \
                    GlobalName.from_config_dict(
                        name=globalname_name,
                        obj=obj['globalnames'][globalname_name])   

