import pandas as pd

# 创建 DataFrame
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [30, 45, 20, 40, 60]
})

with pd.ExcelWriter('gradient_chart.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # 创建图表对象
    chart = workbook.add_chart({'type': 'column'})
    chart.add_series({
        'name': 'Value',
        'categories': '=Sheet1!$A$2:$A$6',
        'values': '=Sheet1!$B$2:$B$6',
        'data_labels': {'value': True},  # 添加数据标签
        'fill': {'color': 'blue', 'gradient': {'colors': ['#00F', '#004'], 'type': 'linear', 'angle': 90}}
    })

    # 配置图表
    chart.set_title({'name': 'Category Values with Gradient'})
    chart.set_x_axis({'name': 'Category'})
    chart.set_y_axis({'name': 'Value'})

    # 将图表插入工作表
    worksheet.insert_chart('E2', chart)
