import re

from snownlp import SnowNLP


class ResumeParser(object):

    def __init__(self):
        self.email = None
        self.name = None
        self.sex = None
        self.ethnicity = None
        self.education = None
        self.experience = None
        self.objective = None
        self.mobile = None
        self.expertise = []
        self.unknown = True
        self.raw = None

    def parse(self, texts, print_line=False):
        self.raw = texts
        for p in texts:
            if len(p) > 10:
                s = SnowNLP(p)
                unknown = True
                name = self.extract_name(s, p)
                email = self.extract_email(s, p)
                sex = self.extract_sex(s, p)
                race = self.extract_ethnicity(s, p)
                education = self.extract_education(s, p)
                experience = self.extract_experience(s, p)
                objective = self.extract_objective(s, p)
                expertise = self.extract_expertise(s, p)
                mobile = self.extract_mobile(s, p)
                if name is not None:
                    self.name = name
                    unknown = False
                if email is not None:
                    self.email = email
                    unknown = False
                if sex is not None:
                    self.sex = sex
                    unknown = False
                if race is not None:
                    self.ethnicity = race
                    unknown = False
                if education is not None:
                    self.education = education
                    unknown = False
                if experience is not None:
                    self.experience = experience
                    unknown = False
                if objective is not None:
                    self.objective = objective
                    unknown = False
                if expertise is not None:
                    self.expertise.append(expertise)
                    unknown = False
                if mobile is not None:
                    self.mobile = mobile
                    unknown = False

                if unknown is False:
                    self.unknown = unknown

                if print_line:
                    print('parsed: ', p)

    def extract_email(self, s, line):
        email = None
        match = re.search(r'[\w\.-]+@[\w\.-]+', line)
        if match is not None:
            email = match.group(0)
        return email

    def extract_sex(self, s, line):
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

    def extract_education(self, s, line):
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

    def extract_mobile(self, s, line):
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


    def extract_experience(self, s, line):
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

    def extract_expertise(self, s, line):
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

        if index == -1:
            return None
        else:
            return line[index+length:].replace(':', '')

    def extract_ethnicity(self, s, line):
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

    def extract_name(self, s, line):
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

    def extract_objective(self, s, line):
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

    def summary(self):
        text = ''
        if self.name is not None:
            text += 'name: {}\n'.format(self.name)
        if self.email is not None:
            text += 'email: {}\n'.format(self.email)
        if self.mobile is not None:
            text += 'mobile: {}\n'.format(self.mobile)
        if self.ethnicity is not None:
            text += 'ethnicity: {}\n'.format(self.ethnicity)
        if self.sex is not None:
            text += 'sex: {}\n'.format(self.sex)
        if self.education is not None:
            text += 'education: {}\n'.format(self.education)
        if self.experience is not None:
            text += 'experience: {}\n'.format(self.experience)
        if self.objective is not None:
            text += 'objective: {}\n'.format(self.objective)
        if len(self.expertise) > 0:
            for ex in self.expertise:
                text += 'expertise: {}\n'.format(ex)

        return text.strip()
