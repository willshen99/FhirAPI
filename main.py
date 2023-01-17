from flask import Flask, request, abort
from flask_restful import Resource, Api
from fhir.resources.humanname import HumanName

app = Flask(__name__)
api = Api(app)



@app.route('/humanname', methods=['GET'])
def humanname_api():
    # convert request arg to dictionary
    query = request.args.to_dict(flat=False)
    # conver card. == 0..1 fields to a non-list
    card1_field = ['use', 'text', 'family', 'period']
    # for card 1 fields, validate input value numbers and tranform to non-iterable object
    for field in card1_field:
        # continue if field not passed in
        if field not in query:
            continue
        # raise error if multiple values are passed in
        if len(query[field]) > 1:
            abort(400)
        # convert to non-iterable item
        query[field] = query[field][0]
    return HumanName.parse_obj(query).json()

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=5000)

