import os

import sys

import shutil

#FUNCTION TO DISPLAY MFG MENU

def MFG_menu():
    print(
        """
  __  __   ______    _____     _____    ______    _____   _____    _____   _   _ 
 |  \/  | |  ____|  / ____|   |  __ \  |  ____|  / ____| |_   _|  / ____| | \ | |
 | \  / | | |__    | |  __    | |  | | | |__    | (___     | |   | |  __  |  \| |
 | |\/| | |  __|   | | |_ |   | |  | | |  __|    \___ \    | |   | | |_ | | . ` |
 | |  | | | |      | |__| |   | |__| | | |____   ____) |  _| |_  | |__| | | |\  |
 |_|  |_| |_|       \_____|   |_____/  |______| |_____/  |_____|  \_____| |_| \_|
                                                                                                                                                   
 """)
    
    print("*=*"*12)
    print("[1] === Create Standard Directory  *")
    print("[2] === Delete Directory           *")
    print("[3] === Addional Directory         *")
    print("[4] === View Directories           *")
    print("[0] === Exit                       *")
    print("*=*"*12)
    print()
    option = str(input(">> "))
    
MFG_menu()


#create month of the year folder 
def months_folder():
    
    jan_dec = ["January", "February", "March", "April", "May","June","July","August","September", "October", "November", "December"]
    
    for month in range(len(jan_dec)):
        
        #mkdirectory(thePath, jan_dec[month])
        os.mkdir(jan_dec[month])

def mkdirectory(path, name):
        
    directory = os.path.join(path, name)
    
    os.mkdir(directory)
    
#CREATING  THE STANDARD FOLDERS 
def subfolders_of_subfolder(thePath, theList, mainCounter):
  
  actual_position = mainCounter
    
  theCounter = 0

  newPath = thePath+f"\{actual_position}"
  
  while theCounter < len(theList):
            
        mkdirectory(newPath, theList[theCounter])
                
        theCounter += 1

def standard_folders(actualfolderpath):
    
    #main direcories array
    
    main_dirs = ["Client Folder", "Logo", "Advertising","Photography", "Website", "Theme","Pluggins", "SLA-Web Requirement"]
    
    
    #  subdirectories arrays
    
    logo_sub_dirs = ["Artwork","Junk","Final"]
    
    advertising_sub_dirs = ["Social Media", "Google Ads"]
    
    socialMedia_sub_dirs = ["Artwork", "Posts","Stats"]
    
    socialMedia_artwork_sub_dirs = ["Junk","2022"]
    
    googleAds_sub_dirs = ["Stats", "Reports"]
    
    website_sub_dirs = ["Artwork","Images","Exports & Backups", "Updates"]
    
    jan_dec = ["January", "February", "March", "April", "May","June","July","August","September", "October", "November", "December"]

    #main directories and subdirectoies counters for while loop
    
    main_dirs_counter = 0
    
    
    while main_dirs_counter < len(main_dirs):
    
        mkdirectory(actualfolderpath, main_dirs[main_dirs_counter])
        
        #creating subfolders for the main folder 
        
        if  main_dirs[main_dirs_counter] == "Logo":
            
            subfolders_of_subfolder(actualfolderpath,logo_sub_dirs, main_dirs[main_dirs_counter])
        
        if  main_dirs[main_dirs_counter] == "Advertising":
            
            subfolders_of_subfolder(actualfolderpath, advertising_sub_dirs, main_dirs[main_dirs_counter])
            
           # folder_navigate = actualfolderpath+f"/{main_dirs[main_dirs_counter]}"
           
            for i in range(len(advertising_sub_dirs)):
                
                if advertising_sub_dirs[i] == "Social Media":
                    
                    recreated_path = actualfolderpath+f"/{main_dirs[main_dirs_counter]}"
                    
                    subfolders_of_subfolder(recreated_path, socialMedia_sub_dirs, advertising_sub_dirs[i])
                    
                    social_array_for_month_folder =  ["Posts","Stats"]
                    
                    if subfolders_of_subfolder:
                        
                        social_media_subfolder_path = actualfolderpath+f"/{main_dirs[main_dirs_counter]}/{advertising_sub_dirs[i]}"
                        
                        for folder in range (len(social_array_for_month_folder)):
                            
                            subfolders_of_subfolder(social_media_subfolder_path,jan_dec, social_array_for_month_folder[folder])
                            
                        
                        for artwork in range(len(socialMedia_sub_dirs)):
                            
                            if socialMedia_sub_dirs[i] == "Artwork":
                                
                                subfolders_of_subfolder(social_media_subfolder_path, socialMedia_artwork_sub_dirs,socialMedia_sub_dirs[i])
                                
                                if subfolders_of_subfolder:
                                    
                                    social_media_subfolder_path +=f"/{socialMedia_sub_dirs[i]}"
                                    subfolders_of_subfolder(social_media_subfolder_path,jan_dec,socialMedia_artwork_sub_dirs[1])
                                
                                break
        
                 
                if advertising_sub_dirs[i] == "Google Ads":
                    
                    recreated_path = actualfolderpath+f"/{main_dirs[main_dirs_counter]}"
                    
                    subfolders_of_subfolder(recreated_path,googleAds_sub_dirs, advertising_sub_dirs[i])
                    
                    if subfolders_of_subfolder:
                        
                        google_ads_subfolder_path = actualfolderpath+f"/{main_dirs[main_dirs_counter]}/{advertising_sub_dirs[i]}"
  
                        for i in range(len(googleAds_sub_dirs)):
                            
                             subfolders_of_subfolder(google_ads_subfolder_path, jan_dec,googleAds_sub_dirs[i])
                             

        
        if main_dirs[main_dirs_counter] == "Website":
                  
            subfolders_of_subfolder(actualfolderpath,website_sub_dirs,main_dirs[main_dirs_counter])
        
        main_dirs_counter +=1
        
 
#grouping folders into their specific alpgabetical group
def alphabetical_group():
    
    alphabetical_groups = ["A","B","C", "D", "E","F","G","H", "I","J","K", "L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    global website_name
    
    website_name = str(input("Enter Website name >> "))
    
    alphabetical_letter = website_name[0].upper()
    
    
    for letter in alphabetical_groups: 
        
        if alphabetical_letter in alphabetical_groups:
            
           # this the actual path of the folde r grouped based on the alphabetical group
           
           global variable_group_path
           
           variable_group_path = Rf"C:\Users\$USERNAME\OneDrive\Office\Clients\{alphabetical_letter}"
           
           global actual_group_path;
           actual_group_path = os.path.expandvars(variable_group_path)
           
         
           global variable_actual_folder_path
           
           variable_actual_folder_path = Rf"C:\Users\$USERNAME\OneDrive\Office\Clients\{alphabetical_letter}\{website_name}"
          
           global actual_folder_path
           actual_folder_path = os.path.expandvars(variable_actual_folder_path)
             
           #Calling the mkdirectory function, to create the directory on the specific group
           
           if not os.path.exists(actual_folder_path):
               
                 mkdirectory(actual_group_path, website_name)
                 
                 standard_folders(actual_folder_path)   
                 
                 os.startfile(actual_folder_path)
               
           else:
               
               print("This Folder already exists")
               
               os.startfile(actual_folder_path)
                
           break
            
alphabetical_group()
