import pandas as pd

# 创建 DataFrame
df = pd.DataFrame({
    'Item': ['Item A', 'Item B', 'Item C', 'Item D'],
    'Value': [10, 20, 30, 40]
})

with pd.ExcelWriter('pie_chart.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # 创建图表对象
    chart = workbook.add_chart({'type': 'pie'})
    chart.add_series({
        'name': 'Items',
        'categories': '=Sheet1!$A$2:$A$5',
        'values': '=Sheet1!$B$2:$B$5',
        'data_labels': {'percentage': True, 'category': True, 'value': True}
    })

    # 配置图表
    chart.set_title({'name': 'Item Distribution'})

    # 将图表插入工作表
    worksheet.insert_chart('E2', chart)
