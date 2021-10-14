import os


def image_list(image_list):
   image_list = open(image_list, "r")
   content_list = image_list.readlines()
   return content_list

def fileNameOnly(item):
    print("1 " + item)
    temp = os.path.basename(item)
    print("2 " + temp)
    strip = os.path.splitext(temp)[0]
    print("3 " + strip)
    return strip

with open('full_image_list.txt') as f:
    total_mrc_files = f.read().splitlines()
with open('converted_tiff_files.txt') as f:
    done_tiffs = f.read().splitlines()

#total_mrc_files = image_list("full_image_list.txt")
#done_tiffs = image_list("converted_tiff_files.txt")
unconverted_mrc_list = []

for mrc in total_mrc_files:
    for tiff in done_tiffs:
        if fileNameOnly(mrc) == fileNameOnly(tiff):
            unconverted = ""
            break
        else:
            unconverted = mrc
    if unconverted != "":
        unconverted_mrc_list.append(unconverted)

#print(unconverted_mrc_list)
#print(len(unconverted_mrc_list))

output_image_list_file = open("unconverted_mrc_list.txt", "w")
for image in unconverted_mrc_list:
    output_image_list_file.write(image + "\n")
output_image_list_file.close()
