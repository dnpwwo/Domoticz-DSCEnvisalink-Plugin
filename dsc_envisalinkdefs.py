#The MIT License (MIT)
#Copyright (c) 2016 Dan Cinnamon
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#These definitions based on the definition file from: https://github.com/Cinntax/pyenvisalink Credit where it is due !

evl_Commands = {
    'KeepAlive' : '000',
    'StatusReport' : '001',
    'Login' : '005',
    'DumpZoneTimers' : '008',
    'TimeSync' : '010',
    'ArmAway' : '030',
    'ArmStay' : '031',
    'ArmMax' : '032',
    'Disarm' : '040',
    'TimeBroadcast': '0561',
    'Panic' : '060',
    'PartitionKeypress' : '071',
    'SendCode' : '200',
    'CommandOutput' : '020'
}

evl_PanicTypes = {
    'Fire' : '1',
    'Ambulance' : '2',
    'Police' : '3'
}

evl_LedMask = {
    'Ready' :       0x01,
    'Armed' :       0x02,
    'Memory' :      0x04,
    'Bypass' :      0x08,
    'Trouble' :     0x10,
    'Program' :     0x20,
    'Fire' :        0x40,
    'Backlight' :   0x80
}

evl_TroubleMask = {
    'Service is Required' :     0x01,
    'AC Power Lost' :           0x02,
    'Telephone Line Fault' :    0x04,
    'Failure to Communicate' :  0x08,
    'Sensor/Zone Fault' :       0x10,
    'Sensor/Zone Tamper' :      0x20,
    'Sensor/Zone Low Battery' : 0x40,
    'Loss of Time' :            0x80
}

evl_ArmModes = {
        '0' : {'name' : 'Arm Away', 'status':{'armed_away': True, 'armed_zero_entry_delay': False, 'alpha':'Arm Away', 'exit_delay':False, 'entry_delay': False }},
        '1' : {'name' : 'Arm Stay', 'status':{'armed_stay': True, 'armed_zero_entry_delay': False, 'alpha':'Arm Stay', 'exit_delay':False, 'entry_delay': False }},
        '2' : {'name' : 'Arm Zero Entry Away', 'status':{'armed_away': True, 'armed_zero_entry_delay': True, 'alpha':'Arm Zero Entry Away', 'exit_delay':False, 'entry_delay': False }},
        '3' : {'name' : 'Arm Zero Entry Stay', 'status':{'armed_stay': True, 'armed_zero_entry_delay': True, 'alpha':'Arm Zero Entry Stay', 'exit_delay':False, 'entry_delay': False }}
    }

evl_ResponseTypes = {
    '500' : {'name':'Poll', 'handler':'poll_response'},
    '501' : {'name':'Invalid Checksum', 'handler':'command_response_error'},
    '502' : {'name':'An error has been detected', 'handler':'system_response_error'},
    '505' : {'name':'Login Prompt', 'handler':'login'},
    '550' : {'name':'Time Response', 'handler':'time_response'},
    '615' : {'name':'Envisalink Zone Timer Dump', 'handler':'zone_timer_dump'},
    '616' : {'name':'Zone Restored', 'handler':'zone_bypass_update'},
    '900' : {'name':'EnterCode', 'handler':'send_code'},

#ZONE UPDATES
    '601' : {'name':'Zone Alarm', 'handler':'zone_state_change', 'status':{'alarm' : True}},
    '602' : {'name':'Zone Alarm Restore', 'handler':'zone_state_change', 'status':{'alarm' : False}},
    '603' : {'name':'Zone Tamper', 'handler':'zone_state_change', 'status':{'tamper' : True}},
    '604' : {'name':'Zone Tamper Restore', 'handler':'zone_state_change', 'status':{'tamper' : False}},
    '605' : {'name':'Zone Fault', 'handler':'zone_state_change', 'status':{'fault' : True}},
    '606' : {'name':'Zone Fault Restore', 'handler':'zone_state_change', 'status':{'fault' : False}},
    '609' : {'name':'Zone Open', 'handler':'zone_state_change', 'status':{'open' : True}},
    '610' : {'name':'Zone Restored', 'handler':'zone_state_change', 'status':{'open' : False}},

#PARTITION UPDATES
    '510' : {'name':'Keypad LED State', 'handler':'keypad_led_change'},
    '511' : {'name':'Keypad LED Flash State', 'handler':'keypad_led_change'},
    '650' : {'name':'Ready', 'handler':'partition_state_change', 'status':{'ready' : True, 'alpha' : 'Ready'}},
    '651' : {'name':'Not Ready', 'handler':'partition_state_change', 'status':{'ready' : False, 'alpha' : 'Not Ready'}},
    '652' : {'name':'Armed', 'handler':'partition_state_change'},
    '653' : {'name':'Ready - Force Arming Enabled', 'handler':'partition_state_change', 'status':{'ready': True, 'alpha' : 'Ready - Force Arm'}},
    '654' : {'name':'Alarm', 'handler':'partition_state_change', 'status':{'alarm' : True, 'alpha' : 'Alarm'}},
    '655' : {'name':'Disarmed', 'handler':'partition_state_change', 'status' : {'alarm' : False, 'armed_stay' : False, 'armed_zero_entry_delay': False, 'armed_away' : False, 'exit_delay' : False, 'entry_delay' : False, 'alpha' : 'Disarmed'}},
    '656' : {'name':'Exit Delay in Progress', 'handler':'partition_state_change', 'status':{'exit_delay' : True, 'alpha' : 'Exit Delay In Progress'}},
    '657' : {'name':'Entry Delay in Progress', 'handler':'partition_state_change', 'status':{'entry_delay' : True, 'alpha' : 'Entry Delay in Progress'}},
    '663' : {'name':'ChimeOn', 'handler':'partition_state_change', 'status': {'chime': True}},
    '664' : {'name':'ChimeOff', 'handler':'partition_state_change', 'status': {'chime': False}},
    '673' : {'name':'Busy', 'handler':'partition_state_change', 'status': {'alpha': 'Busy'}},
    '700' : {'name':'Armed by user', 'handler':'partition_state_change'},
    '750' : {'name':'Disarmed by user', 'handler':'partition_state_change', 'status' : {'alarm' : False, 'armed_stay' : False, 'armed_away' : False, 'armed_zero_entry_delay': False, 'exit_delay' : False, 'entry_delay' : False, 'alpha' : 'Disarmed'}},
    '751' : {'name':'Disarmed special', 'handler':'partition_state_change', 'status' : {'alarm' : False, 'armed_stay' : False, 'armed_away' : False, 'armed_zero_entry_delay': False, 'exit_delay' : False, 'entry_delay' : False, 'alpha' : 'Disarmed'}},
    '840' : {'name':'Trouble LED', 'handler':'partition_state_change', 'status':{'trouble' : True}},
    '841' : {'name':'Trouble Clear', 'handler':'partition_state_change', 'status':{'trouble' : False}},

#GENERAL UPDATES
    '621' : {'name':'FireAlarmButton', 'handler':'keypad_update', 'status':{'fire' : True, 'alarm': True, 'alpha' : 'Fire Alarm'}},
    '622' : {'name':'FireAlarmButtonOff', 'handler':'keypad_update', 'status':{'fire' : False, 'alarm': False, 'alpha' : 'Fire Alarm Cleared'}},
    '623' : {'name':'AuxAlarmButton', 'handler':'keypad_update', 'status':{'alarm': True, 'alpha' : 'Aux Alarm'}},
    '624' : {'name':'AuxAlarmButtonOff', 'handler':'keypad_update', 'status':{'alarm': False, 'alpha' : 'Aux Alarm Cleared'}},
    '625' : {'name':'PanicAlarmButton', 'handler':'keypad_update', 'status':{'alarm': True, 'alpha' : 'Panic Alarm'}},
    '626' : {'name':'PanicAlarmButtonOff', 'handler':'keypad_update', 'status':{'alarm': False, 'alpha' : 'Panic Alarm Cleared'}},
    '631' : {'name':'SmokeAlarmButton', 'handler':'keypad_update', 'status':{'alarm': True, 'alpha' : 'Smoke Alarm'}},
    '632' : {'name':'SmokeAlarmButtonOff', 'handler':'keypad_update', 'status':{'alarm': False, 'alpha' : 'Smoke Alarm Cleared'}},
    '660' : {'name':'PGM Output is in Progress', 'handler':'message_response_error'},
    '670' : {'name':'Invalid Access Code', 'handler':'command_response_error'},
    '671' : {'name':'Function Not Available', 'handler':'command_response_error'},
    '672' : {'name':'Failure to Arm', 'handler':'command_response_error'},
    '680' : {'name':'System in Installers Mode', 'handler':'message_response_error'},
    '701' : {'name':'Special Closing', 'handler':'message_response_error'},
    '702' : {'name':'Partial Closing - one or more zones have been bypassed', 'handler':'message_response_error'},
    '800' : {'name':'LowBatTrouble', 'handler':'keypad_update', 'status':{'bat_trouble': True, 'alpha' : 'Low Battery'}},
    '801' : {'name':'LowBatTroubleOff', 'handler':'keypad_update', 'status':{'bat_trouble': False, 'alpha' : 'Low Battery Cleared'}},
    '802' : {'name':'ACTrouble', 'handler':'keypad_update', 'status':{'ac_present': False, 'alpha' : 'AC Power Lost'}},
    '803' : {'name':'ACTroubleOff', 'handler':'keypad_update', 'status':{'ac_present': True, 'alpha' : 'AC Power Restored'}},
    '829' : {'name':'SystemTamper', 'handler':'keypad_update', 'status':{'alpha' : 'System tamper'}},
    '830' : {'name':'SystemTamperOff', 'handler':'keypad_update', 'status':{'alpha' : 'System tamper Restored'}},
    '849' : {'name':'Verbose Trouble Status', 'handler':'verbose_status'},
    '912' : {'name':'Command Output Pressed', 'handler':'output_pressed'},
}

evl_Errors = {
	'000' : {'description' : 'No Error'},
	'001' : {'description' : 'Receive Buffer Overrun (a command is received while another is still being processed)'},
	'002' : {'description' : 'Receive Buffer Overflow'},
	'003' : {'description' : 'Transmit Buffer Overflow'},
	
	'010' : {'description' : 'Keybus Transmit Buffer Overrun'},
	'011' : {'description' : 'Keybus Transmit Time Timeout'},
	'012' : {'description' : 'Keybus Transmit Mode Timeout'},
	'013' : {'description' : 'Keybus Transmit Keystring Timeout'},
	'014' : {'description' : 'Keybus Interface Not Functioning (the TPI cannot communicate with the security system)'},
	'015' : {'description' : 'Keybus Busy (Attempting to Disarm or Arm with user code)'},
	'016' : {'description' : 'Keybus Busy – Lockout (The panel is currently in Keypad Lockout – too many disarm attempts)'},
	'017' : {'description' : 'Keybus Busy – Installers Mode (Panel is in installers mode, most functions are unavailable)'},
	'018' : {'description' : 'Keybus Busy – General Busy (The requested partition is busy)'},
	
	'020' : {'description' : 'API Command Syntax Error'},
	'021' : {'description' : 'API Command Partition Error (Requested Partition is out of bounds)'},
	'022' : {'description' : 'API Command Not Supported'},
	'023' : {'description' : 'API System Not Armed (sent in response to a disarm command)'},
	'024' : {'description' : 'API System Not Ready to Arm (system is either not-secure, in exit-delay, or already armed)'},
	'025' : {'description' : 'API Command Invalid Length'},
	'026' : {'description' : 'API User Code not Required'},
	'027' : {'description' : 'API Invalid Characters in Command (no alpha characters are allowed except for checksum)'},
}

