import multiprocessing

from gooey import Gooey, GooeyParser
from 文件重命名2 import FileRename1
from 文件重命名2 import gettime



@Gooey(
    # richtext_controls=True,                 # 打开终端对颜色支持
    program_name="3dt文件命名小工具",        # 程序名称
    encoding="utf-8",                       # 设置编码格式，打包的时候遇到问题
    progress_regex=r"^progress: (\d+)%$",   # 正则，用于模式化运行时进度信息
    language='chinese',
    default_size=(800,600),
    tabbed_groups=True
)
def main():
    settings_msg = '多种文件命名方式'
    parser = GooeyParser(description=settings_msg)

    subs = parser.add_subparsers(help='commands', dest='command')

    my_parser = subs.add_parser('3DT批量转换')
    my_parser.add_argument("connect", metavar='运行环境',help="请选择开发环境",choices=['dev环境','staging环境'], default='dev环境')
    my_parser.add_argument("device_type",metavar='设备类型',help="请选择设备类型",choices=['H1','H3'],default='H1')
    my_parser.add_argument("serialNumber", metavar='设备SN号',default='LKVC19060047',help='多个请用逗号或空格隔开')

    siege_parser = subs.add_parser('pak文件重命名为3dt')
    siege_parser.add_argument("pakpath",help='请输入pak路径',default=r'E:\UE_Project\pak\WindowsNoEditor\AirCityExplorer\Content\Paks\AirCityExplorer-WindowsNoEditor.pak')
    siege_parser.add_argument("dtpath", help='请输入3dt路径',default=r'E:\OSGB\{0}\3dt'.format(gettime()))
    siege_parser.add_argument("name", help='请输入文件名', default='3dt')


    # siege_parser = subs.add_parser('pak文件重命名为3dt3')
    # siege_parser.add_argument('pak路径', help='请输入pak路径',
    #                           default=r'C:\Users\PC\Desktop\WindowsNoEditor\AirCityExplorer\Content\Paks')
    # siege_parser.add_argument('3dt路径', help='请输入3dt路径', default=r'E:\OSGB')

    args = parser.parse_args()
    FileRename1(args.pakpath,args.dtpath,args.name)
    print(args, flush=True)    # flush=True在打包的时候会用到


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()