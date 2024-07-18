from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def fetch_data():
	url = 'http://169.254.169.254/opc/v2/instance/hostname'
	headers = {'Authorization': 'Bearer Oracle'}
	response=requests.get(url,headers=headers)
	if response.status_code==200:
		return response.text
	else:
		return f'Failed to fetch data: {response.status_code}'
if __name__ == '__main__':
	app.run(debug=True)
