# zombie-system-demo
A simple setup that demonstrates concept of zombie computer and using it for dos. 

# Setup
1. Two machines with python3 installed (here one windows, other kali linux)
2. Zombie systems are generally part of botnet but for this simple demo, there is only 1 zombie system.

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
2. Port forwarding
3. Editing SOURCE/TARGET ip/port.

# Improvement Ideas
1. Implement more than one zombie hosts using Mininet. (I haven't explored it completely, dont know if its possible.)
2. Using an .exe file instead of Zombie.py script on victim. (on windows)
3. Improving the Controller.

# Video Demo for reference
Dont judge me for using Bandicam :P


[![Video for Demo](doc/ss_demo_zombie.PNG)](https://vimeo.com/544670967 "Simple Demo")

