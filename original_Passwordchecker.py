import math
import hashlib
import requests
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle

psswd=list(input("Enter your password:\n"))

my_list = [1, 2, 3, 4, 5]
psswd_int = ''.join(str(x) for x in psswd)

upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digits=['0','1','2','3','4','5','6','7','8','9']
special=['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|','\\',':',';','"',"'",'<','>',',','.','?','/']

def Upper(psswd,upper):
 if any(ch in upper for ch in psswd):
    print("Uppercase character found!")
    return 1
 else:
    print("Uppercase character not found.")
    return 0

def Lower(psswd,lower):
 if any(ch in lower for ch in psswd):
    print("Lowercase character found!")
    return 1
 else:
    print("Lowercase character not found.")
    return 0

def Digits(psswd,digits):
 if any(ch in digits for ch in psswd):
    print("Digits found!")
    return 1
 else:
    print("Digits not found.")
    return 0
 
def Special(psswd,special):
 if any(ch in special for ch in psswd):
    print("Special character found!")
    return 1
 else:
    print("Special character not found.")
    return 0

def Len_str(psswd):
 if len(psswd) <=5:
    print("Password Length : SMALL")
    return 1
 elif len(psswd) <=10:
    print("Password Length : MADIUM")
    return 1
 elif len(psswd) <=15:
    print("Password Length : BIG")
    return 1

def Strength(psswd):
    strength = 0

    if any(ch in upper for ch in psswd):
        strength += 0.5
    if any(ch in lower for ch in psswd):
        strength += 0.5
    if any(ch in digits for ch in psswd):
        strength += 0.5
    if any(ch in special for ch in psswd):
        strength += 0.5
    if len(psswd) >= 8:
        strength += 2
    print(f"Your password's strength is {strength}/4.0")
    return strength

def Strength_str(strength):
 if strength < 3:
    print("Strength Level: VERY WEAK")
 elif strength < 5:
    print("Strength Level: WEAK")
 elif strength < 7:
    print("Strength Level: MODERATE")
 else:
    print("Strength Level: STRONG")



def charset_size(psswd):
    size = 0
    if any(ch in upper for ch in psswd):
        size += 26
    if any(ch in lower for ch in psswd):
        size += 26
    if any(ch in digits for ch in psswd):
        size += 10
    if any(ch in special for ch in psswd):
        size += 32
    return size

def Entropy(passwd,size):
   f=open("entropy_model.pkl",'rb')
   model=pickle.load(f)
   length=len(passwd)
   entropy = model.predict([[length, size]])
   print(f"Your password's entropy is {entropy}/100")
   return entropy

def Entropy_str(entropy):
    if entropy < 20:
        print("Entropy Level: VERY WEAK")
    elif entropy < 30:
        print("Entropy Level: WEAK")
    elif entropy < 55:
        print("Entropy Level: MODERATE")
    else:
        print("Entropy Level: STRONG")

def hashing(psswd_int):
   hash_object = hashlib.sha1(psswd_int.encode('utf-8'))
   sha_hash = hash_object.hexdigest()
   sha1_hash = sha_hash.upper()
   sha2 = sha1_hash[:5]
   return sha2

def hashing2(psswd_int):
   hash_object2 = hashlib.sha1(psswd_int.encode('utf-8'))
   sha_hash2 = hash_object2.hexdigest()
   sha1_hash2 = sha_hash2.upper()
   sha2_2 = sha1_hash2[5:]
   return sha2_2

def api(sha2,sha2_2):
  API_URL = f"https://api.pwnedpasswords.com/range/{sha2}"
  response = requests.get(API_URL)
  response1 = response.text.splitlines() 
  for line in response1:
      suffix, count = line.split(':')
      if suffix == sha2_2:
         print(f"Password Status: LEAKED\nLeaked {count} times.")
         return int(count)
         break
  else:
     print("Password Status : NOT LEAKED")
     return 0



def risk_lvl(count):
   if count ==0:
      print("Risk Level : SAFE")
   elif 1<= count <=100:
      print("Risk Level : LOW")
   elif 100< count <=1000:
      print("Risk Level : MEDIUM")
   elif 1000< count <=10000:
      print("Risk Level : HIGH")
   elif  count > 10000:
      print("Risk Level : VERY HIGH")

new_psswd = []
   
def add_upper(upper,new_psswd):
   if not any(ch in upper for ch in new_psswd):
       new_psswd.insert(0,random.choice(upper))   
       return new_psswd
      
def add_lower(lower,new_psswd):
   if not any(ch in lower for ch in new_psswd):
       new_psswd.insert(0,random.choice(lower))   
       return new_psswd

def add_digits(digits,new_psswd):
   if not any(ch in digits for ch in new_psswd):
       new_psswd.insert(0,random.choice(digits))   
       return new_psswd

def add_special(special,new_psswd):
   if not any(ch in special for ch in new_psswd):
       new_psswd.insert(0,random.choice(special))   
       return new_psswd
   
def bp(new_psswd):
   add_upper(upper, new_psswd)
   add_lower(lower, new_psswd)
   add_digits(digits, new_psswd)
   add_special(special, new_psswd)
   while(len(new_psswd)<15):
    choice = random.choice([upper, lower, digits, special])
    new_psswd.append(random.choice(choice))
    random.shuffle(new_psswd)
    final_password=''.join(new_psswd)
   return final_password

def bp2(final_password,count):
   if 100 < count :
      print(f"Recommended password : {final_password}")
    
def add():
   add_upper(upper,new_psswd)
   add_lower(lower,new_psswd)
   add_digits(digits,new_psswd)
   add_special(special,new_psswd)

def list_char():
   Upper(psswd, upper)
   Lower(psswd, lower)
   Digits(psswd, digits)
   Special(psswd, special)


def final_verdict(strength,entropy,size,sha2, sha2_2):
   print("====== PASSWORD REPORT =========")
   Len_str(psswd)
   Strength_str(strength)
   Entropy_str(entropy)
   count = api(sha2, sha2_2)
   risk_lvl(count)
   bp2(final_password,count)
   print("================================")

list_char()
strength = Strength(psswd)
size = charset_size(psswd)
entropy = Entropy(psswd, size)
sha2 = hashing(psswd_int)
sha2_2 = hashing2(psswd_int)
final_password=bp(new_psswd)
final_verdict(strength,entropy,size,sha2, sha2_2)



# =================================[Graphing]===================================



df = pd.read_csv("dataset.csv")

data_entro= df["entropy"]
data_siz=df['size']

mu_entro= np.mean(data_entro)
sigma_entro = np.std(data_entro)
mu_siz= np.mean(data_siz)
sigma_siz = np.std(data_siz)

x_ent= np.linspace(min(data_entro), max(data_entro), 200)
y_ent= (1/(sigma_entro * np.sqrt(2 * np.pi))) * np.exp(-(x_ent - mu_entro)**2 / (2 * sigma_entro**2))

# Get corresponding y value on curve
y_uent = (1/(sigma_entro * np.sqrt(2 * np.pi))) * np.exp(-(entropy - mu_entro)**2 / (2 * sigma_entro**2))

while True:
   i = int (input("Select graph:"))
   if i == 1:
    plt.figure()
    plt.plot(x_ent, y_ent, color='black')
    plt.scatter(entropy, y_uent, marker='x', s=120) 
    plt.xlabel("Entropy")
    plt.ylabel("Density")
    plt.show()
   if i==2:
      plt.figure()
      plt.hexbin(df["size"], df["entropy"], gridsize=25, cmap='Greys')
      plt.colorbar(label="Density",)
      plt.scatter(size, entropy, marker='x', s=120)
      plt.xlabel("Password Length")
      plt.ylabel("Entropy")
      plt.title("Entropy vs Length ")
      plt.show()
   if i==3:
      plt.figure()
      plt.scatter(df["strength"], df["entropy"])
      plt.scatter(strength, entropy, marker='x', s=100)
      plt.xlabel("Strength")
      plt.ylabel("Entropy")
      plt.title("Strength vs Entropy (Your Password Highlighted)")
      plt.show()
   if i==4:
      plt.figure()
      plt.hist(df["entropy"])
      plt.axvline(entropy)
      plt.xlabel("Entropy")
      plt.ylabel("Frequency")
      plt.title("Entropy Distribution (Your Password Position)")
      plt.show()
   if i == 5:
      plt.figure()
      plt.hist(df["strength"])
      plt.axvline(strength)
      plt.xlabel("Strength")
      plt.ylabel("Frequency")
      plt.title("Strength Distribution (Your Password Position)")
      plt.show()
   if i==6:
      plt.figure()
      df["length"] = df["password"].apply(len)
      plt.bar(df["length"], df["strength"])
      plt.scatter(len(psswd), strength, marker='x', s=100)
      plt.xlabel("Password Length")
      plt.ylabel("Strength")
      plt.title("Strength vs Length")
      plt.show()
   if i==0:
      break
