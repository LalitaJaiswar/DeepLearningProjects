import os 
  
# Function to rename multiple files
def main(): 
    i = 1417
      #C:\Users\csc28032018h\Desktop\AKTU Internship\300_training\n
    for filename in os.listdir('C:/Users/csc28032018h/Desktop/Project/Dataset/traffic_training3/Class3_200/'): 
        dst ="f" + str(i) + ".jpg"
        src ='C:/Users/csc28032018h/Desktop/Project/Dataset/traffic_training3/Class3_200/'+ filename 
        dst ='C:/Users/csc28032018h/Desktop/Project/Dataset/traffic_training3/Class3_200/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 