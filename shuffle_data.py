import os
import sys
from random import shuffle


imgpath = '/home/wei/Documents/ww/img_align_celeba'

def write_list(impath,im_list):
	with open(impath,'w') as file:
		for items in im_list:
			file.write(items+'\n')


def shuffle_data(imgpath,ratio=0.2):
	train = []
	val = []
	imgs_list= []
	for im_p in os.listdir(imgpath):
		im_pn = os.path.join(imgpath,im_p)
		imgs_list.append(im_pn)

	l_im = len(imgs_list)
	shuffle(imgs_list)
	l_val = int(l_im*ratio)
	l_tra = l_im - l_val
	train = imgs_list[:l_tra]
	val = imgs_list[l_tra:]
	write_list('shuffle_train.list',train)
	write_list('shuffle_val.list',val)
	return train,val

if __name__=='__main__':
	shuffle_data(imgpath)