from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import blockalgo
key = b'alvinolessalessa'
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_ECB)

msg = cipher.encrypt(b'k\xbd\xcaD&\n=\xc6#\xa7\xa9\xd6\x9c\x05I\x0f')

print('\nCiphertext:', msg)

decryp_msg = cipher.decrypt(msg)

print('\nDecrypt Message: ', decryp_msg)
print('\n')
