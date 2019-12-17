# 创建一个Hello类，拥有属性say_hello
class Hello(object):
    def say_hello(self, name='gregory'):
        print( 'Hello, %s.'% name)
print (type(Hello))
# 从Hello类创建一个实例hello
hello =Hello()
# 使用hello调用方法say_hello
hello.say_hello()

def func(self, name='meta'):
    # 创建函数func
    print('Hi, %s.'% name)
Hi= type('Hi', (object,), dict(say_hello=func)) # Hi:类名 (object,):基类 dict(say_hello=func):类的成员


# 通过type创建Hi class
hello=Hi()
hello.say_hello()
print (type(Hello), type(hello))

print ('-------------------------')

class SayMetaClass(type):
    #元类是由“type”衍生而出，所以父类需要传入type。
    def __new__(cls, name, bases, attrs):
        #元类的操作都在 __new__中完成，它的第一个参数是将创建的类，之后的参数即是三大永恒命题：类名，基类，类的成员。

        attrs['say_'+ name] =lambda self, value, saying=name:print(saying + ','+ value +'!')
        #创造属性和方法，由元类创建的类叫“Hello”，那创建时就自动有了一个叫“say_Hello”的类方法
        # 然后又将类的名字“Hello”作为默认参数saying，传到了方法里面。
        # 然后把hello方法调用时的传参作为value传进去，最终打印出来。

        return type.__new__(cls, name, bases, attrs)
        #传承类名，父类，属性

class Hello(object, metaclass =SayMetaClass):
    # 创建类，通过元类创建的类，第一个参数是父类，第二个参数是metaclass
    pass

hello =Hello()# 创建实列
hello.say_Hello(value='gregory',saying='111')# 调用实例方法

class Nihao(object,metaclass=SayMetaClass):
    pass

nihao=Nihao()
nihao.say_Nihao("greg 李")





print ('-------------------------')


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>'% (self.__class__.__name__,self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):
    def __init__(self , name):
        super(IntegerField,self).__init__(name,'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kwarg):
        super(Model, self).__init__(**kwarg)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    # 模拟建表操作
    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join([str(i) for i in args]))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

print (User.__dict__)

u = User(id=12345, name='Gregory', email='292409083@qq.com', password='iamgreg',w=5)
# u.save()

# class A():
#     a = 1
#     b = {"cc":3}
#
# print (A.__dict__)