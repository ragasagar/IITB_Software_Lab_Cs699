import json


def produceresult(data, age_grp):
    """
    Process the data given and create a desired dict result

    :param data: input json content
    :type data: dict
    :param age_grp: age_grp value which is needed to process the data
    :type age_grp: str

    :return: processed dict object
    :rtype: dict
    """
    result = {}
    mcount = 0
    mbalance = 0
    fcount = 0
    fbalance = 0
    tid_name = {}
    for df in data:
        tid_name[df["tid"]] = df["name"]
        balance = float(df['balance'][1:])
        if df['gender'] == "female":
            fcount += 1
            fbalance += balance
        else:
            mcount += 1
            mbalance += balance
    result['age_grp'] = age_grp
    result['tid_name'] = tid_name
    result['mcount'] = mcount
    result['mbalance'] = mbalance
    result['fcount'] = fcount
    result['fbalance'] = fbalance
    return result


def processData(input_path, output_path):
    """
    Groups data based on the age field in the json file and store the output
    again as a .json file. Output json file will contain an array of 2 json objects.
    Only those records are considered whose isActive field is true .

    :param  input_path: input json file path
    :type input_path: str
    :param  output_path: output json file path
    :type output_path: str
    """
    print(input_path)
    data = []

    with open(input_path) as file:
        data = json.load(file)
    data = list(filter(lambda x: x['isActive'] is True, data))
    age2130 = list(filter(lambda x: x['age'] >= 21 and x['age'] <= 30, data))
    age3140 = list(filter(lambda x: x['age'] >= 31 and x['age'] <= 40, data))
    output = [produceresult(age2130, "21-30"), produceresult(age3140, "31-40")]
    with open(output_path, 'w') as file:
        json.dump(output, file, indent=4)

    print(output_path)


if __name__ == "__main__":
    '''
        Remove this comment.
        This is just for you to run and check your code.

        To test your function we will import this file and call your function.
        Before running give appropriate file path for path_to_input_json below. 
    # '''
    # path_to_input_json = './testcases/q6/q6_input.json'
    # path_to_output_json = './testcases/q6/q6_output.json'
    # processData(path_to_input_json, path_to_output_json)
