import time
d = {}
str = '''[00:03.50]传奇
[00:19.10]作词：刘兵 作曲：李健
[00:20.60]演唱：王菲
[00:26.60]
[04:40.75][02:39.90][00:36.25]只是因为在人群中多看了你一眼
[04:49.00]
[02:47.44][00:43.69]再也没能忘掉你容颜
[02:54.83][00:51.24]梦想着偶然能有一天再相见
[03:02.32][00:58.75]从此我开始孤单思念
[03:08.15][01:04.30]
[03:09.35][01:05.50]想你时你在天边         
[03:16.90][01:13.13]想你时你在眼前
[03:24.42][01:20.92]想你时你在脑海
[03:31.85][01:28.44]想你时你在心田
[03:38.67][01:35.05]
[04:09.96][03:39.87][01:36.25]宁愿相信我们前世有约
[04:16.37][03:46.38][01:42.47]今生的爱情故事 不会再改变
[04:24.82][03:54.83][01:51.18]宁愿用这一生等你发现
[04:31.38][04:01.40][01:57.43]我一直在你身旁 从未走远
[04:39.55][04:09.00][02:07.85]
'''
musicLine = str.splitlines()
for mling in musicLine:
    qmling = mling.split("]")
    for index in range(len(qmling)-1):
        time1 = qmling[index][1:]
        timelist = time1.split(":")
        tkey = float(timelist[0])*60 + float(timelist[1])
        d[tkey] = qmling[-1]
# getTime = float(input("请输入时间："))
# list = []
# for key in d:
#     list.append(key)
# list.sort()
# for n in range(len(list)):
#     linshitime = list[n]
#     if getTime < linshitime:
#         break
# if n == 0:
#     print("时间太小")
# else:
#     print(d[list[n - 1]])
list = []
for key in d:
    list.append(key)
list.sort()
getTime = 0
print(list)
while 1:
    for n in range(len(list)):
        linshitime = list[n]
        if getTime < linshitime:
            break
    irc = d.get(list[n - 1])
    if irc == None:
        pass
    else:
        print(irc)
    time.sleep(1.0)
    getTime += 1
    print(getTime)
print(d)