from pydub import AudioSegment
from pydub.silence import detect_silence
from pydub.playback import play
from pydub.utils import db_to_float
import os

def finding_silent_second(audio_segment,min_silence_len=200,silence_thresh=-16,seek_step=1):
    seg_len = len(audio_segment)

    # you can't have a silent portion of a sound that is longer than the sound
    if seg_len < min_silence_len:
        return []

    # convert silence threshold to a float value (so we can compare it to rms)
    silence_thresh = db_to_float(silence_thresh) * audio_segment.max_possible_amplitude

    # find silence and add start and end indicies to the to_cut list
    silence_starts = []

    # check successive (1 sec by default) chunk of sound for silence
    # try a chunk at every "seek step" (or every chunk for a seek step == 1)
    last_slice_start = seg_len - min_silence_len
    slice_starts = range(0, last_slice_start + 1, seek_step)

    # guarantee last_slice_start is included in the range
    # to make sure the last portion of the audio is searched
    if last_slice_start % seek_step:
        slice_starts = itertools.chain(slice_starts, [last_slice_start])

    for i in slice_starts:
        audio_slice = audio_segment[i:i + min_silence_len]
        if audio_slice.rms <= silence_thresh:
            return(i)
            # silence_starts.append(i)
            # return(silence_starts)

def silence_second_bw_8_12_secs_chunks(audio_segment,split_files_location):
    file_name=os.path.basename(audio_segment)
    audio_segment=AudioSegment.from_file(audio_segment)
    
    initial=0
    split_second=0
    last_chopped_second=0
    chunks=[]
    k=0
    l=len(audio_segment)
    
    for a in range(1,l):
        if(last_chopped_second+8>l):
            chunks.append(audio_segment[last_chopped_second:])
            break
        else:
            test1 = audio_segment[last_chopped_second + 8000:]
            split_second = finding_silent_second(test1,200,-16,1)
            if(split_second==[]):
                chunks.append(audio_segment[initial:])
                break
            print('a')
            print(split_second)
            print(initial)
            print(last_chopped_second)
            print('b')
            

            chunks.append(audio_segment[initial:last_chopped_second+8000+split_second])
            initial=last_chopped_second+8000+split_second
            last_chopped_second=last_chopped_second+8000+split_second
            
            print(k)
            k+=1
    print("chunks done")
    length_split=0        
    for i, chunk in enumerate(chunks):
        print("Exporting c{0}.wav.".format(i))
        print(split_files_location,file_name)
        chunk.export(
            split_files_location+"/"+file_name[:-4]+"c{}.wav".format(i),
            bitrate = "192k",
            format = "wav"
        )
        length_split=length_split+len(chunk)
    print(length_split,l)
    print("splitting_done")
        


# silence_second_bw_8_12_secs_chunks("/media/edl-90/WD Elements/Vibhav/Office work/practice/audio/youtube_downloaded/Open Savings Bank Account in Just 5 Minutes _ Kotak 811 Explained in Hindi _ Techno Whizz 🙂-BXV_d7PK8gE.wav")

# file_name=["/media/edl-90/WD Elements/Vibhav/Office work/practice/audio/youtube_downloaded/What is UPI  Unified Payment Interface _ Paytm Wallet को अब भूल जाओ _ Must Watch_ Modi's Idea-RU8EvlhfNg4.wav",
# "/media/edl-90/WD Elements/Vibhav/Office work/practice/audio/youtube_downloaded/Open Savings Bank Account in Just 5 Minutes _ Kotak 811 Explained in Hindi _ Techno Whizz 🙂-BXV_d7PK8gE.wav","/media/edl-90/WD Elements/Vibhav/Office work/practice/audio/How to online complaint in state bank of india (hindi).wav"]

