from flask import Flask, render_template, request
from random import randrange

app = Flask(__name__,template_folder="./")

@app.route("/")
def yo():
	# name = request.args.get("name", "world")

	total_no_of_students = 6*35
	lucky_dog = randrange(1,total_no_of_students)

	name_list=""
	for class_no in range (65,65+6):
		for id in range (1,35):
			if ((class_no-65)*35+id==lucky_dog):
				name_list += f"<label id=\"rounded_box_green_selected\">6{chr(class_no)}&nbsp{str(id).zfill(2)}</label>\n"
			else:
				name_list += f"<label id=\"rounded_box_green\">6{chr(class_no)}&nbsp{str(id).zfill(2)}</label>\n"

	return render_template("index.html", name_box=name_list)

if __name__ == '__main__':
    app.run(debug=True)