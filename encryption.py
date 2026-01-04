
#The XOR Encryption
#it takes raw bits and uses them to lock the message
#It is One Time Pad Encryption
#The hacker cannot read the data even if they have the mail
#------------------------------------
#This converts the message  to binary 8-bit ascii
#XOR the each key
#------------------------------------
class QuVault:

    def xor_cipher(self, message, bit_key):
        messageBin = ''.join(format((ord(i), '08b') for i in message))

        encryptedBits = ''
        for i in range(len(messageBin)):
            m_bit = int(messageBin[i])
            k_bit = int(bit_key[i%len(bit_key)])
            encrypteBite += str(m_bit^k_bit)
        return encryptedBits

