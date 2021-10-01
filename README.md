# Multi Template Match - Process
- Multi-Template-Matching is the package used to match template images within any given input image
- Create list of template images for all objects that need to be detected
- Format to create a template - List of Tuples (Template label, RGB/grayscale template image in array format)
- Perform Multi-Template-Matching on input image against templates
- Visualize the detected objects in an image

# Face Matching - Process
- face_recognition is the package used to compare two faces present in two different images
- Get face encodings from both the input images (face_encodings)
- Compare the face encodings (compare_faces)
- Get euclidean distance between faces (face_distance)
- Multiply the distance by 100 and round it
- This gives the ‘percentage of variation’ between two face encodings
- Lesser the distance; Closer is the match between the faces



