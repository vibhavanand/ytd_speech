import youtube_audio
import split_audio_final
import speech_text_final
import audio_enhancements

import os
import pathlib
import random
import string
import pandas as pd

def ytd_audio_splitting_enhacing_mapping(youtube_link,download_location,split_location,transformation_location,noise_file_location):
    characs="AbCdE"
    youtube_file_name="banking"+characs+".wav"
    # youtube_file_name="bankingbZytQ.wav"
    youtube_dir=download_location
    youtube_link = youtube_link


    youtube_audio.download_audio(youtube_link,youtube_dir,youtube_file_name)


    split_file_location = split_location
    split_audio_final.silence_second_bw_8_12_secs_chunks(youtube_dir+youtube_file_name,split_file_location)
    speech_text_dict=speech_text_final.convert_to_speech(split_file_location) #some changed have to be made to transcribe only the files for a particular youtube video  

    ##enhancements in audio
    audio_enhancements_location = transformation_location
    noise_file = noise_file_location#"/media/edl-90/WD Elements/Vibhav/Office work/practice/diff files/second/noise_1.wav"
    #changes to be made to include the audio files for that particular audio files only
    basepath = split_file_location
    for entry in os.listdir(basepath):
        a=os.path.join(basepath, entry)
        if os.path.isfile(a):
            print(entry)

            audio_enhancements.final_function(a,noise_file,audio_enhancements_location)



    ##matching the enhanced files with their text
    file_text_dict={}
    basepath=audio_enhancements_location#"/media/edl-90/WD Elements/Vibhav/Office work/practice/audio/youtube_downloaded/split_files/audio_enhanced_files/"

    for a in os.listdir(basepath):
        try:
            start_index=0
            for count,input_char in enumerate(a):
                if((int(ord(input_char)) >= 65 and int(ord(input_char)) <= 90) or (int(ord(input_char)) >= 97 and int(ord(input_char)) <= 122)):
                    start_index = count
                    break
            common_name=a[start_index:]

            # dict_b[common_name][]

            matching_file_path=basepath+a    
            text=speech_text_dict[common_name][0]

            size  = os.path.getsize(matching_file_path)
            list1=[size,text]
            file_text_dict[matching_file_path]=list1
            
            
        except Exception as e:
            print(e)
    return youtube_file_name,file_text_dict


# print(file_text_dict)

def publish_to_csv(location,speech_dict,file_name):
    new_dataframe = pd.DataFrame()
    for a,b in speech_dict.items():
        print(a,b)
        new_dataframe = new_dataframe.append({'wav_filename':a,'wav_filesize':b[0],'transcript':b[1]},ignore_index=True)

    new_dataframe = new_dataframe[['wav_filename', 'wav_filesize', 'transcript']]
    new_dataframe=new_dataframe.set_index('wav_filename')
    
    new_dataframe.to_csv(location+file_name+".csv")

#publish_to_csv("/media/edl-90/WD Elements/Vibhav/Office work/practice/audio/youtube_downloaded/transcribed_text.csv",file_text_dict)



#youtube downloaded name=file name + random 5 characters
#split file = ^+ c+(number of split)
#enhanced audio = numericals according to changes + ^
ytd_audio_splitting_enhacing_mapping("https://www.youtube.com/watch?v=FIEiReyph4M","/media/edl-90/WD Elements/Vibhav/Office work/practice/audio","/media/edl-90/WD Elements/Vibhav/Office work/practice/audio","/media/edl-90/WD Elements/Vibhav/Office work/practice/audio","/media/edl-90/WD Elements/Vibhav/Office work/practice/audio")