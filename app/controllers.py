from app.samples.nlopt_examples import nlopt_examples
from flask import jsonify

def api_opt_get_example_list():
    a = nlopt_examples()
    result = a.get_all_examples()
    return jsonify(result)

def api_opt_run_official_example(optId):
    a = nlopt_examples()
    result = a.run_offcial_example()
    return jsonify(result)

def api_opt_run_longtime_example(optId):
    a = nlopt_examples()
    result = a.run_offcial_example()
    return jsonify(result)
#    result = api_run_official_example()
#    print(repr(result))

def api_opt_run_longtime_example_with_queue(optId):
    a = nlopt_examples()
    result = a.run_offcial_example()
    return jsonify(result)

def api_opt_run_example_with_continuous_response(optId):
    a = nlopt_examples()
    result = a.run_offcial_example()
    return jsonify(result)