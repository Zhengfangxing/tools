import pandas as pd

# 创建 DataFrame
df = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Product A': [10, 20, 30, 40],
    'Product B': [15, 25, 35, 45]
})

with pd.ExcelWriter('stacked_column_chart.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # 创建图表对象
    chart = workbook.add_chart({'type': 'column', 'subtype': 'stacked'})
    chart.add_series({
        'name': 'Product A',
        'categories': '=Sheet1!$A$2:$A$5',
        'values': '=Sheet1!$B$2:$B$5'
    })
    chart.add_series({
        'name': 'Product B',
        'categories': '=Sheet1!$A$2:$A$5',
        'values': '=Sheet1!$C$2:$C$5'
    })

    # 配置图表
    chart.set_title({'name': 'Product Sales by Month'})
    chart.set_x_axis({'name': 'Month'})
    chart.set_y_axis({'name': 'Sales'})
    chart.set_style(11)  # 设置样式

    # 将图表插入工作表
    worksheet.insert_chart('E2', chart)
