from flask import render_template
from app import app
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', all_orders=orders)

@app.route('/orders/<order_str>')
def order_details(order_str):
    order_num = int(order_str)
    return render_template('order.html', all_orders=orders, order_num=order_num)

