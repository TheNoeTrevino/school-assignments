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

TODO

[source](https://www.geeksforgeeks.org/carrier-sense-multiple-access-csma/)

## 4

### Question

How does the hidden node problem affect wireless communication, and what techniques
(e.g., RTS/CTS) are used to mitigate it?

### Answer

TODO

## 5

### Question

A Code Division Multiple Access (CDMA) wireless system assigned the following
unique codes to users X, Y and Z for shared medium access simultaneously:
U X = [-1, 1, -1, 1, -1, 1, -1, 1]
U Y = [-1, 1, 1, -1, -1, 1, 1, -1]
U Z = [-1, -1, 1, 1, -1, -1, 1, 1]

(a) Determine the decoder output of the receiver if user X transmits a data bit 1, user Y
    transmits a data bit 1, and when user Z transmitting data bit 0;
(b) Determine the composite signal transmitted on a common transmission channel.
(c) Draw the waveform of the data available in the channel for (b) the above
    transmission

### Answer

(a) User X transmitting a data bit 1: [-1, 1, -1, 1, -1, 1, -1, 1]
    User Y transmitting a data bit 1: [-1, 1, 1, -1, -1, 1, 1, -1]
    User Z transmitting a data bit 0: [1, 1, -1, -1, 1, 1, -1, -1]
