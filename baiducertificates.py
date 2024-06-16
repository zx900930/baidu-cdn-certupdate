import copy
import json
import os
import sys
from baidubce.auth import bce_credentials
from baidubce import bce_base_client, bce_client_configuration
from dotenv import load_dotenv

# Install dependencies: pip install -r requirements.txt

def load_env_file(file_path):
    if os.path.exists(file_path):
        load_dotenv(dotenv_path=file_path)

# Set default .env file
default_env_file = ".env"

# Check if an alternative .env file is provided as a command-line argument
if len(sys.argv) > 1:
    alternative_env_file = sys.argv[1]
    load_env_file(alternative_env_file)
else:
    load_env_file(default_env_file)

# Retrieve the values from environment variables or use default values
AK = os.getenv("AK", "ACCESS_KEY")
SK = os.getenv("SK", "SECRET_KEY")
ENDPOINT = os.getenv("ENDPOINT", "https://cdn.baidubce.com")
FULLCHAIN_PATH = os.getenv("FULLCHAIN_PATH", "/www/server/panel/vhost/cert/example.net/fullchain.pem")
PRIVKEY_PATH = os.getenv("PRIVKEY_PATH", "/www/server/panel/vhost/cert/example.net/privkey.pem")
DOMAIN = os.getenv("DOMAIN", "example.net")
CERTNAME = os.getenv("CERTNAME", DOMAIN + "-latest")

# Read fullchain cert and privkey
with open(FULLCHAIN_PATH, 'r') as cert:
    CERT = cert.read()
    #CERTSTRING = CERT[27:36].strip()
with open(PRIVKEY_PATH, 'r') as key:
    KEY = key.read()

# Print the values to verify
print("AK:", AK)
print("SK:", SK)
print("ENDPOINT:", ENDPOINT)
print("FULLCHAIN_PATH:", FULLCHAIN_PATH)
print("PRIVKEY_PATH:", PRIVKEY_PATH)
print("DOMAIN:", DOMAIN)
print("CERTNAME:", CERTNAME)
print("CERTNAME:", CERTNAME)
print("CERTNAME:", CERTNAME)

# Send POST request to Baidu CDN's API
class Sample(bce_base_client.BceBaseClient):

    def __init__(self, config):
        self.config = copy.deepcopy(bce_client_configuration.DEFAULT_CONFIG)
        self.config.merge_non_none_values(config)

    def run(self):
        path = b'/v2/'+DOMAIN+'/certificates'
        print("APIPATH:", path)
        headers = {
            b'Content-Type': 'application/json'
        }
        

        params = {}
        payload = json.dumps({
    "certificate": {
        "certName": CERTNAME,
        "certServerData": CERT,
        "certPrivateData": KEY
    },
    "httpsEnable": "ON"
})

        return self._send_request(b'PUT', path, headers, params, payload)

if __name__ == '__main__':

    config = bce_client_configuration.BceClientConfiguration(credentials=bce_credentials.BceCredentials(AK, SK),
                                                                endpoint=ENDPOINT)
    client = Sample(config)
    res = client.run()
    print(res.__dict__)
