from flask import Flask, request, jsonify
from exec_eval import eval_exec_match

app = Flask(__name__)


@app.route('/evaluate', methods=['POST'])
def evaluate():
    # 从请求的 JSON 体中获取参数
    data = request.get_json()
    db = data.get('db')
    p_str = data.get('pred')
    g_str = data.get('gold')
    plug_value = data.get('plug_value', False)
    keep_distinct = data.get('keep_distinct', False)
    progress_bar_for_each_datapoint = data.get('progress_bar_for_each_datapoint', False)

    # 调用 evaluate 函数
    try:
        result = eval_exec_match(db=db, p_str=p_str, g_str=g_str, plug_value=plug_value,
                             keep_distinct=keep_distinct,
                             progress_bar_for_each_datapoint=progress_bar_for_each_datapoint)
    except Exception as e:
        print(e)
        return jsonify({'success': False})

    # 返回结果
    return jsonify({'success': result == 1})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')