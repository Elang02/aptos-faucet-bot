
from aptos_sdk.account import Account
from aptos_sdk.client import FaucetClient, RestClient
import json
import requests
from anticaptchaofficial.hcaptchaproxyless import *
import random
username = 'user'
password = 'password'
port = 22225
while True:
  try:
    session_id = random.random()
    super_proxy_url = ('http://%s-session-%s:%s@zproxy.lum-superproxy.io:%d' %(username, session_id, password, port))
    proxies = {
      'http': f'{super_proxy_url}',
      'https': f'{super_proxy_url}'
    }
    proxies1={
      "http": "http://user:pass@p.webshare.io:80/",
      "https": "http://user:pass@p.webshare.io:80/"
    }
    
    solver = hCaptchaProxyless()
    solver.set_verbose(1)
    solver.set_key("db62450188e83a2f39c438fdf1976d33")
    solver.set_website_url("https://devnet.atodex.io/")
    solver.set_website_key("5b44f9d5-027c-4f4a-bd94-0012ce2f418e")
    #:!:>section_1
    NODE_URL = 'https://aptos-devnet.nodereal.io/v1'
    FAUCET_URL = 'https://tap.devnet.prod.gcp.aptosdev.com'
    rest_client = RestClient(NODE_URL)
    faucet_client = FaucetClient(FAUCET_URL, rest_client)  # <:!:section_1
    s = requests.Session()
    #:!:>section_2
    alice = Account.generate()
    private_key = alice.private_key
    address = alice.address()
    params = {
      'address': f'{address}',
      'amount': '10000000000',
    }
    for i in range(2):
      response = requests.post('https://faucet.devnet.aptoslabs.com/mint', params=params, proxies=proxies1)
    headers = {
      'authority': 'api-dev.atodex.io',
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'en-US,en;q=0.9',
      'authorization': 'Bearer',
      'origin': 'https://devnet.atodex.io',
      'referer': 'https://devnet.atodex.io/',
      'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
  }

    params = {
        'address': f'{address}',
    }
    response = s.get('https://api-dev.atodex.io/auth/get_nonce', params=params, headers=headers, proxies=proxies, timeout=2)
    print(f"Address: {alice.address()}")
    print(f"Balance: {rest_client.account_balance(alice.address())}")
    payload = {
      "function": "0x563e8382514ccdcc0c0a83469c9262d22d0b052316c1bd67286ba42bb11d0815::FaucetV1::request",
      "type_arguments": [
        "0x563e8382514ccdcc0c0a83469c9262d22d0b052316c1bd67286ba42bb11d0815::TestCoinsV1::ADX"
      ],
      "arguments": [
        "0x563e8382514ccdcc0c0a83469c9262d22d0b052316c1bd67286ba42bb11d0815"
      ],
      "type": "entry_function_payload"
    }
    txn_hash = rest_client.submit_transaction(alice, payload)
    rest_client.wait_for_transaction(txn_hash)
    payload = {
      "function": "0x563e8382514ccdcc0c0a83469c9262d22d0b052316c1bd67286ba42bb11d0815::FaucetV1::request",
      "type_arguments": [
        "0x563e8382514ccdcc0c0a83469c9262d22d0b052316c1bd67286ba42bb11d0815::TestCoinsV1::USDT"
      ],
      "arguments": [
        "0x563e8382514ccdcc0c0a83469c9262d22d0b052316c1bd67286ba42bb11d0815"
      ],
      "type": "entry_function_payload"
    }
    txn_hash = rest_client.submit_transaction(alice, payload)
    rest_client.wait_for_transaction(txn_hash)
    payload = {
      "function": "0x563e8382514ccdcc0c0a83469c9262d22d0b052316c1bd67286ba42bb11d0815::AtodexSwapPoolV1::swap_exact_coins_for_coins_entry",
      "type_arguments": [
        "0x563e8382514ccdcc0c0a83469c9262d22d0b052316c1bd67286ba42bb11d0815::TestCoinsV1::USDT",
        "0x563e8382514ccdcc0c0a83469c9262d22d0b052316c1bd67286ba42bb11d0815::TestCoinsV1::ADX"
      ],
      "arguments": [
        "500000000",
        "802636"
      ],
      "type": "entry_function_payload"
    }

    txn_hash = rest_client.submit_transaction(alice, payload)
    rest_client.wait_for_transaction(txn_hash)
    payload = {
      "function": "0x563e8382514ccdcc0c0a83469c9262d22d0b052316c1bd67286ba42bb11d0815::AtodexSwapPoolV1::add_liquidity_entry",
      "type_arguments": [
        "0x1::aptos_coin::AptosCoin",
        "0x563e8382514ccdcc0c0a83469c9262d22d0b052316c1bd67286ba42bb11d0815::TestCoinsV1::ADX"
      ],
      "arguments": [
        "20000000",
        "69224844",
        "19100000",
        "55622595"
      ],
      "type": "entry_function_payload"
    }


    txn_hash = rest_client.submit_transaction(alice, payload)
    rest_client.wait_for_transaction(txn_hash)
    time.sleep(3)
    pubkey = alice.public_key()
    json_data = json.loads(response.text)
    nonce = json_data['data']['nonce']
    msg = f'APTOS\nmessage: {address}\nnonce: {nonce}'
    in_value = bytes(msg, 'utf-8')
    signature = alice.sign(in_value)
    headers = {
        'authority': 'api-dev.atodex.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'origin': 'https://devnet.atodex.io',
        'referer': 'https://devnet.atodex.io/',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    }

    json_data = {
        'address': f'{address}',
        'sign': f'{signature}',
        'publicKey': f'{pubkey}',
    }

    response = s.post('https://api-dev.atodex.io/auth/login', headers=headers, json=json_data, proxies=proxies)
    json_data = json.loads(response.text)
    token = json_data['data']['token']
    capt = solver.solve_and_return_solution()
    headers = {
        'authority': 'api-dev.atodex.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {token}',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        'origin': 'https://devnet.atodex.io',
        'referer': 'https://devnet.atodex.io/',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    }

    json_data = {
        'mission_id': 1,
        'token': f'{capt}',
    }

    response = s.post('https://api-dev.atodex.io/mission/claim-mission-captcha-v2', headers=headers, json=json_data, proxies=proxies)
    json_data = json.loads(response.text)
    status = json_data['data'][0]['status']
    if not status == '1':
      time.sleep(2)
      response = s.post('https://api-dev.atodex.io/mission/claim-mission-captcha-v2', headers=headers, json=json_data, proxies=proxies)
      print(response.text)
    capt = solver.solve_and_return_solution()
    json_data = {
        'mission_id': 3,
        'token': f'{capt}',
    }
    response = s.post('https://api-dev.atodex.io/mission/claim-mission-captcha-v2', headers=headers, json=json_data, proxies=proxies)
    capt = solver.solve_and_return_solution()
    json_data = {
        'mission_id': 8,
        'token': f'{capt}',
    }
    response = s.post('https://api-dev.atodex.io/mission/claim-mission-captcha-v2', headers=headers, json=json_data, proxies=proxies)
    print(response.text)
    response = s.get('https://api-dev.atodex.io/user/get-point', headers=headers, proxies=proxies)
    print(response.text)
    json_data = json.loads(response.text)
    code = json_data['error_code']
    point = json_data['data']['point']
    print(f'Point : {point}')
    rest_client.close()
    if code == '':
      with open('atodex.txt', 'a')as f:
        f.write("{0}|{1}\n".format(address,private_key))
    else:
      print('Failed')
  except Exception as e:
    print(e)
    continue