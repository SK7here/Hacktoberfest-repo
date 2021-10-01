# Importing packages
import MTM
from MTM import matchTemplates, drawBoxesOnRGB
import cv2
import matplotlib.pyplot as plt
import os


# Load Template Images, convert them into gray scale and add to template list
listTemplate = []
image_folder = os.path.join('Images/shape_templates/multiple_shapes')
for filename in os.listdir(image_folder):
    template_img = cv2.imread(os.path.join(image_folder, filename))
    template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
    print((filename.split('.')[0], template_img))
    listTemplate.append((filename.split('.')[0], template_img))

# Load input image and convert to gray scale
input_img = cv2.imread('Images/input_image.jpg')
input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    

# Then call the function matchTemplates
Hits = matchTemplates(listTemplate, input_img, score_threshold=0.9,
                      method=cv2.TM_CCOEFF_NORMED, maxOverlap=0.1)

print("Found {} hits".format( len(Hits.index) ) )
print(Hits)

Overlay = drawBoxesOnRGB(input_img,
                         Hits,
                         showLabel = True,
                         labelColor=(255, 0, 0),
                         boxColor = (0, 0, 255),
                         labelScale=0.45,
                         boxThickness = 2)
plt.imshow(Overlay)
plt.show()
