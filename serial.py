"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start=100):
        self.start = int(start)
        self.current = self.start
    
    
    def generate(self):
        self.current +=1
        return self.current
    
    def reset(self):
        self.current = self.start


        
serial = SerialGenerator(start=100)
print(serial.generate())


