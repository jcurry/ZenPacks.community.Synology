# ZenPacks.community.Synology

This ZenPack provides additional monitoring options for Synology Servers.

## Requirements

### Zenoss

You must first have, or install, Zenoss v4.2.4 or later.

### ZenPacks

You must first install:

- [ZenPacks.community.ConstructionKit v2.0 or later](https://github.com/j053ph4/ZenPacks.community.ConstructionKit)

## Usage

Installing the ZenPack will add the following items to your Zenoss system.

### Device classes

- /Devices/Server/Synology

### Event classes

- /Events/Status/HardDisk
- /Events/Status/RAID
- /Events/Status/System

### Modeler Plugins

- community.snmp.SynologyDeviceMap - Gather Synology hardware model + serial number and OS information.
- community.snmp.SynologySystemMap - Gather Synology System information.
- community.snmp.SynologyHardDiskMap - Gather Synology Hard Disk information.
- community.snmp.SynologyLogicalDiskMap - Gather Synology RAID information.

### Monitoring Templates

- /Devices/Server/Synology/rrdTemplates/SynologyHardDisk
- /Devices/Server/Synology/rrdTemplates/SynologyLogicalDisk
- /Devices/Server/Synology/rrdTemplates/SynologySystem

## Removing ZenPack

- Removing a ZenPack can have unexpected consequences. For example, removing a ZenPack that installs a device class removes the device class and all devices in that class.
- Before removing a ZenPack, you should:
 - Move devices to another Device class
 - Delete any data source of a type provided by the ZenPack
 - Perform a backup of your system data
