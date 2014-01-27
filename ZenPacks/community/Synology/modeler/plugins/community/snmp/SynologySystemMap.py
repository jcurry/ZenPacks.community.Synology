__doc__ = """SynologySystemMap

Gather Synology System information.
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import MultiArgs
from ZenPacks.community.Synology.Definition import *

class SynologySystemMap(SnmpPlugin):
    """
    Map Synology System table to model.
    """

    compname = 'os'
    constr = Construct(SynologySystemDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid

    snmpGetMap = GetMap({
        '.1.3.6.1.4.1.6574.1.5.4.0': 'upgradeAvailable',
    })

    upgradeAvailableMap = {
        1: 'Available',
        2: 'Unavailable',
        3: 'Connecting',
        4: 'Disconnected',
        5: 'Others',
    }

    def process(self, device, results, log):
        log.info('Modeler %s processing data for device %s', self.name(), device.id)

        getdata, tabledata = results
        maps = []
        rm = self.relMap()
        
        om = self.objectMap(getdata)
        name = 'Synology'
        om.id = self.prepId(name)
        om.title = name
        om.upgradeAvailable = self.upgradeAvailableMap.get(om.upgradeAvailable, 'Unknown')
        rm.append(om)
        
        maps.append(rm)

        return maps