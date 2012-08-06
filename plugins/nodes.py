import salt.cli.key
import salt.client
import salt.config

def _populate():
    active_nodes = []
    inactive_nodes = []

    '''
    Print a list of up and down minions
    '''

    response = {}

    __opts__ = salt.config.master_config('/etc/salt/master')

    client = salt.client.LocalClient(__opts__['conf_file'])
    key = salt.cli.key.Key(__opts__)
    minions = client.cmd('*', 'test.ping', timeout=__opts__['timeout'])
    keys = key._keys('acc')

    response['inactive_nodes'] = sorted(keys - set(minions))

    active_nodes = client.cmd('*', 'test.ping', timeout=__opts__['timeout'])
    response['active_nodes'] = sorted(active_nodes)

    return response

