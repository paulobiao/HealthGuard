
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64, os, json

def _get_key():
    key = os.environ.get("HG_AES_KEY")
    if not key:
        # Dev only: derive a key to make demo easier
        key = base64.urlsafe_b64encode(b"healthguard-demo-key-32bytes!!").decode()
    return base64.urlsafe_b64decode(key + "===")

def encrypt(plaintext: bytes) -> str:
    key = _get_key()
    iv = get_random_bytes(12)
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    ct, tag = cipher.encrypt_and_digest(plaintext)
    blob = iv + tag + ct
    return base64.b64encode(blob).decode()

def decrypt(token: str) -> bytes:
    raw = base64.b64decode(token)
    iv, tag, ct = raw[:12], raw[12:28], raw[28:]
    key = _get_key()
    cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
    return cipher.decrypt_and_verify(ct, tag)
