def test01():
    try:
        a=3/1
        print(a)
    except BaseException as e:
        print('出现异常:{}'.format(e))

    else:
        print('OK')
    finally:
        print('结束')
def test02():
    with 3/1 as a:
        print(a)

if __name__ == '__main__':
    #test01()
    test02()