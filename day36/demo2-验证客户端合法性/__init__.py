import hmac
obj = hmac.new(key = b'secret_key',msg =b'11010012922')
print(obj.hexdigest())

obj = hmac.new(key = b'secret_key',msg =b'11010012922')
print(obj.hexdigest())