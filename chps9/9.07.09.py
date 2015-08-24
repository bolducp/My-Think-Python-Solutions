"""Recently I had a visit with my mom and we realized that the two digits
that make up my age when reversed resulted in her age. For example, if she’s 73,
I’m 37. We wondered how often this has happened over the years but we got
sidetracked with other topics and we never came up with an answer.
“When I got home I figured out that the digits of our ages have been reversible
six times so far. I also figured out that if we’re lucky it would happen again in
a few years, and if we’re really lucky it would happen one more time after that.
In other words, it would have happened 8 times over all. So the question is, how
old am I now?”
Write a Python program that searches for solutions to this Puzzler. Hint: you
might find the string method zfill useful."""


def is_reverse(x, y):
    x = str(x).zfill(2)
    y = str(y).zfill(2)
    return x == y[::-1]


def car_talk_9():
        for y in range(100):
            for x in range(100):
                if x != y and is_reverse(x, y):
                    print x, y
                    print "difference is:" + str(y - x)
                x += 1
                y += 1
car_talk_9()