# DeskFlasher
This is a Raspberry Pi that is installed under my current workstation desk. I have a small amount of electronics hooked up to the rasberry pi with a long Red LED strip.</br>

This desk flasher is build for suttle notifications. Currently when there is a change on a website RSS feed the desk pulses and flashes on and off for a short period of time to indicate a change. The flashing and pulsing does not indicate in any way what the update is, just that there is an update.</br>
## Installation
In order to get this working you will requried the following:
### Hardware
* Raspberry pi
* MOSFET * 7
* LED Strip
* 12v power source
* 5v power source
### Software
* Operating System: Rasbian <link>www.raspberrypi.org</link>
* ServoD
* Python Version (pre installed with OS)
#### Check You're Compatible
<code>~$ python --version</code></br>
Output:
<code> version </code>

### Servod installation and Configuration
For controlling of the LED dimming, I am using the servodriver from BLAH located here: <link>Location</link>. Documentation on how to install this is located in the GitHub. Catches that I had was, permissions and the service starting. I had small tweaking to the service permission as root is the only user that has access to the hardware directly in Linux out of the box.

### Hardware installation
I used a plastic case that I fould at my local hardware store in the impulse buy section. I cut out the network ports and pwoer cords, there is also an opening to connect the LED power cables. All electronics including the raspberry pi fit in the case. I have then screwed the case to the underside of the desk close to power. The LED strips I then attached to the underside of the desk that follows all the way around the room.

## Using the Notifications
To use the notifications, I am currently running the script within a <code>screen</code>. The RSS feed monitor is currently locked to a single RSS feed. The idea is to eventually grow this to a database driven reader allowing several feeds to be read and the sofware to look for triggers and not just on additions to the feed.</br>
To Run:
1. Change to the directory</br> <code> ~$ cd project_dir</code>
2. Adjust the variable of the URL accordingly. </br> <code>nano feed.py</code> </br> look for the line: bLAH BLAH and add your RSS feed you want to monitor.
3. Test the servod is working with a quick test <code>echo '255; >> servod </code>
