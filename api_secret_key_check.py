import os
from fireblocks_sdk import *

apiKey = os.environ['FIREBLOCKS_API_KEY']
apiSecret = open('fireblocks_secret.key', 'r').read()

fb = FireblocksSDK(apiSecret, apiKey)
print(fb.get_internal_wallets())
print('done')
