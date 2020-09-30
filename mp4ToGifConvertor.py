#mp4 to gif convertor
import imageio,os
from tqdm.auto import tqdm

print("Welcome to the Mp4 to Gif Convertor")
def gifConvertor(inputPath):
    targetFormat=".gif"
    outputPath=os.path.splitext(inputPath)[0]+targetFormat
    print(f'Converting {inputPath} to {outputPath}')
    reader=imageio.get_reader(inputPath)
    fps=reader.get_meta_data()['fps']
    writer=imageio.get_writer(outputPath,fps=fps)
    for frames in tqdm(reader,desc="Converting: "):
        writer.append_data(frames)
        #print(f'Frames{frames}')
    print("\n Conversion Completed!")
    writer.close()

pathOfClip = input("\n Enter the path of the clip: ")
clip=os.path.abspath('pathOfClip')
gifConvertor(pathOfClip)
