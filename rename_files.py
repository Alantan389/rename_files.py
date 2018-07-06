import os
def rename_files():
	# step1, get files name from the folder
	file_list=os.listdir(r"/Users/yourcomputerusername/Desktop/Into_Udacity/prank")
	#print(file_list)
	saved_path=os.getcwd()
	print("Current Working Directory is "+saved_path)
	os.chdir(r"/Users/yourcomputerusername/Desktop/Into_Udacity/prank")
	
	# step2, for each file, rename filename
	for file_name in file_list:
		os.rename(file_name,file_name.translate(None,"0123456789"))
		

rename_files()
