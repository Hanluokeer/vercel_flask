bbq_restaurant/
    └── templates/
        ├── index.html
        ├── menu.html
        ├── contact.html
    └── app.py
from flask import Flask, render_template

app = Flask(__name__)

# 餐厅信息
restaurant_info = {
    'name': '烧烤天堂',
    'address': '123 BBQ Street, BBQ City',
    'phone': '+1 (123) 456-7890',
}

# 菜单
menu_items = [
    {
        'name': '烤牛肉串',
        'description': '新鲜的牛肉串，烤到金黄色。',
        'price': '$10.99',
    },
    {
        'name': '烤羊肉串',
        'description': '香气四溢的羊肉串，配以秘制酱汁。',
        'price': '$12.99',
    },
    {
        'name': '烤鸡翅',
        'description': '酥脆多汁的烤鸡翅，吃了停不下来。',
        'price': '$8.99',
    },
]

@app.route('/')
def index():
    return render_template('index.html', restaurant_info=restaurant_info)

@app.route('/menu')
def menu():
    return render_template('menu.html', menu_items=menu_items)

@app.route('/contact')
def contact():
    return render_template('contact.html', restaurant_info=restaurant_info)

if __name__ == '__main__':
    app.run(debug=True)
<!DOCTYPE html>
<html>
<head>
    <title>{{ restaurant_info.name }}</title>
</head>
<body>
    <h1>欢迎来到{{ restaurant_info.name }}</h1>
    <p>地址：{{ restaurant_info.address }}</p>
    <p>电话：{{ restaurant_info.phone }}</p>
    <a href="{{ url_for('menu') }}">查看菜单</a>
    <a href="{{ url_for('contact') }}">联系我们</a>
</body>
</html>
<!DOCTYPE html>
<html>
<head>
    <title>联系我们</title>
</head>
<body>
    <h1>联系{{ restaurant_info.name }}</h1>
    <p>地址：{{ restaurant_info.address }}</p>
    <p>电话：{{ restaurant_info.phone }}</p>
    <a href="{{ url_for('index') }}">返回首页</a>
    <a href="{{ url_for('menu') }}">查看菜单</a>
</body>
</html>
python app.py

