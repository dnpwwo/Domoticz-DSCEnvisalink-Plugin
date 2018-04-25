#The MIT License (MIT)
#Copyright (c) 2016 Dan Cinnamon
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

class AlarmState:
    """Helper class for alarm state functionality."""

    @staticmethod
    def get_initial_alarm_state(maxZones, maxPartitions):
        """Builds the proper alarm state collection."""

        _alarmState = {'partition': {}, 'zone': {}}

        for i in range(1, maxPartitions + 1):
            _alarmState['partition'][i] = {'status': {'alarm': False, 'alarm_in_memory': False, 'armed_away': False,
                                                      'ac_present': True, 'armed_bypass': False, 'chime': False,
                                                      'armed_zero_entry_delay': False, 'alarm_fire_zone': False,
                                                      'trouble': False, 'bat_trouble': False, 'ready': False, 'fire': False,
                                                      'armed_stay': False, 'alpha': 'N/A', 'beep': False,
                                                      'exit_delay': False, 'entry_delay': False, 'last_disarmed_by_user': '',
                                                      'last_armed_by_user': '' }}
        for j in range (1, maxZones + 1):
            _alarmState['zone'][j] = {'status': {'open': False, 'fault': False, 'alarm': False, 'bypass': False, 'tamper': False}, 'last_fault': 0}

        return _alarmState