import re
import shutil

content = ''
def out_string():
  with open('automation/notes.txt', 'r') as f:
    return f.read()

phone = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
email = r'\S+@\S+'
os = out_string()
ph = re.findall(phone, os)
em = re.findall(email, os)
# em.append('under.jlopez@yahoo.comEvent')
# print(em)
def duplicate_email():
  new_e_list = []
  for i in em: 
    if i not in new_e_list: 
      new_e_list.append(i)
  print(new_e_list)
  print(len(new_e_list))
  return new_e_list 
def duplicate_phone():
  new_list = []
  for i in ph: 
    if i not in new_list: 
      new_list.append(i)
  print(new_list)
  print(len(new_list))
  return new_list 

def store_info(info, file):
  info.sort()
  sorted_files = open_file(file).split('\n')
  with open(file, "a+") as f:
    for data in info:
      if data in sorted_files:
        return False
      else:
        f.write(data + '\n')
# list(dict.fromkeys(phone_numbers))
if __name__ == "__main__":
  duplicate_email()
  store_info(new_e_list, email.txt)
  
  # duplicate_phone()
  print(len(em))
  

