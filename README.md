# zombie-system-demo
A simple setup that demonstrates concept of zombie computer and using it for dos. 

# Setup
1. Two machines with python3 installed (here one windows, other kali linux)
2. Zombie systems are generally part of botnet but for this simple demo, there is only 1 zombie system.
3. This is more like a python reverse connect script. Treat it like one.

# If you want to consider some scenario
1. Host a sample website where there is a link to download the Zombie.py baiting victim.
2. Send the file through email.

# Usage
1. Clone/Download the repo
2. Copy the Zombie.py to victim machine. (here windows)
3. Place the Controller.py in attacker machine. 
4. Place the server file on either a third machine(if possible) or on the attacker machine.
5. Now, we will use zombie to dos the server flask file. So, run the server file first. Open it in browser and its displays instantly.
6. Run the Zombie script on victim.
7. Run the Controller script on attacker machine.
8. Check for status of Zombie system using 'c' or 'C'.
9. Start the attack by entering 'a' or 'A'.
10. Open the server url in browser and eventually loading of page slows down and at a point complete connection is refused.

# Things you may need to do 
1. Turn off your AV/Firewall or make firewall rules for ports needed.
2. IP/Port forwarding (For example, through ngrok)
3. Editing SOURCE/TARGET ip/port.

# Working Screenshots
![Controller](https://user-images.githubusercontent.com/83397936/118151432-3de8db80-b431-11eb-9751-2a73bb399c2e.JPG)
![response1](https://user-images.githubusercontent.com/83397936/118151458-46d9ad00-b431-11eb-9e98-1fcd96af14c9.JPG)
![response2](https://user-images.githubusercontent.com/83397936/118151479-4c36f780-b431-11eb-8e3f-23554fa8c7df.JPG)
![response](https://user-images.githubusercontent.com/83397936/118151489-50631500-b431-11eb-900a-5bd3dde22795.JPG)

# Improvement Ideas
1. Implement more than one zombie hosts using Mininet. (I haven't explored it completely, dont know if its possible.)
2. Using an .exe file instead of Zombie.py script on victim. (on windows) // I did this using pyinstaller. I had to use freeze_control() to run multithreads properly.
3. Improving the Controller.
4. Adding functionality of poping up ads or sending emails through victim.
5. Privilege Escalation if needed.  

# Video Demo for reference
Dont judge me for using Bandicam :P

Note: This was for previous version. Command execution is shown in screenshot, video yet to be updated.
[![Video for Demo]](https://vimeo.com/544670967 "Simple Demo")

