from pydub import AudioSegment
from pydub.playback import play
import os

# class Audio_enhancements(file1,file2):

# def __init__(self,file1,file2):
#     self.main_file = file1
#     self.noise = file2

# def loudness():
#     song = AudioSegment.from_mp3("vehicle_noise.wav")

#     # boost volume by 6dB
#     louder_song = song + 6

#     # reduce volume by 3dB
#     quieter_song = song - 1000

#     #Play song
#     play(louder_song)

#     #save louder song 
#     quieter_song.export("louder_song.wav", format='wav')

# def overlay_noise(main_file,noise):
#     audio_superimposed = main_file.overlay(noise,loop=TRUE)
#     audio_superimposed.export("audio_superimposed.wav", format='wav')

def loading_audio(audio_file):
    audio = AudioSegment.from_wav(audio_file)
    audio = audio.set_frame_rate(7000)
    audio = audio.set_channels(1)
    return audio

# def playback_speed(audio_file,speed):
#     # main_file = AudioSegment.from_mp3("Banking Terminology.wav")
#     speed_1=audio_file.speedup(playback_speed=speed)
#     return speed_1,speed

def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })

    # convert the sound with altered frame rate to a standard frame rate
    # so that regular playback programs will work right. They often only
    # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

   
def audio_level(audio_file,audio_level):
    # main_file = AudioSegment.from_wav(audio_file)
    loudness_changed = audio_file + audio_level
    # loudness_changed.export(audio_file+ " " +str(audio_level) + ".wav", format='wav')
    return loudness_changed

def sampling_rate_correction(audio_file,audio_name,audio_Level,noise_level,playback_speed,output_folder):
    # main_file = AudioSegment.from_wav(audio_file)
    
    sampling_rate = audio_file.set_frame_rate(8000)
    sampling_rate = sampling_rate.set_channels(1)
    sampling_rate.export(output_folder+"_"+ str(audio_Level) + "_" +str(noise_level)+"_"+str(playback_speed)+audio_name, format='wav')
    # print("enhacements_undergoing")
    return sampling_rate
def overlay_noise(audio_file,noise_file):
    # main_file = AudioSegment.from_mp3(audio_file)
    # noise = AudioSegment.from_mp3("vehicle_noise.wav")
    audio_superimposed = audio_file.overlay(noise_file,loop=True)
    return audio_superimposed
    # audio_superimposed.export(audio_file+" noise_superimposed.wav", format='wav')

def final_function(audio_file,noise_file,output_folder):
    try:
    
        # sampling_rate_correction()
        # audio_level()
        # playback_speed()
        # noise=loading_audio(noise_file)
        # overlay_noise()
        file_name=os.path.basename(audio_file)
        main_file=loading_audio(audio_file)
        noise_file=loading_audio(noise_file)

        audio_levels = [-5,0,10]
        noise_levels = [-10,0,5]
        playback_speeds = [0.95,0,1.1]

        for i in audio_levels:
            level_edited_file=audio_level(main_file,i)#main file with changed db level
            for j in noise_levels:
                if(j!=0):#for noise=0 we are having no noise
                    edited_noise_file=audio_level(noise_file,j)#noise file with changed noise level
                    # edited_noise_file.export('/media/edl-90/WD Elements/Vibhav/Office work/practice/1.wav',format='wav')
                    # print(1)
                    
                else:
                    # print(2)
                    edited_noise_file=0


                for k in playback_speeds:
                    if(k!=0):
                        # print(3)
                        speed_edited_file=speed_change(level_edited_file,k)#speed changed of db changed file
                        # speed_edited_file.export('/media/edl-90/WD Elements/Vibhav/Office work/practice/3.wav',format='wav')
                    else:
                        # print(4)

                        speed_edited_file=level_edited_file#speed change is zero
                    
                    #for taking care of case where there is no noise file
                    if(edited_noise_file!=0):
                        superimposed_noise_file = overlay_noise(speed_edited_file,edited_noise_file)
                        # superimposed_noise_file.export('/media/edl-90/WD Elements/Vibhav/Office work/practice/5.wav',format='wav')
                        # print(5)
                    else:
                        # print(6)
                        superimposed_noise_file = speed_edited_file
                    # print(7)
                    sampling_rate_correction(superimposed_noise_file,file_name,i,j,k,output_folder)#audio_file,audio_name,audio_level,noise_level,playback_speed
                    
    except Exception as e:
        print(e)

# if __name__=="__main__":
    # noise=loading_audio("noise_1.wav")
    # main_file=loading_audio("playback_slow.wav")
    # main_file1=audio_level(main_file,-10)
    # noise_overlayed=overlay_noise(main_file1,0)
    # sampling_rate_correction(noise_overlayed)
    


    # slow_sound = speed_change(main_file, 0.95)
    # fast_sound = speed_change(main_file, 1.1)
    # main_file1=playback_speed(main_file,0.9)
    # ff=overlay_noise(main_file1[0],noise1[0])
    # slow_sound.export("playback_slow.wav", format='wav')
    # fast_sound.export("playback_fast.wav", format='wav')


    # main_file=loading_audio("/media/edl-90/WD Elements/Vibhav/Office work/practice/online complaint.wav")
    # noise_file=loading_audio("/media/edl-90/WD Elements/Vibhav/Office work/practice/noise_1.wav")

    # level_edited_file=audio_level(main_file,10)
    # edited_noise_file=audio_level(noise_file,10)
    # print
    # speed_edited_file=speed_change(level_edited_file,1.1)
    # superimposed_noise_file = overlay_noise(speed_edited_file,edited_noise_file)
    # superimposed_noise_file.export('/media/edl-90/WD Elements/Vibhav/Office work/practice/abc.wav',format='wav')
    # print(type(superimposed_noise_file))
    # abc=sampling_rate_correction(superimposed_noise_file,"/media/edl-90/WD Elements/Vibhav/Office work/practice/online complaint.wav",10,10,1.1)
    # print(type(abc))
    
    
    
    # final_function("/media/edl-90/WD Elements/Vibhav/Office work/practice/diff files/second/Fraud call to sbi bank manager about atm verification.wav","/media/edl-90/WD Elements/Vibhav/Office work/practice/diff files/second/noise_1.wav")


