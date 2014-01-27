__doc__ = """SynologyDeviceMap

Gather Synology hardware model + serial number and OS information.
"""

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap
from Products.DataCollector.plugins.DataMaps import MultiArgs, ObjectMap

class SynologyDeviceMap(SnmpPlugin):
    snmpGetMap = GetMap({
        '.1.3.6.1.4.1.6574.1.5.1.0': 'modelName',
        '.1.3.6.1.4.1.6574.1.5.2.0': 'serialNumber',
        '.1.3.6.1.4.1.6574.1.5.3.0': 'version',
    })

    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s", self.name(), device.id)

        manufacturer = 'Synology'
        getdata, tabledata = results
        model = getdata.get('modelName', 'Unknown')
        serial_number = getdata.get('serialNumber', 'Unknown')
        version = getdata.get('version', 'Unknown')

        hw_om = ObjectMap(compname='hw', data={
            'setProductKey': MultiArgs(model, manufacturer),
            'serialNumber': serial_number,
        })

        os_om = ObjectMap(compname='os', data={
            'setProductKey': MultiArgs(version, manufacturer),
        })

        return [hw_om, os_om]