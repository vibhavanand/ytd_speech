import xlwt , os
from xlwt import Workbook
import speech_recognition as sr
from threading import Thread , active_count
import time
#import pocketsphinx
# Workbook is created
def convert_to_speech(rootdir):
    file_names=os.listdir(rootdir)
    file_text_dict={}

    count = 1
    r=sr.Recognizer()
    for i , file in enumerate(file_names):
        name=file
        file=rootdir+file
        print (file)
        size  = os.path.getsize(file)
        try:
            with sr.AudioFile(file) as source:
                
                audio_data = r.record(source)
                
                try:
                    text = r.recognize_google(audio_data)
                    file_text_dict[name]=[text,size]
                    print(text)
                    count = count + 1 
                
                except Exception as e  :
                    print ("in except")
                    print (e,1)
                    
                    text = "No data"
                    continue
        except Exception as e:
            print("file error")
            
            print(e,2)
            continue
    return file_text_dict
        
    print(file_text_dict)
    end = time.time()
    print(end  - start)

def publish_csv(dict_a):
    wb=Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 0, 'wav_filename')#remember the complete path has to be passed in this. In the function convert_to_speech only the filename is being passed.
    sheet1.write(0, 1, "wav_filesize")
    sheet1.write(0, 2, 'transcript')
    i=1
    for key,value in dict_a.items():
        sheet1.write(i, 0, key)
        sheet1.write(i, 1, value[1])
        sheet1.write(i, 2, value[0])
        i+=1
    wb.save("/media/edl-90/WD Elements/Vibhav/Office work/practice/audio/aftermakingfunction")
    print("workbook published")    

#pool = Pool()
# rootdir = "/media/edl-90/WD Elements/Vibhav/Office work/practice/audio/split_files/"
start = time.time()

# text_dict=convert_to_speech(rootdir)
# publish_csv(text_dict)



