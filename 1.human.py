
from glob import glob

val_img_list = glob('/make/dataset/valid/images/*.jpg')
train_img_list = glob('/make/dataset/train/images/*.jpg')
print(len(val_img_list))
print(len(train_img_list))


with open('dataset/train.txt','w') as f:
    f.write('\n'.join(train_img_list)+'\n')

with open('dataset/val.txt','w') as f:
    f.write('\n'.join(val_img_list)+'\n')


import yaml

with open('dataset/data.yaml', 'r') as f:
  data = yaml.safe_load(f)

print(data)

data['train'] = '/make/dataset/train.txt'
data['val'] = '/make/dataset/val.txt'

with open('dataset/data.yaml', 'w') as f:
   yaml.dump(data,f)
print(data)    