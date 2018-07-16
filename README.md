# EOS_Python_API

eos API Reference



### get_info :

- /v1/chain/get_info   
- 返回包含区块链的各种详细信息的对象。 



###  get_block :

- /v1/chain/get_block   
- 返回一个对象，其中包含有关区块链上特定块的各种详细信息。 



### get_block_header_state :

- /v1/chain/get_block_header_state 



### get_account :

- /v1/chain/get_account
- 返回一个对象，其中包含有关区块链上特定帐户的各种详细信息。 



### get_abi:

- /v1/chain/get_abi 



### get_code:

- /v1/chain/get_code 

- 返回一个对象，其中包含有关区块链上特定智能合约的各种详细信息。 



### get_table_rows :

- v1/chain/get_table_rows 

- 返回包含指定表中行的对象。 



### get_currency_balance

- http://127.0.0.1:8888/v1/chain/get_currency_balance 



## abi_json_to_bin

- http://127.0.0.1:8888/v1/chain/abi_json_to_bin 

- 将json序列化为二进制十六进制。生成的二进制十六进制通常用于push_transaction中的数据字段。 



## abi_bin_to_json

- http://127.0.0.1:8888/v1/chain/abi_bin_to_json 

- 将二进制十六进制序列化为json。 
- 

## get_required_keys

- http://127.0.0.1:8888/v1/chainget_required_keys 

- 返回签署事务所需的密钥。

  

## get_currency_stats

- http://127.0.0.1:8888/v1/chainget_currency_stats 



## get_producers

- http://127.0.0.1:8888/v1/chainget_producers 
- 

## push_block

- http://127.0.0.1:8888/v1/chain/push_block 



## push_transaction

- http://127.0.0.1:8888/v1/chainpush_transaction 

- 此方法需要JSON格式的事务，并尝试将其应用于区块链。 



## push_transactions

- http://127.0.0.1:8888/v1/chain/push_transaction 

- 此方法需要JSON格式的事务，并尝试将其应用于区块链。此方法一次推送多个事务。 
