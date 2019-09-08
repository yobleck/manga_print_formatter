#convert Yokohama Kaidashi Kikou into correct format for printing
#by Yobleck
#chrome://bookmarks/?id=2620

import os;
from PIL import Image; #"," whatever other modules are needed    #https://pillow.readthedocs.io/en/stable/
import numpy;

maindir = "f:/documents/ykk_hard"; #main directory that will be worked out of
maindir_list = os.listdir(maindir); #list of volumes
#print (maindir_list); #vol_x (1-14) variable chapter count and image count
output_dir = maindir + "/output"; #output folder

for i in range(9,10): #loop through volumes 1-14     #x,x+1 if only doing one volume at a time
	if(i==2): #chap 2 exception
		vol_dir = (maindir + "/vol_" + str(i));
		vol_dir_list = ['8','9','10','11','12','13','14','15']; #doing this because 8 != 08    #os.listdir(maindir + "/vol_" + str(i));
		#print("vol: " + str(i));
		print(vol_dir);
		#print(vol_dir_list);
		output_vol_dir = (output_dir + "/vol_" + str(i));
	else:	
		vol_dir = (maindir + "/vol_" + str(i)); #volume directory
		vol_dir_list = os.listdir(maindir + "/vol_" + str(i)); #list of chapters in each volume
		#print("vol: " + str(i));
		print(vol_dir);
		#print(vol_dir_list);
		output_vol_dir = (output_dir + "/vol_" + str(i));
		
	for j in range(int(vol_dir_list[0]) , int(vol_dir_list[1])): #loop through chapters             #second number is chap in question when doing only one   #have to add 1 for final chapter
		chap_dir = (vol_dir + "/" + str(j)); #chapter directory
		chap_dir_list = os.listdir(vol_dir + "/" + str(j)); #list of images in each chapter
		#print("chap: " + str(j));
		print(chap_dir);
		#print(chap_dir_list);
		output_chap_dir = (output_vol_dir + "/" + str(j));
		
		for k in range(0 , len(chap_dir_list)): #loop through images        #old: range(int(chap_dir_list[0][0:3])-1 , int(chap_dir_list[len(chap_dir_list)-1][0:3]))
			print(chap_dir_list[k]);
			
			tempbool = True;
			if(tempbool == True):
				#looping through images should work now 9-8-19 sun morning
				
				original_img = Image.open(chap_dir + "/" + chap_dir_list[k]); #open original image	image.open()
				
				copy_img = original_img.copy(); #copy image	image.copy()
				
				original_img.close(); #close original image to avoid accidental overwrites
				
				copy_resized = copy_img.resize((1682,2475),Image.BICUBIC); #resize copy	image.resize((width,height),PIL.Image.BICUBIC)  #https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.resize
				
				output_img = Image.new("RGBA",(3600,4500),color=(255,255,255)); #create 8.5x11 or 12x15 image	image.new("RGB",(width,height),color=(255,255,255))  #https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
				
				if(int(chap_dir_list[k][0:3])%2==0): #even numbered pages
					output_img.paste(copy_resized,box=(1918,1100)); #copy and paste onto blank template  	 image.paste(copy_resized,box=(0,1100))
				elif(int(chap_dir_list[k][0:3])%2!=0): #odd numbered pages
					output_img.paste(copy_resized,box=(0,1100)); 
					#alternating images have to have opposite shifting so can be printed on front and back of paper
					#also don't forget to to format reading right to left
					
				output_img.save(output_chap_dir + "/" + chap_dir_list[k][0:3] + ".png","PNG",dpi=(300,300)) #save image with correct name  image.save(chap_dir + "/" + chap_dir_list[k][0:3] + ".png","PNG") #occasionally screws up thumbnails / see thumbnail()?
				
				output_img.close(); #rewriting existing files causes resizing problems. make sure to delete test files
	

	
#testimg = Image.open(maindir + "/vol_1/2/001.jpg");
#print(testimg.size);
#testimg.close();
#testblank = Image.new("RGBA",(100,100),color=(255,255,255));
#testblank.save(maindir + "/testblank.png","PNG",dpi=(300,300));