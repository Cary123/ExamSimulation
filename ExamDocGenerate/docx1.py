from docxtpl import DocxTemplate
from docxtpl import RichText
import bs4

tpl = DocxTemplate('./tpl/c_exam.docx')

#  需要替换内容以key:value的方式进行更换

context = {
    'choose1_A': 'C 语言程序总是从第一个的函数开始执行',
    'choose1_B': '在 C 语言程序中，要调用函数必须在 main （）函数中定义',
    'choose1_C': 'C 语言程序总是从 main （）函数开始执行',
    'choose1_D': 'C 语言程序中的 main （）函数必须放在程序的开始部分',
    'choose2_A': '有零个输入或多个输入',
    'choose2_B': '高效性',
    'choose2_C': '有穷性',
    'choose2_D': '确定性'
}

tpl.render(context)
tpl.save('leave.docx')
