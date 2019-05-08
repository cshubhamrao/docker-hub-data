import json

from pandas.io.json import json_normalize


def preprocess(file_name):
    with open(file_name) as f:
        d = json.load(f)
    data = json_normalize(d['summaries'])

    get_names = lambda x: [i['name'] for i in x if i['name'] is not ""] if len(x) else []
    data['architectures'] = data['architectures'].map(get_names)
    data['architectures'] = data['architectures'].apply(sorted)
    data['num_archs'] = data['architectures'].map(len)

    data['architectures'] = data['architectures'].map(lambda x: ", ".join(x))
    data = data.drop(['certification_status', 'id',
                      'filter_type', 'logo_url.large',
                      'logo_url.small', 'popularity',
                      'publisher.id', 'name', 'publisher.name', 'type'], axis=1)
    labels_as_list = lambda x: ", ".join(i['label'] for i in x if i['label'] is not "") if \
        len(x) else None
    data['operating_systems'] = data['operating_systems'].map(labels_as_list)

    # def to_numbers(x):
    #     no_plus = str(x)[:-1] if "+" in str(x) else x
    #     print(no_plus)
    #     print(x)
    #     no_plus = no_plus.strip()
    #     number, suffix = float(no_plus[:-1]), no_plus[-1]
    #
    #     if suffix is "K":
    #         return number * 1000
    #     elif suffix is "M":
    #         return number * 1000000
    #     else:
    #         return number
    # data['pull_count'] = data['pull_count'].map(to_numbers)
    data['pull_count'] = data['pull_count'].map(lambda x: str(x)[:-1] if "+" in str(x) else str(x))
    data['pull_count'] = data['pull_count'].map(
        lambda x: float(x[:-1]) * 1000 if x[-1] is "K" else\
        float(x[:-1]) * 1000000 if x[-1] is "M" else float(x))

    # data['categories_exists'] = data['categories'].map(lambda x: 1 if x else 0)
    data['category_count'] = data['categories'].map(lambda x: len(x) if x else 0)
    data = data.drop(['categories'], axis=1)
    data.set_index('slug')
    return data


if __name__ == '__main__':
    DATA_DIR = "../data/recent-data/"
    import os
    files = sorted(os.listdir(DATA_DIR), reverse=True)
    # for i in range(len(files) - 1):
    file_1 = os.path.join(DATA_DIR, files[0])
    file_2 = os.path.join(DATA_DIR, files[1])
    print(file_1, file_2)
    df1, df2 = preprocess(file_1), preprocess(file_2)


