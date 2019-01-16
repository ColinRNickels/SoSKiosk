# SoSKiosk
Raspberry Pi and Arduino based project to highlight student project

<<<<<<< HEAD
##To Do
[] startPlaying
    - flashStart
    - setProgress
    - callOmx
    - checkRFID

[] stopPlaying
    - flashStop
    - resetProgressbar
    - killOMX
    - checkRFID

[] flashStart
    - two blinks green
    - some pattern showing it's playing

[] flashStop
    - two blinks red

[] setProgress
    - playtime = length of song
    - for x in numOfLed: light led(x)
        wait perled
    - stopPlaying

[] killOMX
    - sudo killall OMXPlayer

=======












































## Logical Flow
                          +------------------+
                          |                  |
                          |    checkRFID     |
                          |                  |
                          +------+-----------+
                                 |
                                 |
                                 |
                                 |
                          +------+-----------+
                          |                  |
                          |  RFIDVal = null  |
                          |                  |
                          +------+-----------+
                                 |
                             No  |    Yes
                       +---------+----------------+
                       v                          v
             +---------+-------------+    +-------+---------+
             |                       |    |                 |
             |  RFIDVal = nowPlaying |    |  waiting = true |
             |                       |    |                 |
             +---------+-------------+    +--------+--------+
                       |                           |
                       |                           |
             No        |      Yes               No |         Yes
           +-----------+---------+              +--+-----------+
           |                     |              |              |
           |                     |              |              |
+----------+------------+  +-----+----+  +------+------+  +----+-----+
|                       |  |          |  |             |  |          |
| startPlaying(RFIDVal) |  | Continue |  | stopPlaying |  | Continue |
|                       |  |          |  |             |  |          |
+------------------------  +----------+  +-------------+  +----------+
>>>>>>> 9f8a6d725bca27445544717b1d091366ccbe3d25
