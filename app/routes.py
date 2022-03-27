from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'omar'}
	return '''
<html>
	<head>
		<title>Microblog</title>
	</head>
	<body>
		<h1>Hi, ''' +  user['username'] + ''' </h1>
	</body>
</html>
'''

