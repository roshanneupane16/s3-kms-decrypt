import boto3
import base64

def lambda_handler(event, context):
    # Create a session
    session = boto3.Session()
    
    # Create a KMS client
    kms = session.client('kms')
    
    # Decode the base64-encoded ciphertext blob and encode as bytes
    encrypted_key = ''
    encrypted_key_bytes = base64.b64decode(encrypted_key)
    
    # Specify the key ID
    key_id = 'arn:aws:kms:us-east-1:000000000:key/00000000-0000-0000-0000-000000000000'
    
    # Decrypt the key
    decrypted_key = kms.decrypt(
        KeyId=key_id, 
        CiphertextBlob=encrypted_key_bytes
    )['Plaintext']
    
    # Print the decrypted key
    print(decrypted_key)
    
    # Encode the decrypted key as base64
    decrypted_key_base64 = base64.b64encode(decrypted_key).decode('utf-8')
