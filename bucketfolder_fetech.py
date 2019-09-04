import sys
import boto3
import os
import ast

os.system("rm -r [*")

client = boto3.client('s3',aws_access_key_id="xxxxxxxxxxxxx",aws_secret_access_key="xxxxxxxxxxxxxxx")

response = client.list_objects(
    Bucket='ct-mysql-backup',
    Delimiter="/",
    Prefix='mysql',
)

f= open("dblist.txt","w+")
path = os.getcwd()
data=[]
place="chaipoint-mysql-backup-2"
for i in response['CommonPrefixes']:
  f.write("%s"%(i['Prefix']))
  f.write('\n')
#  data.append(place+"/"+i['Prefix'])
#  print(i['Prefix'])
  ritesh = client.list_objects(
  Bucket='cp-mysql-backup-2',
  Delimiter="/",
  Prefix=i['Prefix']
      )
  typo = str(i['Prefix'])
  name="["+typo[:-1]+"]"
  os.mkdir(path+"/"+name)
  os.chdir(path+"/"+name)
  fi= open(name,"w+")
  for j in ritesh['CommonPrefixes']:
   k = j['Prefix'].split("/")
   fi.write("%s"%(k[1]))
   fi.write('\n')
  # print(j['Prefix'])
   tab = client.list_objects(
     Bucket='chp-mysql-backup-2',
     Delimiter="/",
     Prefix=str(j['Prefix'])
      )
   pars="["+k[1]+"]"    
   tablefi= open(pars,"w+")
   print(tab['Contents'])
   for t in tab['Contents']:
       ti = t['Key'].split("/")
       print(ti)
       tablefi.write("%s"%(ti[2]))
       tablefi.write('\n')
 # os.chdir(path)



#print(response['CommonPrefixes'])
#print(data)

#print(ritesh['CommonPrefixes'])
#print(ritesh['CommonPrefixes'])

#for i in response['CommonPrefixes']:
#  print(i['Prefix'])
