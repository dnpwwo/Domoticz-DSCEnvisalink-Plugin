# Domoticz-DSCEnvisalink-Plugin
Full version of DSC Envisalink Plugin for Domoticz home automation

Controls a single DSC Alarm (PC1616) Envisalink on your network. 

## Key Features

* Creates a Contact device per zone that show Open/Closed status.  These can be changed to 'Motion' devices in the Device Edit page and they will show On/Off (recommend setting an Off Delay otherwise activity is rarely seen in the Web UI)
* Creates an Alert per partition that shows partition state
* When network connectivity is lost the Domoticz UI will optionally show the device(s) with Red banner

## Installation

Python version 3.4 or higher required & Domoticz version 3.87xx or greater.

To install:
* Go in your Domoticz directory using a command line and open the plugins directory.
* Run: ```git clone https://github.com/dnpwwo/Domoticz-DSCEnvisalink-Plugin.git```
* Restart Domoticz.

In the web UI, navigate to the Hardware page.  In the hardware dropdown there will be an entry called "DSC Alarm via EnvisaLink 4".

## Updating

To update:
* Go in your Domoticz directory using a command line and open the plugins directory then the Domoticz-DSCEnvisalink-Plugin directory.
* Run: ```git pull```
* Restart Domoticz.

## Configuration

### DSC

DSC must have an Envisalink 4 attached as an additional keypad.

### Domoticz

| Field | Information|
| ----- | ---------- |
| IP Address | Will handle DNS names and IP V4 addresses (e.g 192.168.xxx.xxx) |
| Port | The port that the Envisalink is listening on. Default 4025. |
| Password | Envisalink password, as used on the device's website on your LAN |
| Max Partitions | The number of partitions you have set up |
| Max Zones | The number of Zones you have defined |
| Time Out Lost Devices | When true, the devices in Domoitcz will have a red banner when network connectivity is lost to the Envisalink |
| Debug | Debug logging options |

## Change log

| Version | Information|
| ----- | ---------- |
| 1.0.0 | Initial upload version |
