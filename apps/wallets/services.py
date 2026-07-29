from web3 import Web3
from cryptography.fernet import Fernet
from django.conf import settings
from .models import Wallet

def create_wallet_for_user(user):

    w3 = Web3()
    account = w3.eth.account.create()
    
    address = account.address
    private_key = account.key.hex()

    fernet = Fernet(settings.FERNET_KEY)
    encrypted_private_key = fernet.encrypt(private_key.encode()).decode('utf-8')

    wallet = Wallet.objects.create(
        user=user,
        address=address,
        private_key=encrypted_private_key,
        balance=0
    )
    
    return wallet