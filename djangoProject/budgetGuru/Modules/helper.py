import random
import string

# Generate a random string of chosend length
def generateRandomeString(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase +
                             string.digits, k=N))
    return res