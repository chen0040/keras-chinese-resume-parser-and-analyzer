import re


def extract_email(s, line):
    email = None
    match = re.search(r'[\w\.-]+@[\w\.-]+', line)
    if match is not None:
        email = match.group(0)
    return email


def extract_sex(s, line):
    parts = line.split(' ')
    sex_found = False
    sex = None
    for w in parts:
        if '性别' in w:
            sex_found = True
            continue
        if sex_found and ':' not in w:
            if w == '男':
                sex = 'male'
            else:
                sex = 'female'
            break
    return sex


def extract_education(s, line):
    parts = line.split(' ')
    found = False
    education = None
    for w in parts:
        if '学历' in w:
            found = True
            continue
        if found and ':' not in w:
            education = w
            break
    return education


def extract_mobile(s, line):
    parts = line.split(' ')
    found = False
    education = None
    for w in parts:
        if '手机' in w:
            found = True
            continue
        if found and ':' not in w:
            education = w
            break
    return education


def extract_experience(s, line):
    parts = line.split(' ')
    found = False
    result = None
    for w in parts:
        if w.find('工作经验') != -1:
            found = True
            continue
        if found and ':' not in w:
            result = w
            break
    return result


def extract_expertise(s, line):
    length = 4
    index = line.find('熟练掌握')
    if index == -1:
        length = 2
        index = line.find('熟悉')
    if index == -1:
        length = 2
        index = line.find('使用')
    if index == -1:
        length = 2
        index = line.find('掌握')
    if index == -1:
        length = 4
        index = line.find('开发环境')
    if index == -1:
        length = 4
        index = line.find('开发工具')

    result = None
    if index == -1:
        return None
    else:
        result = line[index + length:].replace(':', '').strip()
        if result == '':
            return None
    return result


def extract_ethnicity(s, line):
    parts = line.split(' ')
    race_found = False
    race = None
    for w in parts:
        if w.find('民族') != -1:
            race_found = True
            continue
        if race_found and w.find(':') == -1:
            race = w
            break
    return race


def extract_name(s, line):
    name = None
    for w in s.words:
        word = w.strip()
        if word == '姓名':
            name = ''
        elif name is not None:
            if len(name) + len(word) > 4:
                break
            else:
                name += word
        if name is not None and len(name) >= 4:
            break
    return name


def extract_objective(s, line):
    parts = line.split(' ')
    found = False
    result = None
    for w in parts:
        if w.find('求职意向') != -1:
            found = True
            continue
        if found and ':' not in w:
            result = w
            break
    return result
