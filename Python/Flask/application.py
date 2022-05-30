from flask import Flask, render_template, request

app = Flask(__name__,template_folder="./")

@app.route("/")
def yo():
	# 第一个是pass进去的variable，?name=
	# name = request.args.get("name", "world")

	name_list=""
	for class_no in range (65,65+6):
		for id in range (1,35):
			name_list += f"<label id=\"rounded_box_green\">6{chr(class_no)} {str(id).zfill(2)}</label>\n"
		name_list += "<br><br><br>"

	return render_template("index.html", name_box=name_list)

if __name__ == '__main__':
    app.run(debug=True)