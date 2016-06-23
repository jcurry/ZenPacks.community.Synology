
(function(){
    var ZC = Ext.ns('Zenoss.component');

    function render_link(ob) {
        if (ob && ob.uid) {
            return Zenoss.render.link(ob.uid);
        } else {
            return ob;
        }
    }
    
    function pass_link(ob){ 
        return ob; 
    }
    
    ZC.SynologyHardDiskPanel = Ext.extend(ZC.ComponentGridPanel, {
        constructor: function(config) {
            config = Ext.applyIf(config||{}, {
                componentType: 'SynologyHardDisk',
                autoExpandColumn: 'name', 
                fields:                 [
                    {
                        "name": "uid"
                    }, 
                    {
                        "name": "severity"
                    }, 
                    {
                        "name": "status"
                    }, 
                    {
                        "name": "name"
                    }, 
                    {
                        "name": "getDiskStatus"
                    }, 
                    {
                        "name": "getDiskTemperature"
                    }, 
                    {
                        "name": "manufacturer"
                    }, 
                    {
                        "name": "model"
                    }, 
                    {
                        "name": "usesMonitorAttribute"
                    }, 
                    {
                        "name": "monitor"
                    }, 
                    {
                        "name": "monitored"
                    }, 
                    {
                        "name": "locking"
                    }
                ]
,
                columns:                [
                    {
                        "sortable": "true", 
                        "width": 50, 
                        "header": "Events", 
                        "renderer": Zenoss.render.severity, 
                        "id": "severity", 
                        "dataIndex": "severity"
                    }, 
                    {
                        "header": "Name", 
                        "width": 70, 
                        "sortable": "true", 
                        "id": "name", 
                        "dataIndex": "name"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Disk Status", 
                        "renderer": "pass_link", 
                        "id": "getDiskStatus", 
                        "dataIndex": "getDiskStatus"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Temperature", 
                        "renderer": "pass_link", 
                        "id": "getDiskTemperature", 
                        "dataIndex": "getDiskTemperature"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Manufacturer", 
                        "renderer": "pass_link", 
                        "id": "manufacturer", 
                        "dataIndex": "manufacturer"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Model", 
                        "renderer": "pass_link", 
                        "id": "model", 
                        "dataIndex": "model"
                    }, 
                    {
                        "header": "Monitored", 
                        "width": 65, 
                        "sortable": "true", 
                        "id": "monitored", 
                        "dataIndex": "monitored"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 65, 
                        "header": "Locking", 
                        "renderer": Zenoss.render.locking_icons, 
                        "id": "locking", 
                        "dataIndex": "locking"
                    }
                ]

            });
            ZC.SynologyHardDiskPanel.superclass.constructor.call(this, config);
        }
    });
    
    Ext.reg('SynologyHardDiskPanel', ZC.SynologyHardDiskPanel);
    ZC.registerName('SynologyHardDisk', _t('Hard Disk'), _t('Hard Disks'));
    
    })();

