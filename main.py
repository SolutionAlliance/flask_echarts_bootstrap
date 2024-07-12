from flask import Flask, jsonify, request,render_template

app = Flask(__name__,static_folder='image')

# 模拟数据库中的省份和城市数据
provinces = [
    {"id": 1, "name": "河北", "simpleName": "冀", "proCap": "石家庄"},
    {"id": 2, "name": "北京", "simpleName": "京", "proCap": "北京"},
    # 可以添加更多省份
]

cities = {
    1: [
        {"cityId": 1, "cityName": "石家庄"},
        {"cityId": 2, "cityName": "唐山"},
        # 河北省的其他城市
    ],
    2: [
        {"cityId": 3, "cityName": "北京市"},
        # 北京的其他城市
    ],
    # 可以添加更多省份对应的城市
}
# 模拟数据库中的公司数据
companies = {
    1: [
        {"companyId": 1, "companyName": "石家庄公司A"},
        {"companyId": 2, "companyName": "石家庄公司B"},
        # 石家庄的其他公司
    ],
    2: [
        {"companyId": 3, "companyName": "唐山公司A"},
        # 唐山的其他公司
    ],
    3: [
        {"companyId": 4, "companyName": "北京公司A"},
        {"companyId": 5, "companyName": "北京公司B"},
        # 北京的其他公司
    ],
    # 可以添加更多城市对应的公司
}

@app.route(rule="/", methods=["get"])
def index():
    return render_template('dome.html')

@app.route(rule="/tree", methods=["get"])
def tree():
    return render_template('index.html')

@app.route('/findAllProList', methods=['GET'])
def find_all_pro_list():
    return jsonify(provinces)

@app.route('/findAllCityList', methods=['GET'])
def find_all_city_list():
    pro_id = int(request.args.get('proId'))
    return jsonify(cities.get(pro_id, []))

@app.route('/findCompanies', methods=['GET'])
def find_companies():
    city_id = int(request.args.get('cityId'))
    return jsonify(companies.get(city_id, []))

if __name__ == '__main__':
    app.run(debug=True)
