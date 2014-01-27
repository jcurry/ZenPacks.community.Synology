
(function(){
    var ZC = Ext.ns('Zenoss.component');

    function render_link(ob) {
        if (ob && ob.uid) {
            return Zenoss.render.link(ob.uid);
        } else {
            return ob;
        }
    }

    ZC.SynologySystemPanel = Ext.extend(ZC.ComponentGridPanel, {
        constructor: function(config) {
            config = Ext.applyIf(config||{}, {
                componentType: 'SynologySystem',
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
                        "name": "getCpuFanStatus"
                    }, 
                    {
                        "name": "getPowerStatus"
                    }, 
                    {
                        "name": "getSystemFanStatus"
                    }, 
                    {
                        "name": "getSystemStatus"
                    }, 
                    {
                        "name": "getSystemTemperature"
                    }, 
                    {
                        "name": "upgradeAvailable"
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
                        "header": "CPU Fan Status", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getCpuFanStatus", 
                        "dataIndex": "getCpuFanStatus"
                    }, 
                    {
                        "header": "Power Status", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getPowerStatus", 
                        "dataIndex": "getPowerStatus"
                    }, 
                    {
                        "header": "System Fan Status", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getSystemFanStatus", 
                        "dataIndex": "getSystemFanStatus"
                    }, 
                    {
                        "header": "System Status", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getSystemStatus", 
                        "dataIndex": "getSystemStatus"
                    }, 
                    {
                        "header": "Temperature", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "getSystemTemperature", 
                        "dataIndex": "getSystemTemperature"
                    }, 
                    {
                        "header": "Upgrade", 
                        "width": 120, 
                        "sortable": "true", 
                        "id": "upgradeAvailable", 
                        "dataIndex": "upgradeAvailable"
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
            ZC.SynologySystemPanel.superclass.constructor.call(this, config);
        }
    });
    
    Ext.reg('SynologySystemPanel', ZC.SynologySystemPanel);
    ZC.registerName('SynologySystem', _t('System'), _t('System'));
    
    })();

