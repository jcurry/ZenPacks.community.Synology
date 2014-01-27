from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *

BASE = "Synology"
VERSION = Version(1, 0, 0)

def getMapValue(ob, datapoint, map):
    '''Attempt to map number to data dict'''
    try:
        value = int(ob.getRRDValue(datapoint))
        return map[value]
    except:
        return 'Unknown'
    
def getValue(ob, datapoint):
    '''Attempt to get RRD value'''
    try:
        return int(ob.getRRDValue(datapoint))
    except:
        return 'Unknown'
    
def getSystemStatus(ob): return ob.getMapValue('systemStatus_systemStatus', ob.systemStatusMap)
def getPowerStatus(ob): return ob.getMapValue('powerStatus_powerStatus', ob.systemStatusMap)
def getSystemFanStatus(ob): return ob.getMapValue('systemFanStatus_systemFanStatus', ob.systemStatusMap)
def getCpuFanStatus(ob): return ob.getMapValue('cpuFanStatus_cpuFanStatus', ob.systemStatusMap)
def getSystemTemperature(ob): return ob.getValue('systemTemperature_systemTemperature')

systemStatusMap = {
    1: 'Normal',
    2: 'Failed',
}

DATA = {
    'version': VERSION,
    'zenpackbase': BASE,
    'component': 'SynologySystem',
    'componentData': {
        'singular': 'System',
        'plural': 'System',
        'properties': {
            'upgradeAvailable': addProperty('Upgrade', optional=False),
            'getSystemStatus': getReferredMethod('System Status', 'getSystemStatus'),
            'getPowerStatus': getReferredMethod('Power Status', 'getPowerStatus'),
            'getSystemFanStatus': getReferredMethod('System Fan Status', 'getSystemFanStatus'),
            'getCpuFanStatus': getReferredMethod('CPU Fan Status', 'getCpuFanStatus'),
            'getSystemTemperature': getReferredMethod('Temperature', 'getSystemTemperature'),
            'description': addProperty('Description (offline)'),
            'date': addProperty('Date of Purchase (offline)'),
            'firmware': addProperty('Firmware (offline)'),
            'eventClass': getEventClass('/Status/System'),
        },
    },
    'componentAttributes': {'systemStatusMap': systemStatusMap },
    'componentMethods': [
        getValue, getMapValue, getSystemStatus, getPowerStatus,
        getSystemFanStatus, getCpuFanStatus, getSystemTemperature
    ],
}

SynologySystemDefinition = type('SynologySystemDefinition', (BasicDefinition,), DATA)


def getDiskStatus(ob): return ob.getMapValue('diskStatus_diskStatus', ob.diskStatusMap)
def getDiskTemperature(ob): return ob.getValue('diskTemperature_diskTemperature')

diskStatusMap = {
    1: 'Normal', # The disk is functioning normally
    2: 'Initialized - No Data', # The disk has system partitions but no data
    3: 'Not Initialized - Partitioned', # The disk is not partitioned
    4: 'Partition Failed', # Partitions on the disk are damaged
    5: 'Crashed', # The disk is damaged
}

DATA = {
    'version': VERSION,
    'zenpackbase': BASE,
    'component': 'SynologyHardDisk',
    'componentData': {
        'singular': 'Hard Disk',
        'plural': 'Hard Disks',
        'properties': {
            'interface': addProperty('Interface'),
            'manufacturer': addProperty('Manufacturer', optional=False, order=1),
            'model': addProperty('Model', optional=False, order=1),
            'getDiskStatus': getReferredMethod('Disk Status', 'getDiskStatus'),
            'getDiskTemperature': getReferredMethod('Temperature', 'getDiskTemperature'),
            'alias': addProperty('Alias (offline)'),
            'cache': addProperty('Cache (offline)'),
            'capacity': addProperty('Capacity (offline)'),
            'formFactor': addProperty('Form Factor (offline)', default='3.5"'),
            'serialNumber': addProperty('Serial # (offline)'),
            'rpm': addProperty('RPM (offline)'),
            'storageType': addProperty('Storage Type (offline)', default='HDD'),
            'description': addProperty('Description (offline)'),
            'date': addProperty('Date of Purchase (offline)'),
            'bay': addProperty('Bay (offline)'),
            'firmware': addProperty('Firmware (offline)'),
            'eventClass': getEventClass('/Status/HardDisk'),
        },
    },
    'componentAttributes': {'diskStatusMap': diskStatusMap },
    'componentMethods': [getValue, getMapValue, getDiskStatus, getDiskTemperature],
}

SynologyHardDiskDefinition = type('SynologyHardDiskDefinition', (BasicDefinition,), DATA)


def getRaidStatus(ob): return ob.getMapValue('raidStatus_raidStatus', ob.raidStatusMap)

raidStatusMap = {
    1: 'Normal', # RAID is functioning normally
    2: 'Repairing', # These statuses are shown when RAID is created or deleted
    3: 'Migrating',
    4: 'Expanding',
    5: 'Deleting',
    6: 'Creating',
    7: 'Raid Syncing',
    8: 'Raid Parity Checking',
    9: 'Raid Assembling',
    10: 'Canceling',
    11: 'Degrade - tolerable failure', # Degrade is shown when a tolerable failure of disk(s) occurs
    12: 'Crashed - read-only', # RAID has crashed and is now read-only
}

DATA = {
    'version': VERSION,
    'zenpackbase': BASE,
    'component': 'SynologyLogicalDisk',
    'componentData': {
        'singular': 'Logical Disk',
        'plural': 'Logical Disks',
        'properties': {
            'getRaidStatus': getReferredMethod('RAID Status', 'getRaidStatus'),
            'alias': addProperty('Alias (offline)'),
            'capacity': addProperty('Capacity (offline)'),
            'description': addProperty('Description (offline)'),
            'eventClass': getEventClass('/Status/RAID'),
        },
    },
    'componentAttributes': {'raidStatusMap': raidStatusMap },
    'componentMethods': [getMapValue, getRaidStatus],
}

SynologyLogicalDiskDefinition = type('SynologyLogicalDiskDefinition', (BasicDefinition,), DATA)