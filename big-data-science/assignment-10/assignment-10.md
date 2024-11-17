# Assignment 1

## Question 1

Explain how Generative Adversarial Networks (GANs) work briefly. (1 point)

---

Answer:

GANs create new data similar to a training dataset. An example of this would be
something like a text to image model. You could start off with a large data set
of described images, and feed that into the training. Afterwards, when you input
a set of text, the GAN can look at its own training and replicate something
similar to what it has had been trained on. During the training process, we would have a
generator and a discriminator. The generator will generate data, and the
discriminator will judge that data and determine if it is similar to the
training data. The iterator will improve by taking feedback from the
discriminator, and this process will repeat.

## Q2:

Explain the roles of encoder and decoder in the Transformer architecture. (1 point)

---

Answer:

The encoder will take the user's input and process it into a matrix like
structure. This is so is is more easily processed by the model, better capturing
the relationships between the tokens and such. After this, the decoder will
decode the encoders output, and generate something most likely very similar. An
example would be:

Input: 'Yo what up' -> encoder -> decoder(encoders output) -> output: 'Hey, what's up'

This is why the technique is called a "transformer". It will get an input and
then transform it into something more appropriate.
