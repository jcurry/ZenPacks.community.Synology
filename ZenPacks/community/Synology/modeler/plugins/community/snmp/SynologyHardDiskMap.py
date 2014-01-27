__doc__ = """SynologyHardDiskMap

Gather Synology Hard Disk information.
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import MultiArgs
from ZenPacks.community.Synology.Definition import *

class SynologyHardDiskMap(SnmpPlugin):
    """
    Map Synology Hard Disk table to model.
    """

    compname = 'os'
    constr = Construct(SynologyHardDiskDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    snmpEntryName = 'synoDisk'
    snmpEntryOID = '.1.3.6.1.4.1.6574.2.1.1'
    snmpTitleName = 'diskID'
    
    snmpGetTableMaps = (
        GetTableMap(snmpEntryName, snmpEntryOID, {
            '.2': snmpTitleName,
            '.3': 'model', # diskModel
            '.4': 'interface', # diskType
        }),
    )

    manufacturerMap = {
        'wd': 'Western Digital',
        'st': 'Seagate',
        'hu': 'Hitachi',
    }

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
            om.model = getattr(om, 'model', '') or 'Unknown'
            om.manufacturer = self.manufacturerMap.get(om.model[:2].lower(), 'Unknown')
            om.setProductKey = MultiArgs(om.model, om.manufacturer)
            rm.append(om)
        
        maps.append(rm)

        return maps
