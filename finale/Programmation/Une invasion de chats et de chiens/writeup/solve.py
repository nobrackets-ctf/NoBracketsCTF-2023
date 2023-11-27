from pwn import *

from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import base64
from io import BytesIO

r = remote("localhost", 1337)


processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")

for _ in range(500):
	raw_image = r.recvuntil(b"\n").decode()
	a = r.recvuntil(b"'dog'): ")
	
	image_base64 = base64.b64decode(raw_image)

	image = Image.open(BytesIO(image_base64))

	inputs = processor(images=image, return_tensors="pt")
	outputs = model(**inputs)

	# convert outputs (bounding boxes and class logits) to COCO API
	# let's only keep detections with score > 0.9
	target_sizes = torch.tensor([image.size[::-1]])
	results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

	for label in results["labels"]:
		g = model.config.id2label[label.item()]
		if g in ['cat', 'dog']:
			print(g)
			r.sendline(g.encode())
			break
	else:
		print("Error : cat")
		r.sendline(b"cat")
	  
	  
r.interactive()