from timeofprocessing import counter
from time import sleep


@counter
def test(t):
    sleep(t)


test(1)
