import pandas


def read_from_excel():
    global df
    # 读取 Excel 文件
    df = pandas.read_excel('example.xlsx', sheet_name='Sheet1')  # 替换 'Sheet1' 为实际的工作表名称
    # 显示 DataFrame 的前几行
    print(df.head())


def write_to_excel():
    global df
    # 创建一个示例 DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pandas.DataFrame(data)
    # 将 DataFrame 写入 Excel 文件
    df.to_excel('output.xlsx', index=False, sheet_name='Sheet1')  # index=False 表示不写入行索引


def chart_line():
    # 创建 DataFrame 并写入 Excel 文件
    df = pandas.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    })
    with pandas.ExcelWriter('chart_output.xlsx', engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        # 创建图表
        chart = workbook.add_chart({'type': 'column'})
        chart.add_series({'values': '=Sheet1!$B$2:$B$4', 'name': 'Age'})

        # 插入图表到工作表
        worksheet.insert_chart('E2', chart)


if __name__ == '__main__':
    chart_line()