import inspect

def create_instance(info):
    instance_id = info
    return instance_id


def create_instance_d(course_id):
    return None


def create_section(info):
    section_id = info
    return section_id


def create_section_d(course_id):
    return None


def create_chapter(info):
    chapter_id = info
    return chapter_id


def create_chapter_d(course_id):
    return None


def create_leaf(info):
    leaf_id = info
    return leaf_id


def create_leaf_d(leaf_id):
    return None


def create_course(info):
    course_id = info
    return course_id


def create_course_d(course_id):
    return None


def create_classroom(info):
    classroom_id = info
    return classroom_id


def create_classroom_d(course_id):
    return None

#print create_classroom_d.__name__

#print inspect.getargspec(create_classroom_d)

#print create_leaf.__code__.co_varnames