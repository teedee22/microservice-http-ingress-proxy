Outer proxy entry to system

Proxy receives a payload including a message and also an integer. The integer represents the number of seconds to sleep for before multiplying it by a random number and sending it to next worker

The next worker saves the number of second slept for onto a redis database