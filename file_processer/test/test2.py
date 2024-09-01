import pandas as pd

# 创建 DataFrame
df = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [200, 220, 250, 270, 300],
    'Expenses': [150, 170, 200, 210, 250]
})

with pd.ExcelWriter('multi_series_chart.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # 创建图表对象
    chart = workbook.add_chart({'type': 'line'})
    chart.add_series({
        'name': 'Sales',
        'categories': '=Sheet1!$A$2:$A$6',
        'values': '=Sheet1!$B$2:$B$6',
        'line': {'color': 'blue', 'width': 2}
    })
    chart.add_series({
        'name': 'Expenses',
        'categories': '=Sheet1!$A$2:$A$6',
        'values': '=Sheet1!$C$2:$C$6',
        'line': {'color': 'red', 'width': 2}
    })

    # 配置图表
    chart.set_title({'name': 'Sales and Expenses Over Time'})
    chart.set_x_axis({'name': 'Month'})
    chart.set_y_axis({'name': 'Amount', 'major_gridlines': {'visible': False}})
    chart.set_style(10)  # 设置样式

    # 将图表插入工作表
    worksheet.insert_chart('E2', chart)
