import termcolor
import colorama
import requests

WIDTH=80
DEEP=-225
LOWER_RED_LINE=-213
UPPER_RED_LINE=-209
HEIGHT=-200
URL='http://kineret.org.il/miflasim/'
BORDER_SYNBOL = '.'

def red_line(height,background):
	print(BORDER_SYNBOL,end='')
	bold = "\033[1m"
	reset = "\033[0;0m"
	for print_num in range(WIDTH):
		termcolor.cprint(bold+'-', 'red',background,end='')
	print(BORDER_SYNBOL,end='')
	print(height)

def normal_line(height,background):
	print(BORDER_SYNBOL,end='')
	for print_num in range(WIDTH):
		termcolor.cprint(' ', None,background,end='')
	print(height)
	
def get_kineret_height():
	left_token ='<span class=\"hp_miflas_height\">'
	right_token = '</span></div><div id=\"hp_miflas_info\">'
	try:
		response = requests.get(URL)
	except Exception as e:
		print("no internet!!")
		exit()
	html = response.text
	return float(html.split(left_token)[1].split(right_token)[0])

def get_background_color(kineret_height, height):
	if height<=kineret_height:
		return 'on_blue'
	else:
		return None

def is_red_line(height):
	return height == LOWER_RED_LINE or height == UPPER_RED_LINE
	
def is_it_miflas(kineret_height,height):
	return 0<=kineret_height - height <= 1

def main():
	colorama.init()
	kineret_height = get_kineret_height()
	for line_to_print in range(HEIGHT, DEEP, -1):
		background_color = get_background_color(kineret_height,line_to_print)
		height = BORDER_SYNBOL		
		if is_red_line(line_to_print):
			red_line(line_to_print,background_color)
			continue
		elif is_it_miflas(kineret_height,line_to_print):
			height = height+str(kineret_height)
		normal_line(height,background_color)
		
	
	
if __name__ == "__main__":
	main()