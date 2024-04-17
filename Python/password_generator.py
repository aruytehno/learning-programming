from itertools import chain
import random

print(''.join(str(x) for x in [chr(random.choice(list(chain(range(65, 91), range(97, 123), range(48, 58))))) for x in range(20)]))
