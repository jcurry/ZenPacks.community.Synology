
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
                        "sortable": "true", 
                        "width": 120, 
                        "header": "CPU Fan Status", 
                        "renderer": "pass_link", 
                        "id": "getCpuFanStatus", 
                        "dataIndex": "getCpuFanStatus"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Power Status", 
                        "renderer": "pass_link", 
                        "id": "getPowerStatus", 
                        "dataIndex": "getPowerStatus"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "System Fan Status", 
                        "renderer": "pass_link", 
                        "id": "getSystemFanStatus", 
                        "dataIndex": "getSystemFanStatus"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "System Status", 
                        "renderer": "pass_link", 
                        "id": "getSystemStatus", 
                        "dataIndex": "getSystemStatus"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Temperature", 
                        "renderer": "pass_link", 
                        "id": "getSystemTemperature", 
                        "dataIndex": "getSystemTemperature"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Upgrade", 
                        "renderer": "pass_link", 
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

