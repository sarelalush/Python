"""
Student: Sarel Alush
ID: 316373851
Assignment no. 1
Program: encrypt.py
""" 

import random

#create dict with key(alphabeta) and values(from text) or zero
def create_dict_key_value(s = ""):
      dic_alphabet = {}
      j=0
      for i in range(97,123):
            dic_alphabet[chr(i)] = 0
      if s != "": #if this from text
            for k in dic_alphabet.keys():
                  dic_alphabet[k] = s[j] #enter from text to dict 
                  j+=1
      return dic_alphabet

#create keys randoms to dict(alphabet) 
def create_key():
      f = open("key.txt","w")
      dic_alphabet = create_dict_key_value() #create dict(alphabet) 
      rnd_alphabet = 0
      for k in dic_alphabet.keys(): #run all keys 
            while rnd_alphabet in dic_alphabet.values(): #check if random key is in dict 
                  rnd_alphabet = chr(random.randint(97,122))#if yes choose another
            dic_alphabet[k] = rnd_alphabet #found 
      f.write("".join(dic_alphabet.values()))#write to file 
      f.close()

#get text from file and encrypt to another file
def encrypt_text():
      f = open("plaintext.txt","r")#to encrypt
      f2 = open("key.txt","r") #keys
      f3 = open("ciphertext.txt","w")#encrypted
      st = [ch.lower() for ch in "".join(f.readlines())]#get the text from file
      st = list(st)#convert to list
      dic_alphabet = create_dict_key_value(f2.readline()) #create dict(alphabet) with keys from file
      for i in range(len(st)):
            if st[i].isalpha():
                  st[i] = dic_alphabet[st[i]] #encrypt 
      f3.write("".join(st))#write to file
      f3.close()
      f2.close()
      f.close()

#here the function get value and dic and return the key of this value!
def get_key_by_value(dic,value):
      search = 0
      for k,v in dic.items():
            if v == value: #found value
                  search = k #get the key
                  break
      return search

#decerypt from ciphertext.txt to another decrypted.txt
def decrypt_text():
      f = open("ciphertext.txt","r")
      f2 = open("key.txt","r")
      f3 = open("decrypted.txt","w")
      dic_alphabet = create_dict_key_value(f2.readline())#create dict(alphabet) with keys from file
      st = [ch for ch in "".join(f.readlines())] #get all text from file
      st = list(st) #text to list
      for i in range(len(st)):
            if st[i].isalpha():# if is alpha ..
                  st[i] = get_key_by_value(dic_alphabet,st[i]) #here we get value and find the key
      f3.write("".join(st))#write to file ..
      f3.close()
      f2.close()
      f.close()
      
#for check what user choose
def check_choose(c):
      if c =="k":
            create_key()
            print("Succsessful, your key found in key.txt")
      elif c == "e":
            encrypt_text()
            print("Succsessful, your Encrypt found in ciphertext.txt")
      elif c == "d":
            decrypt_text()
            print("Succsessful, your Decrypt found in decrypted.txt")
      else:
            print("Thank You And Good Bye :D")
            exit()

#menu for user ..
def menu():
      print("|Welcome to Crypto|")
      print("k - Create Key")
      print("e - Encrypt Text From plaintext.txt  To ciphertext.txt")
      print("d - Decrypt Text From ciphertext.txt to decrypted.txt")
      print("another - Exit")
      print("[To choose, click on one of the options and Enter]")
      user_choose = input("Your Choose Is : ")
      return user_choose

def main():
      check_choose(menu())
main()
