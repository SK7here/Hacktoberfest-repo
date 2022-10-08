# Importing Packages
import base64
import face_recognition
import io
import numpy as np
import os
from PIL import Image

class FaceMatching:
	def match_face(self, known_image_base64_encoded, unknown_image_base64_encoded):
		result = []
		match_result = {}
		
		# Padding correction for known image
		if len(known_image_base64_encoded) % 4 != 0:  # check if multiple of 4
			while len(known_image_base64_encoded) % 4 != 0:
				known_image_base64_encoded = known_image_base64_encoded + "="
		else:
			pass

		# Base64 to Numpy array and creating face encoding for known image
		known_image_base64_decoded = base64.b64decode(known_image_base64_encoded)
		known_image = Image.open(io.BytesIO(known_image_base64_decoded))
		known_image_np = np.array(known_image)
		known_image_encoding = face_recognition.face_encodings(known_image_np)[0]

		# Padding correction for unknown image
		if len(unknown_image_base64_encoded) % 4 != 0:  # check if multiple of 4
			while len(unknown_image_base64_encoded) % 4 != 0:
				unknown_image_base64_encoded = unknown_image_base64_encoded + "="
		else:
			pass

		# Base64 to Numpy array and creating face encoding for unknown image
		unknown_image_base64_decoded = base64.b64decode(unknown_image_base64_encoded)
		unknown_image = Image.open(io.BytesIO(unknown_image_base64_decoded))
		unknown_image_np = np.array(unknown_image)
		unknown_image_encoding = face_recognition.face_encodings(unknown_image_np)[0]

		# Comparing known and unknown faces
		results = face_recognition.compare_faces([known_image_encoding], unknown_image_encoding)
		print(results)

		# Getting euclidean distance for calculating similarity between images
		distance_list = face_recognition.face_distance([known_image_encoding], unknown_image_encoding)
		distances = [str(distance) for distance in distance_list]
		distance = "".join(distances)
		distance = float(distance)
		distance = distance * 100
		distance = round(distance, 2)

		# Preparing results of face comparison
		if results[0] == True:
			match_result['match'] = True
			match_result['percentage_of_variation'] = distance
		else:
			match_result['match'] = False
			match_result['percentage_of_variation'] = distance

		result.append(match_result)

		return result


if __name__ == '__main__':
	obj = FaceMatching()
	result = obj.match_face(
		known_image_base64_encoded='//Give base64 encoded value for the image1'
		unknown_image_base64_encoded='//Give base64 encoded value for the image2')
	print(result)
