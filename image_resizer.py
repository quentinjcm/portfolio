import os
from PIL import Image

BASE_PATH = "./images/sanctuary"
def main():
	for root, dirs, files in os.walk(BASE_PATH):
		for in_name in files:
			if in_name == ".DS_Store":
				continue
			in_path = os.path.join(root, in_name)
			out_name = in_name.split(".")
			out_name[0] += "_proxy"
			out_name = ".".join(out_name)
			out_path = os.path.join(root, out_name)

			print in_path
			with open(in_path, "r+b") as f:
				with Image.open(f) as im:
					height, width = im.size
					width /= 3.0
					height /= 3.0
					im.thumbnail((width, height), Image.ANTIALIAS)
					im.save(out_path, im.format)

main()
