#encording=utf-8
# request:https://www.liaoxuefeng.com/wiki/1016959663602400/1183249464292448
# json,jsonpath:https://www.jianshu.com/p/94ddacae5d55
# pymsql:https://blog.csdn.net/qq_40910788/article/details/84397026
# xlwt:https://segmentfault.com/a/1190000017866070
# snownlp:https://blog.csdn.net/google19890102/article/details/80091502


import requests
import jsonpath
import pymysql
import traceback
import re
import json
import xlwt
import snownlp

#mysql 信息
host = 'localhost'
username = 'root'
password = 'damilhc1987'
database = 'feedback_database'
#excel 地址
Path='/Users/ricelee/Desktop/Feedback.xls'


class feedbackclass (object):
    def __init__(self,ProjectID,startpage,endpage,db):
        self.ProjectID=ProjectID
        self.startpage=startpage
        self.endpage=endpage+1
        self.db=db
        #self.train_path=train_path

    def getfeedback_info(self):
        #请求到json数据

        feedback_json_all=[]
        finall_request_success_page = 0
        for page in range(self.startpage,self.endpage):
            self.url = "https://itunes.apple.com/rss/customerreviews/page={}/id={}/sortby=mostrecent/json?l=en&&cc=cn".format(
            page, self.ProjectID)
            print(self.url)

            try :
                b = requests.get(self.url)

                str_json =b.content.decode()
        #序列化json返回数据
                dic_json=json.loads(str_json)
        # 使用jsonpath 第三方库渠道entry下的数据
                feedback_json=jsonpath.jsonpath(dic_json,"$..entry")[0]
                #print(type(feedback_json))
                #print(len(jsonpath.jsonpath(dic_json,"$..entry")[0])) # 列表里只有1个元素
                feedback_json_all+=feedback_json#问题：.append()失败：TypeError: list indices must be integers or slices, not str
                #print(type(feedback_json_all))
                finall_request_success_page +=1
            except Exception as e:
                print("Request Url Err:{}".format(e))

        return feedback_json_all
    def save_feedback(self,path,feedback_json_all):
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.worksheet=self.workbook.add_sheet('Feedback')
        excel_title=['作者','版本','打分','评论id','标题','内容','标题情感分析','内容情感分析']
        for i in range(0,8):
            self.worksheet.write(0, i, label=excel_title[i])
        j = 1
        for i in feedback_json_all:
            #if i['id']['label']) 不存在
            self.worksheet.write(j, 0, label=i['author']['name']['label'])
            self.worksheet.write(j, 1, label=i['im:version']['label'])
    #print(i['im:rating']['label'])
            self.worksheet.write(j, 2, label=i['im:rating']['label'])
    #print(i['id']['label'])
            self.worksheet.write(j, 3, label=i['id']['label'])
    #print(i['title']['label'])
            self.worksheet.write(j, 4, label=i['title']['label'])
    #print(i['content']['label'])
            self.worksheet.write(j, 5, label=i['content']['label'])
            #sentiments
            s_title=snownlp.SnowNLP(i['title']['label'])
            s_title=float('%.2f' % s_title.sentiments)
            #print(s)
            self.worksheet.write(j, 6, label=s_title)

            s_content=snownlp.SnowNLP(i['content']['label'])
            s_content=float('%.2f' % s_content.sentiments)
            #print(s)
            self.worksheet.write(j, 7, label=s_content)

            j+=1
        #else：
         #   break

        self.workbook.save(path)
        print('Excel文件保存完成到:{}'.format(path))


    def save_mysql(self,feedback_json_all):
        cur = self.db.cursor()
        cur.execute('use feedback_database')
        try:
            create_projectid_table='create table projectid_%d(author varchar(100),version varchar(10),rating int(20),id varchar(30),title text(50),content text(2000),sent_title float(8),sent_content float(8))'%self.ProjectID
            #print(create_projectid_table)
            cur.execute(create_projectid_table)
            self.db.commit()
            print('----------------Table 创建成功----------------')
        except Exception as e:
            pass
            #print("Mysql Err:{}".format(e))
        #j = 1
        projectid = 'projectid_%s' % self.ProjectID
        idcount = 0
        for i in feedback_json_all:
            # author_name = i['author']['name']['label']
            argv="author,version,rating,id,title,content,sent_title,sent_content"

            author=str(i['author']['name']['label'])
            #print(author)
            version = str(i['im:version']['label'])
            rating = str(i['im:rating']['label'])
            id = str(i['id']['label'])
            title = str(i['title']['label'])
            content = str(i['content']['label'])
            sent_title=float('%.2f' %snownlp.SnowNLP(title).sentiments)
            sent_content=float('%.2f' %snownlp.SnowNLP(content).sentiments)
            #print(sent_title)
            mql_value=(author,version,rating,id,title,content,sent_title,sent_content)
            #print(mql_value)
            try:
                ss="select  * from {} where id = {} ".format(projectid,id)
                idcount = cur.execute(ss)
            except Exception as e:
                print('运行错误',e)

            #print(idcount)
            if idcount==0:#判断是否有数据。如果没有插入新数据。
                insert_content='insert into {}({}) values{}'.format(projectid,argv,mql_value)
            #print(insert_content)
                cur.execute(insert_content)
            elif idcount!=0:
                print('有重复！！ {}'.format(id))
            #j += 1
            self.db.commit()  # 提交数据
        cur.close()
        self.db.close()
        print('mql saved')


    #暂时不可用
        #cursor.execute()
    # def train_snownlp(self):
    #     cur = self.db.cursor()
    #     projectid = 'projectid_%s' % self.ProjectID
    #     select_content="select  content from {}".format(projectid)
    #     train_content=cur.execute(select_content)
    #     train_content_file=open("./trainFile.txt","w")
    #     train_content_file.write(str(train_content))
    #     train_content_file.close()
    #     snownlp.sentiment.train("./trainFile.txt")
    #     snownlp.sentiment.save('sentiment.marshal')
    #     print('-------------Train Finished---------------')

def main():
    #输入配置数据
    #ProjectID=int(input('Please input ProjectID: '))
    #414478124
    #print("Star/Endpage 应该小于等于10")
    #startpage=int(input('StartPage: '))
    #endpage=int(input('EndPage: '))
    # if endpage-startpage<0 or endpage<=0 or startpage<=0:
    #     print('--------输入错误-------')
    #     raise ValueError
    # else:
    #     pass
    #连接DB
    db = pymysql.connect(host, username, password, database)

    a = feedbackclass(ProjectID=414478124,startpage=1,endpage=10,db=db)

    getfeedback=a.getfeedback_info()
    #存储数据到excel。Path路径头部自己配置更改
    a.save_feedback(path=Path,feedback_json_all=getfeedback)
    #存储新增数据到DB，会校验数据是否已经存储。
    a.save_mysql(feedback_json_all=getfeedback)
    #a.train_snownlp();


if __name__ == '__main__':
    main()

