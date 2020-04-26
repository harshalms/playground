# import the necessary packages
from skimage.measure import compare_ssim
# from skimage.metrics._structural_similarity import compare_ssim
import argparse
import imutils
import cv2
import os
# construct the argument parse and parse the arguments
'''
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="first input image")
ap.add_argument("-s", "--second", required=True, help="second")
args = vars(ap.parse_args())
'''
# Give folder path input files and output files (with white background)
input_folder = os.listdir('/home/user/playground/input')
print('Input Folder items:', len(input_folder))
input_path = '/home/user/playground/input/'
input_dict = {}
for img in input_folder:
    name = img.split('.')
    input_dict[name[0]] = img
output_folder = os.listdir('/home/user/playground/output/')
print('Output Folder items:', len(output_folder))
output_path = '/home/user/playground/output/'
dataset = []
# Getting the image file path and ita mask path and 
# creating a dictionary of corp, image and mask keywords 
for i in output_folder:
  mask_path = os.path.abspath(output_path+ i)
  j = i.split('.')
#   k = j[0] + '_mask.mat'
  image_path = os.path.abspath(input_path + input_dict[j[0]])
  dataset.append({"img":image_path, "mask":mask_path})
print('Length of Dataset:', len(dataset))

# load the two input images
count = 0
for i in range(len(dataset)):
	imageA = cv2.imread(dataset[i]["img"])
	imageB = cv2.imread(dataset[i]["mask"])
	# convert the images to grayscale
	grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
	grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

	# compute the Structural Similarity Index (SSIM) between the two
	# images, ensuring that the difference image is returned
	(score, diff) = compare_ssim(grayA, grayB, full=True)
	diff = (diff * 255).astype("uint8")
	# print("SSIM: {}".format(score))

	# threshold the difference image, followed by finding contours to
	# obtain the regions of the two input images that differ
	thresh = cv2.threshold(diff, 0, 255,
		cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)

	# loop over the contours
	for c in cnts:
		# compute the bounding box of the contour and then draw the
		# bounding box on both input images to represent where the two
		# images differ
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
		cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
	# show the output images
	# cv2.imshow("Original", imageA)
	# cv2.imshow("Modified", imageB)
	# cv2.imshow("Diff", diff)
	gen_mask_folder_path = '/home/user/playground/'
	name_split = dataset[i]['img'].split('/')
	k = name_split[-1].split('.')
	gen_mask_name = k[0]+'.png'
	gen_mask_path = gen_mask_folder_path + gen_mask_name
	cv2.imwrite(gen_mask_path, diff)
	count+=1
	if count%50 == 0:
		print('{} images are written...'.format(count))
	# cv2.imshow("Thresh", thresh)
	# cv2.waitKey(0)
print('{} images are written successfully.'.format(count))
