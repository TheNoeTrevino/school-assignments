# Homework 1 - Noe Trevino

## Question 1

What is wireless communication, and how does it differ from wired
communication in terms of technology and applications?

### Answer

Wireless communication is the act of sending data of any sort via signals,
rather than a wired connection. 

It differs from wired communication in terms of difficulty, since we use radio frequencies
to send symbols with a defined meaning. Wired connection use electrical signals. 

In terms of application, wireless connections are much more diverse. We can use
it to connect in an extremely large range. For example, streaming videos off the
internet, downloading data, and viewing the internet. 

## Question 2

What challenges do wireless networks face in ensuring reliable communication
in environments with high user density, such as stadiums or urban areas?

### Answer 

The immediate challenge would be the increase of noise in the medium. This can
distort signals and make them more difficult to be interpreted by the receiver.
There can also be the improper reusing of frequencies, which will cause
corrupted data and slow down operations made by the receiver. There is also a
possible overload on the sender, since the access point will probably be in a
similar area. 

## Question 3

How does a sinusoidal waveform contribute to the modulation of signals in
wireless communication protocols?

### Answer 

These types of waveforms provide us with three main properties to use for
modulation: 

1. Amplitude shift
2. Frequency shift
3. Phase shift

We can use these properties to encode data, and give the receiver a place to
'listen', or receive the signal. First example of this that comes to mind is the
radio frequencies on a car. You can tune in to your favorite one by just
scrolling to it. For example 104.1fm, is one I tune into occasionally. These
properties allow us to choose a combination of which will provide a stabe, and
fast connection. It will also allow us to modulate these properties depending on
the environment we are in. 

## Question 4

Define Frequency Shift Keying (FSK), Amplitude Shift Keying (ASK) and
Phase Shift Keying. Give example of each.

### Answer 

1. Amplitude Shift Keying 

We can change height of the wave. To represent another symbol. A wave twice as
high as another can represent 1, while the smaller one represents 0.

A common example is a waveform taking up some amount of time. Representing one.
In the next segment of that time, the waveform will be completely flat, or have
of the amplitude. Representing 0

3. Frequency Shift Keying

The changing the speed at which a wave completes. A wave twice as ***fast*** can
represent 1. While the slower one will represent 0. 

It is hard to describe this in text, but you can imagine a waveform taking a
certain amount of time. This will represent 0. In the next segment of that
amount of time, the wave form will double in its frequency, representing 1.

4. Phase Shift Keying 

We can use the angle at which the signal starts to represent different values.
This one seems to me to be the most versatile. A wave starting at angle of 0
will be 00, one starting at angle 90, can be 01, one starting at 180 degrees, can
be 10, 270 can be 11. This allows us to send symbols at a higher rate. Although,
it is at risk from a unfavorable SNR. Although this is difficult to depict only
through text, we can think of: dictating a symbol depending on the starting
angle of our waveform.

## Question 5

What is multiplexing in communication systems? Explain the purpose and
importance of multiplexing in maximizing the utilization of communication
channels.

### Answer

Multiplexing is used when a channels bandwidth is not fully utilized. We take
advantage of the bandwidth by carrying multiple signals on the same medium, more
efficiently using the bandwidth.

With scenarios like multiple people in a same room, doing different things on
their phone, multiplexing multiple signals into one allows us to fully utilize
the potential of the channel.

## Question 6

Explain the significance of antennas in wireless communication systems. How
do different antenna design impact signal propagation and coverage?

### Answer 

Their main use is to convert electrical signals into electromagnetic waves,
which we can use to communicate wirelessly. 

Antennas can help by moving the place in which our electromagnetic fields come
from. Rather than having then on the ground, or in a building, which would cause
a lot of obstructions automatically, we can place them outside, in a more
central place, and higher. This will increase the radius by getting above
the obstructions. 

Different deigns, like the parabolic antenna which gives us a more focused
direction of the signal, will give us different advantages and what not. 

## Question 7

A company is claiming that they have a modulation and FEC technique that will
allow nearly error free data transmission at a rate of 80 Mbps
over a 20 MHz channel that has an SNR of 5 dB with white, Gaussian noise.
Give a brief explanation of why this is, or is not, credible. Show your
calculations.

### Answer 

We will use Shannon's Theorem for this problem.

C = Blog_2(1+SNR)

C = 20,000*log_2(1+3.16)

I used a website to calculate the linear scale of the decibels

C = 20,000*log_2(4.16)

C = 20,000*2.07

C = 41,700

So the channel's maximum bandwidth is 41.7Mbps, not even close to 80. This is
not credible

## Question 8

A wireless communication system operates over a noiseless channel with a
bandwidth of 20 MHz and achieves a channel capacity of 100 Mbps. Determine
how many signal levels are required to achieve this channel capacity.

### Answer 

For noiseless channels we will use the Nyquist formula

B = 20,000

C = 100,000

C = 2B log_2(M)

M = 2^(C/2B)

M = 2^(100,000/40,000)

M = 2^2.5

M = around 5.55

6 signal level are required to achieve the channel capacity.



