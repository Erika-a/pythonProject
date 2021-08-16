# coding=utf-8

s_dict = {102:'zhangsan',105:'lisi',109:'wangwu'}

print('---bianlijian---')
for s_id in s_dict.keys():
	print('xuehao:'+str(s_id))

print('---bianlizhi---')
for s_id in s_dict.values():
	print('xuesheng：' + s_name)

print('---bianlijian:zhi---')
for s_id,s_name in s_dict.items():
	print('xuehao:{0}' - 'xuesheng：{1}'.format(s_id,s_name))
