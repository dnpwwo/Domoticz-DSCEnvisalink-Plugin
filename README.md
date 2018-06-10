# Domoticz-DSCEnvisalink-Plugin
Full version of DSC Envisalink Plugin for Domoticz home automation

Controls a single DSC Alarm (PC1616) Envisalink on your network. 

## Key Features

* Creates a Contact device per zone that show Open/Closed status.  These can be changed to 'Motion' devices in the Device Edit page and they will show On/Off (recommend setting an Off Delay otherwise activity is rarely seen in the Web UI)
* Creates an Alert per partition that shows partition state, useful if you don't want to use the Security Panel integration or you have more than one partition.
* Creates a Contact device for each Command Output/Partition combination seen. The DSC only reports activation so an Off Delay must exist for the device to reset).
* Optionally creates a Security Panel device that allows arming and disarming via Domoticz.
* When network connectivity is lost the Domoticz UI will optionally show the device(s) with Red banner

## Installation

Python version 3.4 or higher required & Domoticz version 3.87xx or greater.

To install:
* Go in your Domoticz directory using a command line and open the plugins directory.
* Run: ```git clone https://github.com/dnpwwo/Domoticz-DSCEnvisalink-Plugin.git```
* Restart Domoticz.

In the web UI, navigate to the Hardware page.  In the hardware dropdown there will be an entry called "DSC Alarm via EnvisaLink 4".

Devices are created in the 'Devices' tab, to use them you need to click the green arrow icon and 'Add' them to Domoticz.

To use the integrated Security Panel this must be configured through the 'Settings' page in Domoticz. In the 'Security Panel' widget:
* Enter a numeric password, I used the same code as my DSC Alarm
* Set the 'Delay' to match the exit delay in the DSC 
This will create a 'Domoticz Internal' Security Panel device in the 'Devices' page, just ignore it.

To use the Security Panel functionality, either select 'Security Panel' from the menu system or click the padlock icon on the Security Panel device (which will be in the 'Switches' tab)

For security reasons the DSC Alarm can only be Armed or Disarmed via the Security Panel.

## Updating

To update:
* Go in your Domoticz directory using a command line and open the plugins directory then the Domoticz-DSCEnvisalink-Plugin directory.
* Run: ```git pull```
* Restart Domoticz.

## Configuration

### DSC

DSC must have an Envisalink 3 or 4 attached as an additional keypad.

### Domoticz

| Field | Information|
| ----- | ---------- |
| IP Address | Will handle DNS names and IP V4 addresses (e.g 192.168.xxx.xxx) |
| Port | The port that the Envisalink is listening on. Default 4025. |
| Password | Envisalink password, as used on the device's website on your LAN |
| Max Partitions | The number of partitions you have set up |
| Max Zones | The number of Zones you have defined |
| Integrated Security Panel | If true the a Domoticz security panel device is created for partition 1. |
| Alarm Passcode | A numeric PIN that can disarm the DSC Alarm panel |
| Time Out Lost Devices | When true, the devices in Domoitcz will have a red banner when network connectivity is lost to the Envisalink |
| Debug | Debug logging options |

## Change log

| Version | Information|
| ----- | ---------- |
| 1.0.0 | Initial upload version |
| 1.1.0 | Added Command Output support |
| 2.1.7 | Added integration with Security Panel |
| 2.1.8 | Bugfix: time synchronisation error message |
