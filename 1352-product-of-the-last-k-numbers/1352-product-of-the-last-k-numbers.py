class ProductOfNumbers:

    def __init__(self):
        # Initialize with 1 to handle the division logic seamlessly
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # A zero resets the contiguous product sequence
            self.prefix = [1]
        else:
            # Append the running prefix product
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is larger than the elements we've seen since the last 0, 
        # it means the last k elements include a 0.
        if k >= len(self.prefix):
            return 0
            
        # The product of the last k elements is the total product divided 
        # by the product of elements just before the last k elements.
        return self.prefix[-1] // self.prefix[-k - 1]