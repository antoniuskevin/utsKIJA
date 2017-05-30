import string
import random


def exclusive_or(list_ascii,key):
    xor_result=[]
    c = 0
    for x in list_ascii:
        #print x^key[c]
        xor_result.append(x^key[c])
        c+=1
        if c==len(key):
            c=0
    print xor_result
    return xor_result

def addition_mod(xor_result,key):
    add_result=[]
    c=0
    for x in xor_result:
       add_result.append(x+key[c])
       c+=1
       if c==len(key):
            c=0
    temp=[]
    c=0
    add_result_bin=[]
    for x in add_result:
        temp.append(format(x,'08b'))
        c+=1
        if c==4:
            xx=''.join(temp)
            if len(xx)>32:
                b=len(xx)-32
                xx=xx[b-1:]
            xx=[xx[i:i+8] for i in range(0, len(xx), 8)]
            for i in xx:
                add_result_bin.append(i)
            final_result=[]
            for i in add_result_bin:
                i=chr(int(i,2))
                final_result.append(i)
            temp=[]
            c=0
    print final_result
    final_result=''.join(final_result)
    return final_result
def subtract_mod (xor_result,key):
    add_result=[]
    c=0
    for x in xor_result:
       add_result.append(x-key[c])
       c+=1
       if c==len(key):
            c=0
    temp=[]
    c=0
    add_result_bin=[]
    for x in add_result:
        temp.append(format(x,'08b'))
        c+=1
        if c==4:
            xx=''.join(temp)
            if len(xx)>32:
                b=len(xx)-32
                xx=xx[b-1:]
            xx=[xx[i:i+8] for i in range(0, len(xx), 8)]
            for i in xx:
                add_result_bin.append(i)
            final_result=[]
            for i in add_result_bin:
                i=chr(int(i,2))
                final_result.append(i)
            temp=[]
            c=0
    final_result=''.join(final_result)
    return final_result

def encrypt():
    plaintext = raw_input("Masukkan plaintext:")
    list_ascii = [ord(c) for c in plaintext]
    key0 = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
    key1 = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
    key = []
    key = ''.join(key0 + key1)
    print "Key anda:" + key
    key0 = [ord(c) for c in key0]
    key1 = [ord(c) for c in key1]
    key = [ord(c) for c in key]
    xor_result = exclusive_or(list_ascii, key0)
    final_result = addition_mod(xor_result, key1)
    print "Ciphertext:" + final_result

def decrypt():
    chipertext = raw_input("Masukkan chipertext:")
    list_ascii = [ord(c) for c in chipertext]
    key = raw_input("Masukkan key:")
    key0 = key[:3]
    key1 = key[4:7]
    key0 = [ord(c) for c in key0]
    key1 = [ord(c) for c in key1]
    chipertext = [ord(c) for c in chipertext]
    subtract_result = subtract_mod(chipertext, key1)
    subtract_result = [ord(c) for c in subtract_result]
    final_result = exclusive_or(subtract_result, key0)
    print "Hasil:"
    for i in final_result:
        print chr(i)
        tfg,


menu= raw_input("Masukkan 1 untuk encrypt, 2 untuk decrypt")
if menu=='1':
    encrypt()
elif menu=='2':
    decrypt()