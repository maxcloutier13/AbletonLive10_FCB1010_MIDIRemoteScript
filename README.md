# AbletonLive10_FCB1010_MIDIRemoteScript
 Custom script for the Behringer FCB1010 (EurekaPROM chip 2.0)

Main mode meant for liveLooping and recording guitar clips hands free
- Move the selection (up/down, left/right)
- Smart launchtrack (On empty cell: record. While recording: Stop and play clip. On a playing clip: stop. On empty clip while other is playing: stop clip and record
- Prev/Next preset (to be mapped to VST)
- Play/Pause - Stop - Record

Various "prep and record" functions
- Stop New - Stop playing clip and select next available slot. Useful to start playing instead of clip before being ready to record new clip
- Set New - Keep playing clip and select next available slot. Useful to get ready.
- Record New - Stop playing clip, select next available slot and starts recording. 

-- Base Mode  - Recording/LiveLooping
| 1-6 | 2-7 | 3-8 | 4-9 | 5-10 |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Prev  | Next  | Play/Pause  | Stop/Reset  | Set New  |
| Left  | Right  | Stop New  | Record New  | Record/Launch  |

Pedals are currently not handled. 
