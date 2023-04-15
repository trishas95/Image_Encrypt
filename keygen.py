import random
import func
import prime

class PrivateKey:
    """
    note:
        λ: lowest common multiple of p-1 and q-1
        μ: modular multiplicative inverse of λ and n
    """
    
    def __init__(self, p, q, n):

        self.λ = func.lcm( p-1, q-1)
        self.μ = func.multiplicative_inverse( self.λ, n)
        
    def __repr__(self):
        return ("---\nPrivate Key :\nλ:\t"+str(self.λ) +"\nμ:\t"+str(self.μ) +"\n---")


class PublicKey:
    """
    attributes:
        n: product of two primes
        g: a random number such that,
    """
    def __init__(self, n):
        self.n = n
        self.nsq = n * n
        self.g = n+1
    
    def __repr__(self):
        return ("---\nPublic Key :\nn:\t"+ str(self.n) +"\n---")


def generate_keys(bitlen=128):
    
    p = prime.generate_prime(bitlen)
    q = prime.generate_prime(bitlen)
    n = p * q
    return (PublicKey(n), PrivateKey(p, q, n))


def Encrypt(public_key, plaintext):
    """
    It encrypts the plaintext using the given public key.

    """
    
    r = random.randint( 1, public_key.n-1)
    while not func.xgcd( r, public_key.n)[0] == 1:
        r = random.randint( 1, public_key.n)
        
    a = pow(public_key.g, plaintext, public_key.nsq)
    b = pow(r, public_key.n, public_key.nsq)
    
    ciphertext = (a * b) % public_key.nsq
    return ciphertext


def Decrypt(public_key, private_key, ciphertext):
    """
    It decrypts the ciphertext using the given public key and private key.
   
    """
    
    x = pow(ciphertext, private_key.λ, public_key.nsq)
    L = lambda x: (x - 1) // public_key.n
    
    plaintext = (L(x) * private_key.μ) % public_key.n 
    return plaintext


def homomorphic_add(public_key, a, b):
    """
    adds encrypted integer a to encrypted integer b 
  
    """
    return (a * b) % public_key.nsq


def homomorphic_add_constant(public_key, a, k):
    """
    adds a plaintext k to encrypted integer a
  
    """
    return a * pow( public_key.g, k, public_key.nsq) % public_key.nsq


def homomorphic_mult_constant(public_key, a, k):
    """
    multiplies a plaintext k to encrypted integer a

    """
    return pow(a, k, public_key.nsq)