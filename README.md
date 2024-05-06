# NASA-SAFE-T-Beacon
## Introduction
This project was developed by Ataraxia is the SAR (Search and Rescue) Assisting Frequency-modulating Electronic Transceiver - known professionally as SAFE-T, for short. This device is essentially a handheld beacon that will assist NASA with Lunar Search and Rescue operations by transmitting position, navigation, and time (PNT) information to the appropriate parties. 

The Ataraxia team consists of Vatsal Modgil, Falak Fahim, Peyton Goodman, and Gabrielle Quemada. Dr. Joseph Morgan was the faculty advisor overseeing the project, which was sponsored by Matt Leonard, the President of T STAR. The beacon prototype was designed at the request of NASA, to be further developed by the Lunar Search and Rescue program to be used by astronauts in 2024. 

## Background and Rationale
The background of SAFE-T stems from NASA’s plan to return to the moon under the Artemis missions in 2024. With the Artemis program, NASA will establish a sustained presence on the Moon, opening more of the lunar surface to exploration than ever before. Currently, there is no adequate means of cislunar and lunar surface distress tracking coupled with a notification system, which will be a key element of safe exploration. Thus, the need for a mobile beacon arises. 

The intention is for SAFE-T to serve this purpose, as well as be capable of attaching to the Gandalf Staff - another project under development by several other ETID Capstone teams. The Gandalf Staff will be utilized in the upcoming years as a handheld extra-vehicular activity tool capable of lighting and remote imaging, and Ataraxia providing an automated distress tracking and notification system for the staff will only benefit the safety of lunar surface users. 

# Software contribution
The digital logic controlling the operation of SAFE-T can logically be broken into two parts: one for the general operation of the system, and one for the traversing of the menu and interacting with the mechanical buttons.  

For the general operation logic, SAFE-T initializes its home screen display and will try to connect to all of the data-collecting peripherals (heart monitor, GPS, etc.).  Once successfully initialized, nominal (normal) mode is entered and a series of checks occur.

In nominal mode SAFE-T awaits its mechanical buttons to be pressed by the user and will log and record any and all data it has at the given 15 minute interval rate (emergency mode differs).  This 15 minute period does not ‘freeze’ the device and prevent any interactions, it just simply denotes that the ‘automatic’ transmission of messages can only occur at set intervals. This establishes a ‘breadcrumb trail’ of information that rescue parties can use to search for potentially lost, unconscious, or disabled crew members.

As for emergency mode, SAFE-T will send ‘SOS’ messages at two specific time intervals depending on the time since activation of emergency mode: once every fifteen seconds during the first thirty minutes of an emergency, and once every minute after the first thirty minutes of an emergency.  

During this time, the beacon will still continue to operate in a ‘nominal’ mode setting, however every communication it makes will have its ‘Message Priority’ message field set to indicate that emergency mode has been triggered.  According to Ataraxia’s customer, a method to disable emergency mode manually is not required for such an early-staged prototype. 

Figure 1 summarizes the process described above.

![alt text](https://i.imgur.com/LSIKQFe.png)

Figure 1. Flowchart - Main Operation

The next portion of the digital logic behind SAFE-T’s operation is the logic behind sending messages by interacting with the onscreen menu of preformatted messages, as illustrated in Figure 12.  

The currently selected message on the screen is adjusted by the user pressing either the ‘up’ or ‘down’ buttons on the front face of the enclosure - which causes an internal variable representing an index to be updated and compared to ‘protective logic’.  This protective logic prevents the user from accessing the zero-th index (the ‘SOS’ text), and also prevents the user from accessing indexes that do not exist.  The ‘SOS’ text selection-prevention is different from the idea of preventing ‘index errors’ of indexes that are too large in the way that the ‘SOS’ text is in fact accessible, but only when the emergency button is pressed.

Once a message is highlighted/displayed on the screen, a check is made to determine if the ‘select’ button has been pressed.  If the ‘select’ button is pressed, SAFE-T will log any and all data it has access to and attempt to transmit a message over the 802.11n protocol to a nearby Gandalf Staff.  SAFE-T will only transmit messages if the ‘select’ button is pressed, allowing the user to freely navigate the menu of messages without accidentally sending an erroneous transmission.

![alt text](https://i.imgur.com/CKIALIX.png)
Figure 2. Flowchart - Message Sending

As for the method of SAFE-T internally storing data, it will utilize its onboard microSD card as a file system for not only its OS, but also file I/O and memory.  The chosen method of logging data is with a (.csv) file.  The file contains a column header indicating various information fields for things such as whether or not emergency mode has been triggered, the time, the message itself, the heart rate, latitude, longitude, etc..  By analyzing these logs, entire treks, missions, and even ‘stories’ can be inferred from the gathered information, with the following figure as an example of a story.  In this scenario (ignoring the artificial heart rate values) an excavation/science crew member acknowledges receiving a message and agrees to stay where they are before attempting to begin their mining work in the lunar south pole region, but they soon send out an SOS message indicating an emergency.  From the message log, it is clear and easy to follow that the crew member indicated an emergency due to a suit issue (low pressure) and declared that they were ‘on the way’ (OTW) back to the lander in order to correct the issue.  The (.csv) file’s labels and order of data presentation are not finalized, but serve to depict what a fully developed data logging system might look like. (Despite not being finalized, the data collected was generated using currently existing code, with the heart rate, latitude, and longitude values being simulated).

![alt text](https://i.imgur.com/oJGOdyp.png)
Figure 3. Example Data Log Analysis


NOTE: The Figure above utilizes an old version of the message logs, but is more ‘user friendly’ and easier to understand than the official, final rendition.


