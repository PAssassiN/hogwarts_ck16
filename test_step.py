import pytest
import yaml


def step1():
    print("step1打开浏览器")


def step2():
    print("step2注册新账号")


def step3():
    print("step3登录新账号")


# 解析测试步骤文件
def steps(path):
    with open(path) as f:
        steps = yaml.safe_load(f)
    for step in steps:
        if "step1" in step:
            step1()
        elif "step2" in step:
            step2()
        elif "step3" in step:
            step3()


def test_foo():
    steps("./step.yml")
