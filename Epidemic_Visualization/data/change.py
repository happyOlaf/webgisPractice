'''
获取文件信息
'''
fi = open("usa.txt",encoding='UTF-8')
lines = fi.readlines()
txt = open("usaout.txt",mode='w',encoding='UTF-8')
# 读取身高大于170cm
data = []
# lines =lines.split("\n");
for line in lines:
    line=line.strip('\n')  #去掉换行符
    txt.write('{name:' + line + ', value: 1},' + '\n')
    # line = "'"+line+"',"     
    
print("data{}".format(line))


""" for human in lines:
    ## hinfo = human.split()
    if hinfo:
        if int(hinfo[1][:3]) >= 170:
            data.append(tuple(hinfo)) """
 
'''
写入excel
'''
""" import xlwt
 
# 创建workbook和sheet对象
workbook = xlwt.Workbook()  # Workbook的开头W 大写
sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
# 向sheet页中写入数据
sheet1.write(0, 0, '姓名')
sheet1.write(0, 1, '身高cm')
row = 1
for i in data:
    sheet1.write(row, 0, i[0])  # i0 姓名
    sheet1.write(row, 1, i[1])  # i1 身高
    row += 1
 
workbook.save('c.xlsx')  # 写入excel """