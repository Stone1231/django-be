from django.test import TestCase, SimpleTestCase, TransactionTestCase
from unittest import skip
from .cust_models import *
# Create your tests here.
from django.db import transaction

class HelloTestCase(TestCase):
    def test_hello(self):
        s = "hello"
        self.assertEqual("hello", s)


class DeptTestCase(TestCase):
# class DeptTestCase(TransactionTestCase):
# class DeptTestCase(SimpleTestCase):
    def test_all(self):
        # datas = Dept.objects.filter(name="dept1")
        item:Dept = Dept()
        item.name = "dept_test"
        item.save()

        datas = Dept.objects.all()
        for item in datas:
            print(item.name)
            # item.name = item.name + "xx"
            # item.save()
            
        print(len(datas))

    # @skip
    # def test_insert2(self):
    #     try:
    #         Dept.objects.create(name="dept_test")
    #     except Exception as e:
    #         print(repr(e))

    # @skip
    def test_insert(self):
        try:
            item:Dept = Dept()
            item.name = "dept_test"
            item.save()
            print("item.save()")
        except Exception as e:
            print(repr(e))

    # @skip
    # def test_update(self):
    #     datas = Dept.objects.filter(name="dept_test")
    #     # datas = Dept.objects.all()
    #     print(len(datas))
    #     if len(datas) == 0:
    #         return
    #     item = datas[0]
    #     item.name = "dept_test2"
    #     item.save()

    # @skip
    # def test_del(self):
    #     datas = Dept.objects.filter(name="dept2")
    #     if len(datas) == 0:
    #         return
    #     item = datas[0]
    #     item.delete()    
