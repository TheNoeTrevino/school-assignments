# Homework 2 - Noe Trevino

## 1

### Question

What is meant by spread spectrum?
List and explain each type of spread spectrum? 
Give the advantages of spread spectrum over a fixed-frequency transmission?

### Answer

Spread spectrum is the act of sending your transmission signal across multiple
signals by either doing Frequency Hopping Spread Spectrum, or Direct Sequence
Spread Spectrum.  

The two types that we have spoken of this far are FHSS and DSSS.
First, FHSS. This is the act of using multiple frequencies to send to our data.
We will send a certain amount of our data, this unit is called the 'hop time',
then we will switch to another of the frequencies that has already been decided
up on by the order. For example, "hel" will be sent on frequency 1, "lo "

Second, DSSS is the act of sending your signal with a pseudo noise on
top of it. Making the signal itself take up more bandwidth, similarly to FHSS.

The benefits of these two are that it will make it more difficult to intercept,
jam, and tamper with. 

## 2

### Question

What is the role of a medium access control (MAC) protocol in wired and wireless
networks, and why is it essential for efficient communication?

### Answer

There are many types of MAC protocols. They all achieve the goal of making sure
that each transited signal is sent through the correct frequencies for each
device, avoiding collision. If a collision is made, each different MAC protocol
has a way to deal with such a thing. These are essential to make sure we do not
overlap transmission signals with mishaps like using the same carrier frequency,
etc...

## 3

### Question

Explain how Carrier Sense Multiple Access with Collision Detection (CSMA/CD)
works in wired Ethernet. Why is CSMA/Collision Avoidance (CSMA/CA) used in
wireless networks instead?

### Answer

CSMA/CD works by checking if the wire is idle or not. If the wire is idle, we
will send our signal. If a collision, which can happen during our vulnerability
window, happens the receiver will tell the whole network that a collision has
occurred. 

With CSMA/CA, we reserve time slots to transmit out signals. Since the time is
set, when others try to communicate with the receiver they will be not allowed,
avoiding the collision in the first place. 

[source](https://www.geeksforgeeks.org/carrier-sense-multiple-access-csma/)

## 4

### Question

How does the hidden node problem affect wireless communication, and what techniques
(e.g., RTS/CTS) are used to mitigate it?

### Answer

The hidden node problem happens when two devices, that are out of range of each
other, try to communicate with an access point. The two devices, unknowingly
transmitting at the same time, cause a collision. We can avoid this problem with
the RTS/CTS protocol. We will send a RTS, and the access point will reserve a
certain amount of time for us to transmit. This will allow devices out of range
to know that there a transmission in progress. This is how we perform collision
avoidance with wireless networks.

## 5

### Question

A Code Division Multiple Access (CDMA) wireless system assigned the following
unique codes to users X, Y and Z for shared medium access simultaneously:
U X = [-1, 1, -1, 1, -1, 1, -1, 1]
U Y = [-1, 1, 1, -1, -1, 1, 1, -1]
U Z = [-1, -1, 1, 1, -1, -1, 1, 1]

a. Determine the decoder output of the receiver if user X transmits a data bit 1, user Y
    transmits a data bit 1, and when user Z transmitting data bit 0;

b. Determine the composite signal transmitted on a common transmission channel.

c. Draw the waveform of the data available in the channel for (b) the above
    transmission

### Answer

a. User X transmitting a data bit 1: [-1, 1, -1, 1, -1, 1, -1, 1]
   User Y transmitting a data bit 1: [-1, 1, 1, -1, -1, 1, 1, -1]
   User Z transmitting a data bit 0: [1, 1, -1, -1, 1, 1, -1, -1]

b. NOTE: I assume we are talking about the composite signal of question a. Not
   the values in the chipping sequence, but the values of 1, 1 and 0. 
   Answer [-1, 3, -1, -1, -1, 3, -1, -1] 

c. NOTE: This was attached to the assignment as a separate file since I drew it
   by hand. 


