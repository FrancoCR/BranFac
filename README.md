## BranFac
System Call based Smart IDS for Android. Project for Wei Yangs 6332 System Security and Malicious Code Analysis class at UTD. Project consists of Brandon Marzik and Franco Covarrubias-Reyes. The IDS is meant to capture kernel calls from an application and determine if the application is malicious based on parameters set for our AI, BINKS. 



## Tools Used to Create BranFac and Conduct Testing
1. Genymotion
2. Tensorflow
3. Android Studio

### How to Submit Flags

Before you can submit flags, you have to discover the Bluetooth MAC address of your device.  Here are a couple example commands to help you find your device:

Tool and command used to collect kernel calls:   
```` strace  ````

Tool and command used to fuzz input to the application:
```` monkey  ````

Command used to transfer the logs out of our rooted device:  
```` adb pull su  ````

Show score with bleah:  
```` sudo bleah -b "30:ae:a4:20:79:da" -e ````

The 25 malware samples in testing were taken from a pool of the drebin and GNOME repositories. Opposite of this the benign applications were ripped directly from the play store and chosen based on network activity and overall popularity. 

##UPDATE PENDING
