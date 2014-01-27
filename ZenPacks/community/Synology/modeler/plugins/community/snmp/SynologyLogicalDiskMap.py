__doc__ = """SynologyLogicalDiskMap

Gather Synology RAID information.
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import MultiArgs
from ZenPacks.community.Synology.Definition import *

class SynologyLogicalDiskMap(SnmpPlugin):
    """
    Map Synology RAID table to model.
    """

    compname = 'os'
    constr = Construct(SynologyLogicalDiskDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    snmpEntryName = 'synoRaid'
    snmpEntryOID = '.1.3.6.1.4.1.6574.3.1.1'
    snmpTitleName = 'raidName'
    
    snmpGetTableMaps = (
        GetTableMap(snmpEntryName, snmpEntryOID, {
            '.2': snmpTitleName,
        }),
    )

    def process(self, device, results, log):
        log.info('Modeler %s processing data for device %s', self.name(), device.id)

        getdata, tabledata = results
        maps = []
        rm = self.relMap()

        for snmpindex, row in tabledata.get(self.snmpEntryName, {}).items():
            om = self.objectMap(row)
            name = "%s" % getattr(om, self.snmpTitleName)
            om.id = self.prepId(name)
            om.title = name
            om.snmpindex = snmpindex
            rm.append(om)
        
        maps.append(rm)

        return maps
