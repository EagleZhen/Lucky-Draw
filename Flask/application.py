# This Python file uses the following encoding: utf-8
from flask import Flask, render_template, request
from random import randrange

app = Flask(__name__,template_folder="./")

data = "6A01 陳靖朗|6A02 鍾浩程|6A03 何晉希|6A04 簡捷|6A05 郭加智|6A06 林芷穎|6A07 李樂軒|6A08 梁樂怡|6A09 廖珮婷|6A10 盧雪藍|6A11 布欣霖|6A12 潘朗|6A13 邵如雪|6A14 冼懷哲|6A15 黃卓盈|6A16 黃俊傑|6A17 王熙晴|6A18 黃昊光|6A19 王子軒|6A20 黃楹雅|6A21 姚樂儀|6B01 陳樂齡|6B02 陳上恩|6B03 陳奕文|6B04 陳鴻興|6B05 鄭景丰|6B06 鄭惜之|6B07 莊子樂|6B08 朱晴|6B09 金穎彤|6B10 黎芷晴|6B11 劉心弦|6B12 梁凱傑|6B13 馬梓馨|6B14 柯映而|6B15 彭花茶|6B16 史俊希|6B17 謝朗晴|6B18 徐晞妤|6B19 尹靖嵐|6B20 黃婕妤|6B21 黃子晴|6B22 黃梓銓|6B23 黃欣陶|6B24 王欣同|6B25 楊靖堯|6B26 楊善如|6B27 余蔚藍|6C01 區梓雋|6C02 張浚謙|6C03 張蕙然|6C04 張詠暘|6C05 韓穎|6C06 何紫琪|6C07 何勇琦|6C08 紀智琛|6C09 郭楠|6C10 黎穎忻|6C11 林嘉軒|6C12 李家悅|6C13 梁靖欣|6C14 呂紀瑩|6C15 馬崑庭|6C16 吳梓銘|6C17 龐智軒|6C18 潘在恩|6C19 蘇洛弘|6C20 蘇恩霖|6C21 王苑琳|6C22 王秉洋|6C23 楊海寧|6D01 陳明真|6D02 陳星朗|6D03 陳日楠|6D04 陳琬晴|6D05 陳悅|6D06 張卓熙|6D07 趙紳寶|6D08 鄧燊|6D09 何彥璁|6D10 羅康晴|6D11 李俊毅|6D12 李俊煒|6D13 李珈汶|6D14 連韋澄|6D15 呂易衡|6D16 柯欣然|6D17 潘曉晴|6D18 施玉兒|6D19 單學賢|6D20 黃樂賢|6D21 鄔迦悅|6D22 楊樂琛|6D23 楊嘉琪|6D24 楊詩慧|6D25 葉皓泓|6E01 陳可桐|6E02 陳煥翹|6E03 鄭芷晴|6E04 張靄祺|6E05 植家祺|6E06 蔡卓霖|6E07 丁天瑞|6E08 范日稀|6E09 何冠聰|6E10 許綽允|6E11 葉澄|6E12 金靖晞|6E13 金大衛|6E14 金己靖|6E15 高楚翹|6E16 顧芊瀛|6E17 關頌曦|6E18 林栢穎|6E19 劉浩霖|6E20 劉覺恩|6E21 羅卓希|6E22 李德嵐|6E23 梁步禮|6E24 梁梓彥|6E25 李歷安|6E26 吳仲翹|6E27 潘煦朗|6E28 譚曉晴|6E29 王鈺錕|6E30 黃俊健|6E31 黃亭嘉|6E32 袁浩軒|6F01 岑杏琳|6F02 翟凱澄|6F03 陳嘉禮|6F04 陳柏嘉|6F05 陳曉約|6F06 陳有駿|6F07 鄭思律|6F08 張文彥|6F09 焦采溢|6F10 鍾恩信|6F11 樊子晞|6F12 符哲滔|6F13 胡穎琪|6F14 郭芊璇|6F15 林正童|6F16 林日東|6F17 劉詠茵|6F18 李傑正|6F19 梁家朗|6F20 倫芷悠|6F21 龍瑞希|6F22 羅安琪|6F23 馬樂茵|6F24 馬肇煒|6F25 吳哲朗|6F26 唐鄯恆|6F27 王俊稀|6F28 黃諾謙|6F29 黃瑞豐|6F30 黃迪|6F31 黃梓謙|6F32 姚涵瑛|6F33 楊汶璁|6F34 楊文曦|6F35 甄梓濠|6G01 林名軒|6G02 趙浩明|6G03 錢泓熙|6G04 林渭潼|6G05 吳卓熙|6G06 張子蕎|6G07 余俊彥|6G08 汪夏禾|6G09 何旨悠|6G10 謝天詠"
info_list = data.split("|")

@app.route("/")
def main():
	# name = request.args.get("name", "world")

	#build the name labels
	codes=""
	for cnt,info in enumerate(info_list):
		class_id = "rounded_box_green"
		label_id = cnt
		content = info

		codes+=f"<label class=\"{class_id}\" id=\"{label_id}\">{content}</label>\n"

	#select the lucky number
	selected_id = randrange(0,cnt)

	#render the webpage
	return render_template("index.html", labels=codes, total_number = cnt+1, lucky_dog = selected_id)

if __name__ == '__main__':
    app.run(debug=True)